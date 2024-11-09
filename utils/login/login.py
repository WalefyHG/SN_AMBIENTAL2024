from ninja import Router
from usuario.models import Usuario
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from utils.login.schemas import LoginSchema
from django.contrib.auth import get_user_model
from ninja.errors import HttpError

route = Router()

# Função de login para obter token de usuario
@route.post('login')
def obtain_token(request, user: LoginSchema):
    try:
        # Pegando o usuario pelo email
        user1 = Usuario.objects.get(email=user.email)
        
        # Checando se a senha do usuario é a mesma que a senha passada na requisição
        if user1.senha == user.senha:
            token = AccessToken.for_user(user1)
            # Token gerado
            return {'token': str(token)}
        else:
            # Caso a senha ou email esteja errada, dá error 404
            raise HttpError(404, 'Email ou senha inválidos')
        
    except Usuario.DoesNotExist:
        # Caso o usuario não exista dá error 406
        raise HttpError(406, 'Usuário não existe')