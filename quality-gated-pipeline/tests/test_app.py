import pytest
from app.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_endpoint(client):
    """Test the main landing page"""
    res = client.get('/')
    assert res.status_code == 200
    assert res.json['status'] == "UP"

def test_health_endpoint(client):
    """Test the health check endpoint"""
    res = client.get('/health')
    assert res.status_code == 200
    assert res.json['status'] == "Healthy"