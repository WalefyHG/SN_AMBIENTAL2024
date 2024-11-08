from ninja import Router

route = Router()

@route.get('listarPedido')
def get_pedidos(request):
    return 'Lista de pedidos'
