import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_product(client):
    response = client.get('/products/1')
    assert response.status_code == 200
    assert 'name' in response.json
