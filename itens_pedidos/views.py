from ninja import Router

route = Router()

@route.get('listarItensPedido')
def get_itens_pedidos(request):
    return 'Lista de itens de pedidos'
