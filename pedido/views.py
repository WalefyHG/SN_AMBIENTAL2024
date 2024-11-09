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

# Listando todos os pedidos existentes
@route.get('/listarPedidos' , response=List[PedidoSchemaOut])
@paginate
def listar_pedidos(request):
    return Pedido.objects.all()

# Criando os Pedidos

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

# Listando os pedidos pelo id
@route.get('/listarPedido/{id}', response=PedidoSchemaOut)
@paginate
def listar_pedido(request, id: int):
    # Ele pega o id do pedido e verifica se ele existe, caso não exista, ele dá error 404
    pedido = get_object_or_404(Pedido, id=id)
    return pedido

# Atualizando o pedido pelo id
@route.put('/atualizarPedido/{id}', response=PedidoSchemaOut)
def atualizar_pedido(request, id: int, pedido: PedidosSchemaPut, pedido_status: PedidosStatusType):
    pedido_obj = get_object_or_404(Pedido, id=id)
    
    if pedido.data_pedido:
        pedido_obj.data_pedido = pedido.data_pedido
        
    if pedido.total:
        pedido_obj.total = pedido.total
        
    if pedido.status:
        pedido_obj.status = pedido_status.value
    
    pedido_obj.save()
    
    return pedido_obj

# Deletando o pedido pelo id
@route.delete('/deletarPedido/{id}', response={200: str})
def deletar_pedido(request, id: int):
    pedido = get_object_or_404(Pedido, id=id)
    pedido.delete()
    return 'Pedido deletado com sucesso'

# Listando pedidos de um usuario
@route.get('/listarPedidosUsuario/{usuario_id}', response=List[PedidoSchemaOut])
@paginate
def listar_pedidos_usuario(request, usuario_id: int):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    return list(Pedido.objects.filter(usuario_id=usuario))


# Listando pedidos pelo status
@route.get('/listarPedidosUsuarioStatus/', response=List[PedidoSchemaOut])
@paginate
def listar_pedidos_usuario_status(request, pedidos_status: PedidosStatusType):
    return list(Pedido.objects.filter(status=pedidos_status.value))

# Listando todos os pedidos através da data

@route.get('/listarPedidosData/{data_pedido}', response=List[PedidoSchemaOut])
@paginate
def listar_pedidos_data(request, data_pedido: date):
    return list(Pedido.objects.filter(data_pedido=data_pedido))