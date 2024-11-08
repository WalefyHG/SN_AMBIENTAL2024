import pytest
from rest_framework.test import APIClient
from pedido.schemas import PedidosStatusType
from itens_pedidos.schemas import ItensPedidosCategoriaType
from usuario.models import Usuario
from pedido.models import Pedido
from itens_pedidos.models import ItensPedidos
from django.utils import timezone
from decimal import Decimal


# Testando o endpoint de criação de itens de pedido

@pytest.mark.django_db

def test_create_itens_pedido():
    client = APIClient()
    url = '/criarItem'
    
    user = Usuario.objects.create(
        nome='Teste',
        email= 'teste@gmail.com',
        senha= '123456'
    )
    
    login_data = {
        'email': 'teste@gmail.com',
        'senha': '123456'
    }
    
    order = Pedido.objects.create(
        usuario_id=user,
        data_pedido='2021-10-10',
        total=100.0,
        status=PedidosStatusType.pendente.value
    )
    
    login_response = client.post('/login', login_data, format='json')
    assert login_response.status_code == 200
    assert 'token' in login_response.json()
    
    token = login_response.json()['token']
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    
    data = {
        'pedido_id': order.id,
        'nome': 'Salada Verde',
        'preco': 50.0,
        'descricao': 'Uma salada verde',
    }
    
    response = client.post(f"{url}?itens_pedidos_status={ItensPedidosCategoriaType.salada.value}", data, format='json')
    print(response.json())
    print(response.status_code)
    assert response.status_code == 200

# Testando o endpoint de criar itens, mas não existe pedido

@pytest.mark.django_db

def test_create_itens_pedido_not_exists():
    client = APIClient()
    url = '/criarItem'
    
    user = Usuario.objects.create(
        nome='Teste',
        email= 'teste@gmail.com',
        senha= '123456'
    )
    
    login_data = {
        'email': 'teste@gmail.com',
        'senha': '123456'
    }
    
    order = Pedido.objects.create(
        usuario_id=user,
        data_pedido='2021-10-10',
        total=100.0,
        status=PedidosStatusType.pendente.value
    )
    
    login_response = client.post('/login', login_data, format='json')
    assert login_response.status_code == 200
    assert 'token' in login_response.json()
    
    token = login_response.json()['token']
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    
    data = {
        'pedido_id': 10,
        'nome': 'Salada Verde',
        'preco': 50.0,
        'descricao': 'Uma salada verde',
    }
    
    response = client.post(f"{url}?itens_pedidos_status={ItensPedidosCategoriaType.salada.value}", data, format='json')
    assert response.status_code == 404
    
# Testando o endpoint de listar todos os itens

@pytest.mark.django_db

def test_list_itens():
    client = APIClient()
    url = '/listarItens'
    
    user = Usuario.objects.create(
        nome='Teste',
        email= 'teste@gmail.com',
        senha= '123456'
    )
    
    login_data = {
        'email': 'teste@gmail.com',
        'senha': '123456'
    }
    
    order = Pedido.objects.create(
        usuario_id=user,
        data_pedido='2021-10-10',
        total=100.0,
        status=PedidosStatusType.pendente.value
    )
    
    item = ItensPedidos.objects.create(
        pedido_id=order,
        nome='Salada Verde',
        preco=50.0,
        descricao='Uma salada verde',
        categoria=ItensPedidosCategoriaType.salada.value
    )
    
    login_response = client.post('/login', login_data, format='json')
    assert login_response.status_code == 200
    assert 'token' in login_response.json()
    
    token = login_response.json()['token']
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    
    response = client.get(url)
    assert response.status_code == 200
    
# Testando o endpoint de listar item pelo ID

@pytest.mark.django_db

def test_list_item_by_id():
    
    client = APIClient()
    url = '/listarItem/'
    
    user = Usuario.objects.create(
        nome='Teste',
        email= 'teste@gmail.com',
        senha= '123456'
    )
    
    login_data = {
        'email': 'teste@gmail.com',
        'senha': '123456'
    }
    
    order = Pedido.objects.create(
        usuario_id=user,
        data_pedido='2021-10-10',
        total=100.0,
        status=PedidosStatusType.pendente.value
    )
    
    item = ItensPedidos.objects.create(
        pedido_id=order,
        nome='Salada Verde',
        preco=50.0,
        descricao='Uma salada verde',
        categoria=ItensPedidosCategoriaType.salada.value
    )
    
    login_response = client.post('/login', login_data, format='json')
    assert login_response.status_code == 200
    assert 'token' in login_response.json()
    
    token = login_response.json()['token']
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    
    response = client.get(f"{url}{item.id}")
    assert response.status_code == 200
    
# Testando o endpoint de listar o item pelo ID, mas passando o id errado

@pytest.mark.django_db

def test_list_item_by_id_not_exists():
    
    client = APIClient()
    url = '/listarItem/'
    
    user = Usuario.objects.create(
        nome='Teste',
        email= 'teste@gmail.com',
        senha= '123456'
    )
    
    login_data = {
        'email': 'teste@gmail.com',
        'senha': '123456'
    }
    
    order = Pedido.objects.create(
        usuario_id=user,
        data_pedido='2021-10-10',
        total=100.0,
        status=PedidosStatusType.pendente.value
    )
    
    item = ItensPedidos.objects.create(
        pedido_id=order,
        nome='Salada Verde',
        preco=50.0,
        descricao='Uma salada verde',
        categoria=ItensPedidosCategoriaType.salada.value
    )
    
    login_response = client.post('/login', login_data, format='json')
    assert login_response.status_code == 200
    assert 'token' in login_response.json()
    
    token = login_response.json()['token']
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    
    response = client.get(f"{url}10")
    assert response.status_code == 404
    