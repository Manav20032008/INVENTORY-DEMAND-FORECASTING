from fastapi import FastAPI

from backend.routers.prediction_router import router as prediction_router

from backend.exceptions.custom_exceptions import (
    ModelNotFoundException,
    PredictionException
)

from backend.exceptions.exception_handlers import (
    model_not_found_handler,
    prediction_handler
)


app = FastAPI(
    title="Inventory Demand API",
    version="1.0")

app.add_exception_handler(
    ModelNotFoundException,
    model_not_found_handler
)

app.add_exception_handler(
    PredictionException,
    prediction_handler
)

app.include_router(prediction_router)


@app.get("/")
def home():

    return {
        "message":
        "Inventory Demand Forecast API"
    }