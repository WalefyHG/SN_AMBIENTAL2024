from ninja import Schema
from pedido.schemas import PedidoSchemaOut
from enum import Enum


class ItensPedidosCategoriaType(str, Enum):
    bebida = "Bebida"
    sobremesa = "Sobremesa"
    salada = "Salada"
    acompanhamento = "Acompanhamento"

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
    
class ItensPedidosSchemaPut(Schema):
    nome: str = ''
    descricao: str = ''
    preco: float = None
    categoria: str = ''
    