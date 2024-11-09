from typing import List
from ninja import Router
from .models import Pedido
from .schemas import PedidoSchemaIn, PedidoSchemaOut, PedidosStatusType, PedidosSchemaPut
from usuario.models import Usuario
from django.shortcuts import get_object_or_404
from datetime import date
from ninja.pagination import paginate

route = Router()

# Rotas para os pedidos

# Endpoint para listar todos os pedidos existentes
@route.get('/listarPedidos' , response=List[PedidoSchemaOut])
@paginate
def listar_pedidos(request):
    return Pedido.objects.all()

# Endpoint para criar os Pedidos

@route.post('/criarPedido', response=PedidoSchemaOut)
def criar_pedido(request, pedido: PedidoSchemaIn, pedidos_status: PedidosStatusType):
    # Ele pega o id do usuario e verifica se ele existe, caso não exista, ele dá error 404
    usuario = get_object_or_404(Usuario, id=pedido.usuario_id)
    # Cria o pedido com os dados passados
    pedido = Pedido.objects.create(
        usuario_id=usuario,
        data_pedido=pedido.data_pedido,
        total=pedido.total,
        status=pedidos_status.value
    )
    # Salva o pedido no banco de dados
    pedido.save()
    # Retorna uma mensagem de sucesso
    return pedido

# Endpoint para listar os pedidos pelo id
@route.get('/listarPedido/{id}', response=PedidoSchemaOut)
@paginate
def listar_pedido(request, id: int):
    # Ele pega o id do pedido e verifica se ele existe, caso não exista, ele dá error 404
    pedido = get_object_or_404(Pedido, id=id)
    return pedido

# Endpoint para atualizar o pedido pelo id
@route.put('/atualizarPedido/{id}', response=PedidoSchemaOut)
def atualizar_pedido(request, id: int, pedido: PedidosSchemaPut, pedido_status: PedidosStatusType):
    
    # Verifica se o pedido existe, caso não exista dá erro 404
    pedido_obj = get_object_or_404(Pedido, id=id)
    
    # Verifica se existe alterações no payload e atualiza o pedido
    if pedido.data_pedido:
        pedido_obj.data_pedido = pedido.data_pedido
        
    if pedido.total:
        pedido_obj.total = pedido.total
        
    if pedido.status:
        pedido_obj.status = pedido_status.value
        
    # Salva no banco de dados
    pedido_obj.save()
    
    # Retorna o objeto já atualizado
    return pedido_obj

# Endpoint para deletar o pedido pelo id
@route.delete('/deletarPedido/{id}', response={200: str})
def deletar_pedido(request, id: int):
    
    # Verifica se o pedido existe, caso não exista dá erro 404
    pedido = get_object_or_404(Pedido, id=id)
    # Deleta o pedido caso exista
    pedido.delete()
    # Retorna uma mensagem que foi bem sucessida
    return 'Pedido deletado com sucesso'

# Endpoint para listar todos os pedidos de um usuario
@route.get('/listarPedidosUsuario/{usuario_id}', response=List[PedidoSchemaOut])
@paginate
def listar_pedidos_usuario(request, usuario_id: int):
    # Verifica se o usuario existe, caso não exista dá erro 404
    usuario = get_object_or_404(Usuario, id=usuario_id)
    # Retorna uma lista de pedidos filtrados pelo id do usuario
    return list(Pedido.objects.filter(usuario_id=usuario))


# Endpoint para listar os pedidos pelo status
@route.get('/listarPedidosUsuarioStatus/', response=List[PedidoSchemaOut])
@paginate
def listar_pedidos_usuario_status(request, pedidos_status: PedidosStatusType):
    # Retorna uma lista de pedidos filtrados pelo status
    return list(Pedido.objects.filter(status=pedidos_status.value))

# Endpoint para listar todos os pedidos através da data

@route.get('/listarPedidosData/{data_pedido}', response=List[PedidoSchemaOut])
@paginate
def listar_pedidos_data(request, data_pedido: date):
    # Retorna uma lista de pedidos filtrados pela data
    return list(Pedido.objects.filter(data_pedido=data_pedido))