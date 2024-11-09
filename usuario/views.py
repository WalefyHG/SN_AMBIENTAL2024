from ninja import Router
from .schemas import UsuarioSchemaIn, UsuarioSchemaOut, UsuarioSchemaPut
from .models import Usuario
from ninja.pagination import paginate
from typing import List
from ninja.errors import HttpError
from django.shortcuts import get_object_or_404

# Serão criadas as funções e chamadas das rotas

route = Router()

# Endpoint para listar todos os usuarios que foram cadastrados
@route.get('listarUsuario', response={200: List[UsuarioSchemaOut]})
@paginate
def get_usuarios(request):
    
    # Listando todos os usuarios
    return Usuario.objects.all()
    

# Endpoint para criar um usuario
@route.post('criandoUsuario', auth=None, response={200: UsuarioSchemaOut})
def create_usuario(request, user: UsuarioSchemaIn):
    
    # Verifica se o usuario já existe, caso ele exista dá um erro 400
    if Usuario.objects.filter(email=user.email).exists():
        raise HttpError(400, "Usuario já existe")
    
    
    # Criando um usuario a partir do payload que foi inserido
    usu = Usuario.objects.create(
        nome=user.nome,
        email=user.email,
        senha=user.senha
    )
    return usu

# Endpoint para listar um usuario atravas do ID
@route.get('listarUsuario/{id}', response={200: UsuarioSchemaOut})
@paginate
def get_usuario_by_id(request, id: int):
    
    # Verifica se o usuario existe, caso não exista ele dá erro 404
    user = get_object_or_404(Usuario, id=id)
    
    return user


# Endpoint para atualizar um usuario atraves do ID
@route.put('atualizarUsuario/{id}', response={200: str})
def update_usuario(request, id: int, user: UsuarioSchemaPut):
    # Atualizando o usuario a partir do ID e do payload
    usu = get_object_or_404(Usuario, id=id)
    # Verifica se existe itens no payload e atualiza o usuario
    if user.nome:
        usu.nome = user.nome
    if user.email:
        usu.email = user.email
    if user.senha:
        usu.senha = user.senha
    usu.save()
    return 'Usuario atualizado com sucesso'

# Endpoint para deletar usuario atraves do ID
@route.delete('deletarUsuario/{id}', response={200: str})
def delete_usuario(request, id: int):
    # Deletando o usuario a partir do ID
    user = get_object_or_404(Usuario, id=id)
    user.delete()
    return 'Usuario deletado com sucesso'