from ninja import Schema
from pedido.schemas import PedidoSchemaOut

class ItensPedidosSchemaIn(Schema):
    pedido_id: int
    nome: str
    descricao: str
    preco: float
    categoria: str
    
class ItensPedidosSchemaOut(Schema):
    id: int
    pedido_id: PedidoSchemaOut
    nome: str
    descricao: str
    preco: float
    categoria: str