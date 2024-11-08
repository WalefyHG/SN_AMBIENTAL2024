from ninja import Router
from usuario.models import Usuario
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from utils.login.schemas import LoginSchema
from django.contrib.auth import get_user_model

route = Router()

# Função de login para obter token de usuario
@route.post('login')
def obtain_token(request, user: LoginSchema):
    try:
        # Usando o authenticate do django para verificar se o usuario existe a partir do email
        user1 = get_user_model().objects.get(email=user.email)
        
        # Checando se a senha do usuario é a mesma que a senha passada na requisição
        if user1.senha == user.senha:
            token = AccessToken.for_user(user1)
            # Token gerado
            return {'token': str(token)}
        else:
            # Senha incorreta
            raise AuthenticationFailed('Usuário ou senha inválidos')
        
    except Usuario.DoesNotExist:
        # Usuario não existe
        raise AuthenticationFailed('Usuário não existe')