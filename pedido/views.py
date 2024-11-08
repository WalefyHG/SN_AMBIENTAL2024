from typing import List
from ninja import Router
from .models import Pedido
from .schemas import PedidoSchemaIn, PedidoSchemaOut
from usuario.models import Usuario
from django.shortcuts import get_object_or_404

route = Router()

# Rotas para os pedidos

@route.get('/listarPedidos' , response=List[PedidoSchemaOut])
def listar_pedidos(request):
    return Pedido.objects.all()

@route.post('/criarPedido', response={200: str})
def criar_pedido(request, pedido: PedidoSchemaIn):
    usuario = get_object_or_404(Usuario, id=pedido.usuario_id)
    pedido = Pedido.objects.create(
        usuario_id=usuario,
        data_pedido=pedido.data_pedido,
        total=pedido.total,
        status=pedido.status
    )
    pedido.save()
    return "Pedido criado com sucesso"

@route.get('/listarPedido/{id}', response=PedidoSchemaOut)
def listar_pedido(request, id: int):
    return Pedido.objects.get(id=id)

@route.put('/atualizarPedido/{id}', response=PedidoSchemaOut)
def atualizar_pedido(request, id: int, pedido: PedidoSchemaIn):
    Pedido.objects.filter(id=id).update(**pedido.dict())
    return Pedido.objects.get(id=id)

@route.delete('/deletarPedido/{id}', response={200: str})
def deletar_pedido(request, id: int):
    Pedido.objects.get(id=id).delete()
    return 'Pedido deletado com sucesso'

# Listar pedidos de um usuario
@route.get('/listarPedidosUsuario/{usuario_id}', response=List[PedidoSchemaOut])
def listar_pedidos_usuario(request, usuario_id: int):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    return list(Pedido.objects.filter(usuario_id=usuario))


# Listar pedidos pelo status
@route.get('/listarPedidosUsuarioStatus/{status}', response=List[PedidoSchemaOut])
def listar_pedidos_usuario_status(request, status: str):
    return list(Pedido.objects.filter(status=status))