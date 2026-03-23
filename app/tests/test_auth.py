

def test_register_exitoso(client):
    response = client.post('/auth/register',json={
        'name': 'Test User',
        'email' : 'nuevo@test.com',
        'password' : 'password123'
    })

    assert response.status_code == 200
    assert 'access_token' in response.json()

def test_login_exitoso(client):
    #Primero registramos
    client.post('/auth/register', json={
        'name' : 'Test User',
        'email': 'login@test.com',
        'password': 'password123'
    })

    #Luego logueamos
    response = client.post('/auth/login', json={
        'email': 'login@test.com',
        'password': 'password123'
    })
    assert response.status_code == 200
    assert 'access_token' in response.json()

def test_login_password_incorrecta(client):
    response = client.post('/auth/login', json={
        'email': 'login@test.com',
        'password': 'passwordmala'
    })
    assert response.status_code == 401


def test_login_usuario_no_existe(client):
    response = client.post('auth/login', json={
        'email': 'noexiste@test.com',
        'password': 'password123'
    })
    assert response.status_code == 401
