import pytest
from rest_framework.test import APIClient
from usuario.models import Usuario
from pedido.models import Pedido
from pedido.schemas import PedidosStatusType


# Testando o endpoint de criar pedido caso o usuario exista

@pytest.mark.django_db
def test_create_order():
    client = APIClient()
    url = '/criarPedido'

    user = Usuario.objects.create(
        nome='Teste',
        email='teste@gmail.com',
        senha='123456'
    )
    
    order_data = {
        'usuario_id': user.id,
        'data_pedido': '2021-10-10',
        'total': 100.0,
    }
    
    login_data = {
        'email': 'teste@gmail.com',
        'senha': '123456'
    }
    
    login_response = client.post('/login', login_data, format='json')
    assert login_response.status_code == 200
    assert 'token' in login_response.json()
    
    token = login_response.json()['token']
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    response = client.post(f"{url}?pedidos_status={PedidosStatusType.pendente.value}", order_data, format='json')
    print("Create order response status:", response.status_code)
    print("Create order response data:", response.json())
    assert response.status_code == 200
    
# Testando o endpoint de criar pedido caso o usuario não exista

@pytest.mark.django_db
def test_create_order_user_not_exists():
    client = APIClient()
    url = '/criarPedido'

    user = Usuario.objects.create(
        nome='Teste',
        email= 'teste@gmail.com',
        senha= '123456'
    )
    
    order_data = {
        'usuario_id': 10,
        'data_pedido': '2021-10-10',
        'total': 100.0,
    }
    
    login_data = {
        'email': 'teste@gmail.com',
        'senha': '123456'
    }
    
    login_response = client.post('/login', login_data, format='json')
    assert login_response.status_code == 200
    assert 'token' in login_response.json()
    
    token = login_response.json()['token']
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    response = client.post(f"{url}?pedidos_status={PedidosStatusType.pendente.value}", order_data, format='json')
    assert response.status_code == 404


# Testando o endpoint de listar pedidos

@pytest.mark.django_db

def test_list_orders():
    client = APIClient()
    url = '/listarPedidos'

    user = Usuario.objects.create(
        nome='Teste',
        email= 'teste@gmail.com',
        senha= '123456'
    )
    
    order = Pedido.objects.create(
        usuario_id=user,
        data_pedido='2021-10-10',
        total=100.0,
        status=PedidosStatusType.pendente.value
    )
    
    login_data = {
        'email': 'teste@gmail.com',
        'senha': '123456'
    }
    
    login_response = client.post('/login', login_data, format='json')
    assert login_response.status_code == 200
    assert 'token' in login_response.json()
    
    token = login_response.json()['token']
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    response = client.get(url)
    assert response.status_code == 200
    
    
# Testando o endpoint de listar pedido pelo ID

@pytest.mark.django_db

def test_list_order_by_id():
    client = APIClient()
    url = '/listarPedido/'

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
    response = client.get(f"{url}{order.id}")
    assert response.status_code == 200
    
    
# Testando o endpoint de listar pedido por id, mas utilizando o id errado

@pytest.mark.django_db

def test_list_order_by_id_wrong_id():
    client = APIClient()
    url = '/listarPedido/'

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
    response = client.get(f"{url}10")
    assert response.status_code == 404
    
    
# Testando o endpoint de listar pedidos de um usuario

@pytest.mark.django_db

def test_list_orders_by_user():
    client = APIClient()
    url = '/listarPedidosUsuario/'

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
    response = client.get(f"{url}{user.id}")
    assert response.status_code == 200
    
    
# Testando o endpoint de listar pedidos pelo usuario, mas o id errado

@pytest.mark.django_db

def test_list_orders_by_user_wrong_id():
    client = APIClient()
    url = '/listarPedidosUsuario/'

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
    response = client.get(f"{url}10")
    assert response.status_code == 404 
    
    
# Testando o endpoint de listar pedidos pelo status

@pytest.mark.django_db

def test_list_orders_by_status():
    client = APIClient()
    url = '/listarPedidosUsuarioStatus/'

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
    
    response = client.get(f"{url}?pedidos_status={PedidosStatusType.pendente.value}")
    assert response.status_code == 200

# Testando o endpoint de listar por data de pedido

@pytest.mark.django_db

def test_list_orders_by_date():
    
    client = APIClient()
    url = '/listarPedidosData/'

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
    
    response = client.get(f"{url}{order.data_pedido}")
    assert response.status_code == 200
 

# Testando o endpoint de atualizar pedido

@pytest.mark.django_db

def test_update_order():
    client = APIClient()
    url = '/atualizarPedido/'

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
    
    order_data = {
        'usuario_id': user.id,
        'data_pedido': '2021-10-10',
        'total': 100.0,
    }
    
    response = client.put(f"{url}{order.id}?pedido_status={PedidosStatusType.entregue.value}", order_data, format='json')
    assert response.status_code == 200
    
# Testando o endpoint de atualizar pedido com id errado

@pytest.mark.django_db

def test_update_order_wrong_id():
    client = APIClient()
    url = '/atualizarPedido/'

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
    
    order_data = {
        'usuario_id': user.id,
        'data_pedido': '2021-10-10',
        'total': 100.0,
    }
    
    response = client.put(f"{url}10?pedido_status={PedidosStatusType.entregue.value}", order_data, format='json')
    assert response.status_code == 404
    
    
# Testando o endpoint de deletar pedido

@pytest.mark.django_db

def test_delete_order():
    client = APIClient()
    url = '/deletarPedido/'

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
    
    response = client.delete(f"{url}{order.id}")
    assert response.status_code == 200
    
# Testando o endpoint de deletar pedido com id errado

@pytest.mark.django_db

def test_delete_order_wrong_id():
    client = APIClient()
    url = '/deletarPedido/'

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
    
    response = client.delete(f"{url}10")
    assert response.status_code == 404