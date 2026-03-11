"""Tests for inference API.
Run with: pytest -q
"""

#start code here
# TODO: create tests for:

from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)

# 1) /health returns HTTP 200

def test_health_ok():
    res = client.get("/health")
    assert res.status_code == 200
    body  = res.json()
    assert body["status"] == "ok"
    assert "model_version" in body

# 2) /predict validates request schema

def test_predict_ok():
    payload = {"feature_1": 1.2, "feature_2": 0.8}
    res = client.post("/predict", json = payload)
    assert res.status_code == 200
    body = res.json()
    assert "model_name" in body
    assert "model_version" in body
    assert "score" in body
    assert isinstance(body["score"], float)

# 3) /predict returns expected output shape


# 4) deterministic prediction on same payload

def test_predict_deterministic():
    payload = {"feature_1": 2.0, "feature_2": 3.0}
    a = client.post("/predict", json = payload)
    b = client.post("/predict", json = payload)
    assert a.status_code == 200
    assert b.status_code == 200
    assert a.json()["score"]  == b.json()["score"]

# 5) invalid payload returns 4xx
def test_predict_invalid_payload_returns_422():
    payload = {"feature_1": "bad_type", "feature_2": 0.8}
    res = client.post("/predict", json = payload)
    assert res.status_code == 422

#send code here
