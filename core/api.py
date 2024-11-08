from ninja import NinjaAPI
from usuario.views import route as usuario_route
from pedido.views import route as pedido_route
from itens_pedidos.views import route as itens_pedido_route
from utils.login.login import route as login_route
from rest_framework_simplejwt.authentication import JWTAuthentication
from ninja.security import HttpBearer


# Bearer para fazer a verificação de tokens
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

# Adicionando as rotas na minha url
api.add_router('', login_route, tags=["Login"])
api.add_router('', usuario_route, auth=JWTBearer(), tags=["Usuarios"])
api.add_router('', pedido_route, auth=JWTBearer() ,tags=["Pedidos"])
api.add_router('', itens_pedido_route, auth=JWTBearer() ,tags=["Itens Pedidos"])