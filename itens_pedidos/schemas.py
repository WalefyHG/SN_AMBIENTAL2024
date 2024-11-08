from ninja import Schema

class ItensPedidosSchemaIn(Schema):
    pedido_id: int
    item_id: int
    quantidade: int
    preco: float
    
class ItensPedidosSchemaOut(Schema):
    id: int
    pedido_id: int
    item_id: int
    quantidade: int
    preco: float