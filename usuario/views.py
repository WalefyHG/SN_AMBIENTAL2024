from ninja import Router
from .schemas import UsuarioSchemaIn, UsuarioSchemaOut
from .models import Usuario

# Serão criadas as funções e chamadas das rotas

route = Router()

@route.get('listarUsuario')
def get_usuarios(request):
    return 'Lista de usuários'

@route.post('criandoUsuario', auth=None)
def create_usuario(request, user: UsuarioSchemaIn):
    usu = Usuario.objects.create(**user.dict())
    return UsuarioSchemaOut(**usu.__dict__)
    