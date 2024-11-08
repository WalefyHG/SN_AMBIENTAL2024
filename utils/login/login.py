from ninja import Router
from usuario.models import Usuario
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from utils.login.schemas import LoginSchema

route = Router()

@route.post('login')
def obtain_token(request, user: LoginSchema):
    try:
        user1 = authenticate(email=user.email, password=user.senha)
        
        if user1 is not None:
            token = AccessToken.for_user(user1)
            return {'token': str(token)}
        else:
            raise AuthenticationFailed('Usuário ou senha inválidos')
        
    except Usuario.DoesNotExist:
        raise AuthenticationFailed('Usuário não existe')