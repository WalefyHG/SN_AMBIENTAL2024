from ninja import NinjaAPI
from usuario.views import route as usuario_route
from utils.login.login import route as login_route
from rest_framework_simplejwt.authentication import JWTAuthentication
from ninja.security import HttpBearer

class JWTBearer(HttpBearer):
    def authenticate(self, request, token):
        try:
            user = JWTAuthentication().authenticate(request)
        except Exception as e:
            return None
        if user is None:
            return None
        return user[0]

api = NinjaAPI()

api.add_router('', login_route)
api.add_router('', usuario_route)