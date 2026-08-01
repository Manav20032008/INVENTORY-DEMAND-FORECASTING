from unittest.mock import MagicMock, patch

import pytest
from fastapi.testclient import TestClient

from backend.app import app


@pytest.fixture
def client():
    return TestClient(app)


def test_root_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


@patch("backend.services.health_service.HealthService.check_database", return_value="connected")
@patch("backend.services.health_service.HealthService.check_model", return_value="loaded")
def test_health_endpoint(mock_model, mock_db, client):
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["database"] == "connected"
    assert data["model"] == "loaded"


@patch("backend.services.prediction_service.PredictionService.predict", return_value=42.5)
def test_predict_endpoint(mock_predict, client):
    payload = {
        "store": 1,
        "item": 1,
        "year": 2017,
        "month": 1,
        "day": 1,
        "daysofweek": 6,
        "weekofyear": 1,
        "quarter": 1,
        "is_weekend": 1,
        "lag_1": 15.0,
        "lag_7": 14.0,
        "lag_30": 16.0,
        "rolling_mean_7": 14.8,
        "rolling_std_7": 1.2,
        "rolling_mean_30": 15.2,
        "rolling_std_30": 1.3,
    }
    response = client.post("/api/v1/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["predicted_sales"] == 42.5


@patch(
    "backend.services.prediction_service.PredictionService.get_prediction_history",
    return_value=[],
)
def test_predictions_endpoint(mock_history, client):
    response = client.get("/api/v1/predictions")
    assert response.status_code == 200
    assert response.json() == []


@patch(
    "backend.services.analytics_service.AnalyticsService.get_dashboard_analytics",
    return_value={
        "total_predictions": 10,
        "average_prediction": 20.5,
        "highest_prediction": 50.0,
        "lowest_prediction": 5.0,
        "unique_stores": 3,
        "unique_items": 4,
    },
)
def test_analytics_endpoint(mock_analytics, client):
    response = client.get("/api/v1/analytics")
    assert response.status_code == 200
    data = response.json()
    assert data["total_predictions"] == 10
