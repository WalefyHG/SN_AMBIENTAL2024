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