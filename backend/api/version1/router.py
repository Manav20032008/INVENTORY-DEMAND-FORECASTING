from fastapi import APIRouter

from backend.api.version1.routes import router as version1_router

api_router = APIRouter()
api_router.include_router(version1_router)
