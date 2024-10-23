# Unit tests for the API
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_start_mission(client):
    response = client.post('/start_mission', json={'mission_name': 'Test Mission'})
    assert response.status_code == 200
    assert b'Mission started' in response.data
