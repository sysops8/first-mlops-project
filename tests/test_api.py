import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Diabetes Prediction API is live"}

def test_predict_diabetic():
    payload = {
        "Pregnancies": 2,
        "Glucose": 130,
        "BloodPressure": 70,
        "BMI": 28.5,
        "Age": 45
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "diabetic" in response.json()
    assert response.json()["diabetic"] == True

def test_predict_non_diabetic():
    payload = {
        "Pregnancies": 1,
        "Glucose": 85,
        "BloodPressure": 66,
        "BMI": 26.6,
        "Age": 31
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert response.json()["diabetic"] == False
