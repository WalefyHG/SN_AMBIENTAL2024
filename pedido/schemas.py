from ninja import Schema
from datetime import date
from usuario.schemas import UsuarioSchemaOut

class PedidoSchemaIn(Schema):
    usuario_id: int
    data_pedido: date
    total: float
    status: str

class PedidoSchemaOut(Schema):
    id: int
    usuario_id: UsuarioSchemaOut
    data_pedido: date
    total: float
    status: str
    
