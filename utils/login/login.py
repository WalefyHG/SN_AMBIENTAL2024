from ninja import Router
from usuario.models import Usuario
from rest_framework_simplejwt.tokens import AccessToken

from utils.login.schemas import LoginSchema

route = Router()

@route.post('login')
def obtain_token(request, user: LoginSchema):
    try:
        user1 = Usuario.objects.get(email=user.email)
        
        if user1.senha == user.senha:
            token = AccessToken.for_user(user)
            return {'token': str(token)}
        
    except Usuario.DoesNotExist:
        return 'Usuário não encontrado', 404