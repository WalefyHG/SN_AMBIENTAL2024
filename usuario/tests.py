import pytest
from rest_framework.test import APIClient
from usuario.models import Usuario


@pytest.mark.django_db

# Testando o endpoint de criação de usuário caso o usuario não exista

def test_create_user():
    client = APIClient()
    url = '/criandoUsuario'
    
    user_data = {
        'nome': 'Teste',
        'email': 'teste@gmail.com',
        'senha': '123456' 
    }
    
    response = client.post(url, user_data, format='json')
    assert response.status_code == 200
    
# Testando o endpoint de criação de usuário caso o usuario exista

@pytest.mark.django_db
def test_create_user_exists():
    client = APIClient()
    url = '/criandoUsuario'
    
    user_data = {
        'nome': 'Teste',
        'email': 'teste@gmail.com',
        'senha': '123456'
    }
    
    response = client.post(url, user_data, format='json')
    assert response.status_code == 200
    
    response = client.post(url, user_data, format='json')
    assert response.status_code == 400
    
# Testando o endpoint de login caso o usuario exista

@pytest.mark.django_db
def test_login_user():
    client = APIClient()
    url = '/login'
    
    user = Usuario.objects.create(
        nome= 'Teste',
        email= 'teste@gmail.com',
        senha= '123456'
    )
 
    user_data = {
        'email': 'teste@gmail.com',
        'senha': '123456'
    }
    
    response = client.post(url, user_data, format='json')
    assert response.status_code == 200


# Testando o endpoint de login caso a senha esteja incorreta

@pytest.mark.django_db

def test_login_user_wrong_password():
    client = APIClient()
    url = '/login'
    
    user = Usuario.objects.create(
        nome= 'Teste',
        email= 'teste@gmail.com',
        senha= '123456'
    )
    
    user_data = {
        'email': 'teste@gmail.com',
        'senha': '12345'
    }
    
    response = client.post(url, user_data, format='json')
    assert response.status_code == 404


# Testando o endpoint de login caso o usuario não exist

@pytest.mark.django_db

def test_login_user_not_exists():
    client = APIClient()
    url = '/login'
    
    user_data = {
        'email': 'teste@gmail.com',
        'senha': '123456'
    }
    
    response = client.post(url, user_data, format='json')
    assert response.status_code == 406
    
    
# Testando o endpoint de listar todos os usuarios

@pytest.mark.django_db

def test_list_users():
    client = APIClient()
    url = '/listarUsuario'
    
    user = Usuario.objects.create(
        nome= 'Teste',
        email= 'teste@gmail.com',
        senha= '123456'
    )
    
    user_data = {
        'email': 'teste@gmail.com',
        'senha': '123456'
    }
    
    login_response = client.post('/login', user_data, format='json')
    assert login_response.status_code == 200
    assert 'token' in login_response.json()
    
    token = login_response.json()['token']
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    response = client.get(url)
    assert response.status_code == 200
    
# Testando listar usuario pelo ID

@pytest.mark.django_db

def test_list_user_by_id():
    client = APIClient()
    url = '/listarUsuario/'
    
    user = Usuario.objects.create(
        nome= 'Teste',
        email= 'teste@gmail.com',
        senha= '123456'
    )
    
    user_data = {
        'email': 'teste@gmail.com',
        'senha': '123456'
    }
    
    login_response = client.post('/login', user_data, format='json')
    assert login_response.status_code == 200
    assert 'token' in login_response.json()
    
    token = login_response.json()['token']
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    response = client.get(url + str(user.id))
    assert response.status_code == 200
    
# Testando listar usuario pelo ID caso o usuario não exista

@pytest.mark.django_db

def test_list_user_by_id_not_exists():
    client = APIClient()
    url = '/listarUsuario/'
    
    user = Usuario.objects.create(
        nome= 'Teste',
        email= 'teste@gmail.com',
        senha= '123456'
    )
    
    user_data = {
        'email': 'teste@gmail.com',
        'senha': '123456'
    }
    
    login_response = client.post('/login', user_data, format='json')
    assert login_response.status_code == 200
    assert 'token' in login_response.json()
    
    token = login_response.json()['token']
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    response = client.get(url + '10')
    assert response.status_code == 404

# Testando atualizar o usuario pelo id

@pytest.mark.django_db

def test_update_user():
    client = APIClient()
    url = '/atualizarUsuario/'
    
    user = Usuario.objects.create(
        nome= 'Teste',
        email= 'teste@gmail.com',
        senha= '123456'
    )
    
    user_data = {
        'email': 'teste@gmail.com',
        'senha': '123456'
    }
    
    login_response = client.post('/login', user_data, format='json')
    assert login_response.status_code == 200
    assert 'token' in login_response.json()
    
    token = login_response.json()['token']
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    user_data = {
        'nome': 'Teste2',
        'email': 'teste@gmail.com',
        'senha': '123456'
    }
    
    response = client.put(url + str(user.id), user_data, format='json')
    assert response.status_code == 200

# Testando atulizar o usuario pelo id caso o usuario não exista

@pytest.mark.django_db

def test_update_user_not_exists():
    client = APIClient()
    url = '/atualizarUsuario/'
    
    user = Usuario.objects.create(
        nome= 'Teste',
        email= 'teste@gmail.com',
        senha= '123456'
    )
    
    user_data = {
        'email': 'teste@gmail.com',
        'senha': '123456'
    }
    
    login_response = client.post('/login', user_data, format='json')
    assert login_response.status_code == 200
    assert 'token' in login_response.json()
    
    token = login_response.json()['token']
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    
    user_data = {
        'nome': 'Teste2',
        'email': 'teste@gmail.com',
        'senha': '123456'
    }
    
    response = client.put(url + '10', user_data, format='json')
    assert response.status_code == 404
        
        
# Testando o endpoint de deletar o usuario pelo id

@pytest.mark.django_db

def test_delete_user():
    client = APIClient()
    url = '/deletarUsuario/'
    
    user = Usuario.objects.create(
        nome= 'Teste',
        email= 'teste@gmail.com',
        senha= '123456'
    )
    
    user_data = {
        'email': 'teste@gmail.com',
        'senha': '123456'
    }
    
    login_response = client.post('/login', user_data, format='json')
    assert login_response.status_code == 200
    assert 'token' in login_response.json()
    
    token = login_response.json()['token']
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    
    response = client.delete(url + str(user.id))
    assert response.status_code == 200
    
# Testando o endpoint de deletar o usuario pelo id caso o usuario não exista

@pytest.mark.django_db

def test_delete_user_not_exists():
    client = APIClient()
    url = '/deletarUsuario/'
    
    user = Usuario.objects.create(
        nome= 'Teste',
        email= 'teste@gmail.com',
        senha= '123456'
    )
    
    user_data = {
        'email': 'teste@gmail.com',
        'senha': '123456'
    }
    
    login_response = client.post('/login', user_data, format='json')
    assert login_response.status_code == 200
    assert 'token' in login_response.json()
    
    token = login_response.json()['token']
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    
    response = client.delete(url + '10')
    assert response.status_code == 404