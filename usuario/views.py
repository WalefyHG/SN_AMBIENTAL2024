from ninja import Router
from .schemas import UsuarioSchemaIn, UsuarioSchemaOut
from .models import Usuario
from ninja.pagination import paginate
from typing import List

# Serão criadas as funções e chamadas das rotas

route = Router()

# Listando todos os usuarios que foram cadastrados
@route.get('listarUsuario', response={200: List[UsuarioSchemaOut]})
@paginate
def get_usuarios(request):
    return Usuario.objects.all().values()

# Criando um usuario
@route.post('criandoUsuario', auth=None)
def create_usuario(request, user: UsuarioSchemaIn):
    # Criando um usuario a partir do schema de entrada
    usu = Usuario.objects.create(**user.dict())
    return UsuarioSchemaOut(**usu.__dict__)

# Listando usuario atraves do ID
@route.get('listarUsuario/{id}', response={200: UsuarioSchemaOut})
def get_usuario_by_id(request, id: int):
    return Usuario.objects.get(id=id)

# Atualizando usuario atraves do ID
@route.put('atualizarUsuario/{id}', response={200: str})
def update_usuario(request, id: int, user: UsuarioSchemaIn):
    # Atualizando o usuario a partir do ID e do schema de entrada
    usu = Usuario.objects.get(id=id)
    if user.nome:
        usu.nome = user.nome
    if user.email:
        usu.email = user.email
    if user.senha:
        usu.senha = user.senha
    usu.save()
    return 'Usuario atualizado com sucesso'

# Deletando usuario atraves do ID
@route.delete('deletarUsuario/{id}', response={200: str})
def delete_usuario(request, id: int):
    # Deletando o usuario a partir do ID
    Usuario.objects.get(id=id).delete()
    return 'Usuario deletado com sucesso'