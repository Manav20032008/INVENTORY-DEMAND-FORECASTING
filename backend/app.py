from fastapi import FastAPI

from backend.routers.prediction_router import router as prediction_router

from backend.exceptions.custom_exceptions import (
    model_not_found_execption,
    predictiob_execption
)

from backend.exceptions.exception_handlers import (
    model_not_found_handler,
    prediction_handler
)


app = FastAPI(
    title="Inventory Demand API",
    version="1.0")

app.add_exception_handler(
    model_not_found_execption,
    model_not_found_handler
)

app.add_exception_handler(
    predictiob_execption,
    prediction_handler
)

app.include_router(prediction_router)


@app.get("/")
def home():

    return {
        "message":
        "Inventory Demand Forecast API"
    }