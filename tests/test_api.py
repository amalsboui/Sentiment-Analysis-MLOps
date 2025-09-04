import pytest
from fastapi.testclient import TestClient
from FastAPI.app import app  # Adjust if your app.py path is different

client = TestClient(app)

def test_predict_positive():
    """Test predicting a positive review."""
    response = client.post("/predict", json={"text": "I loved this movie, it was amazing!"})
    assert response.status_code == 200
    assert response.json()["sentiment"] in ["positive", "negative"]

def test_predict_negative():
    """Test predicting a negative review."""
    response = client.post("/predict", json={"text": "This movie was terrible and boring."})
    assert response.status_code == 200
    assert response.json()["sentiment"] in ["positive", "negative"]

def test_predict_empty_text():
    """Test handling of empty text input."""
    response = client.post("/predict", json={"text": ""})
    assert response.status_code == 200
    assert response.json()["sentiment"] in ["positive", "negative"]

def test_predict_invalid_payload():
    """Test invalid payload returns 422."""
    response = client.post("/predict", json={"wrong_key": "Hello"})
    assert response.status_code == 422
