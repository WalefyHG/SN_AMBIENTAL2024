from ninja import Router

# Serão criadas as funções e chamadas das rotas

route = Router()

@route.get('listarUsuario')
def get_usuarios(request):
    return 'Lista de usuários'