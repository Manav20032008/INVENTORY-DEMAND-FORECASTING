from fastapi import Request
from fastapi.responses import JSONResponse

from backend.exceptions.custom_exceptions import ModelNotFoundException, PredictionException


async def model_not_found_handler(request: Request, exc: ModelNotFoundException):
    return JSONResponse(
        status_code=404,
        content={"success": False, "message": exc.message},
    )


async def prediction_handler(request: Request, exc: PredictionException):
    return JSONResponse(
        status_code=500,
        content={"success": False, "message": exc.message},
    )
