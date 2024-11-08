from ninja import Schema
from datetime import date
from usuario.schemas import UsuarioSchemaOut
from .models import Pedido
from enum import Enum

class PedidosStatusType(str, Enum):
    pendente = "Pendente"
    em_preparo = "Em_preparo"
    a_caminho = "A_caminho"
    entregue = "Entregue"



class PedidoSchemaIn(Schema):
    usuario_id: int
    data_pedido: date
    total: float

class PedidoSchemaOut(Schema):
    id: int
    usuario_id: UsuarioSchemaOut
    data_pedido: date
    total: float
    status: str
    
