from fastapi.middleware.cors import CORSMiddleware
from backend.core.settings import settings


def configure_cors(app) -> None:
    app.add_middleware(CORSMiddleware  , allow_origins=settings.CORS_ORIGINS ,allow_credentials=True, allow_methods=["*"],allow_headers=["*"],)
