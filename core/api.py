from ninja import NinjaAPI
from usuario.views import route as usuario_route

api = NinjaAPI()

api.add_router('', usuario_route)