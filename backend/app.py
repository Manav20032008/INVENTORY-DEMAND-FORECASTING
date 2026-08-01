from contextlib import asynccontextmanager

from fastapi import FastAPI

from backend.api.v1.router import api_router
from backend.core.settings import settings
from backend.exceptions.custom_exceptions import ModelNotFoundException, PredictionException
from backend.exceptions.exception_handlers import model_not_found_handler, prediction_handler
from backend.logging.logger import get_logger
from backend.middleware.cors import configure_cors
from backend.middleware.logging_middleware import RequestLoggingMiddleware

logger = get_logger()


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting Inventory Demand API env=%s", settings.APP_ENV)
    yield
    logger.info("Shutting down Inventory Demand API")


app = FastAPI(
    title=settings.API_TITLE,
    version=settings.API_VERSION,
    description="Production-grade inventory demand forecasting API powered by XGBoost.",
    lifespan=lifespan,
)

configure_cors(app)
app.add_middleware(RequestLoggingMiddleware)

app.add_exception_handler(ModelNotFoundException, model_not_found_handler)
app.add_exception_handler(PredictionException, prediction_handler)

app.include_router(api_router, prefix=settings.API_PREFIX)

# Legacy unversioned routes for backward compatibility
app.include_router(api_router)


@app.get("/", tags=["Root"])
def home():
    return {
        "message": "Inventory Demand Forecast API",
        "version": settings.API_VERSION,
        "docs": "/docs",
        "health": f"{settings.API_PREFIX}/health",
    }


@app.get("/health", tags=["Health"])
def root_health():
    from backend.services.health_service import HealthService

    return HealthService.get_health()
