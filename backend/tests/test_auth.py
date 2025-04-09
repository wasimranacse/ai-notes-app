import sys
import os
from fastapi.testclient import TestClient

# Adjust sys.path to ensure app is importable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

# Import the FastAPI app from main.py
from app.main import app

client = TestClient(app)

def test_valid_api_key():
    response = client.get("/notes", headers={"X-API-KEY": "local123987@1122!"})
    assert response.status_code == 200
