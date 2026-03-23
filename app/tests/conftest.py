import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.core.database import get_db,Base,engine

@pytest.fixture(autouse=True)
def reset_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def auth_token(client):
    #Crea un usuario y devuelve su token
    client.post('/auth/register', json={
        'name': 'Test User',
        'email': "test@test.com",
        'password': 'testpassword123'
    })
    response = client.post('/auth/login',json={
        'email' :'test@test.com',
        'password': 'testpassword123'
    })
    return response.json()['access_token']

@pytest.fixture
def auth_headers(auth_token):
    return {'Authorization': f"Bearer {auth_token}"}
