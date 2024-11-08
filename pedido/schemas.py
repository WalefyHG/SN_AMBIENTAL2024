from ninja import Schema

class PedidoSchemaIn(Schema):
    nome: str
    descricao: str
    preco: float
    quantidade: int
    categoria: str

class PedidoSchemaOut(Schema):
    id: int
    nome: str
    descricao: str
    preco: float
    quantidade: int
    categoria: str

