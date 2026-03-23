from app.tests.conftest import auth_headers


def test_publico_sin_token(client):
    response = client.get('/events/')
    assert response.status_code == 200

def test_endpoint_protegido_con_token(client,auth_headers):
    response = client.get('/events/', headers=auth_headers)
    assert  response.status_code == 200

def test_crear_evento_sin_token(client):
    response = client.post('/events/', json={
        'name' : 'Evento test',
        'date' : '2025-01-01'
    })
    assert  response.status_code == 401

def test_crear_evento_con_token(client, auth_headers):
    response = client.post('/events/', json={
        'title': 'Evento test',
        'date': '2025-01-01T00:00:00',
        'place': 'Rotterdam',
        'capacity': 100
    }, headers=auth_headers)
    assert response.status_code == 200