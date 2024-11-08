from typing import List
from ninja import Router
from itens_pedidos.models import ItensPedidos
from itens_pedidos.schemas import ItensPedidosSchemaIn, ItensPedidosSchemaOut, ItensPedidosCategoriaType
from pedido.models import Pedido

route = Router()

@route.get('listarItens' , response=List[ItensPedidosSchemaOut])
def listar_itens(request):
    return ItensPedidos.objects.all()

@route.post('criarItem', response={200: str})
def criar_item(request, item: ItensPedidosSchemaIn, itens_pedidos_status: ItensPedidosCategoriaType):
    pedido = Pedido.objects.get(id=item.pedido_id)
    item = ItensPedidos.objects.create(
        pedido_id=pedido,
        nome=item.nome,
        descricao=item.descricao,
        preco=item.preco,
        categoria= itens_pedidos_status.value
    )
    item.save()
    return "Item criado com sucesso"

@route.get('listarItem/{id}', response=ItensPedidosSchemaOut)
def listar_item(request, id: int):
    return ItensPedidos.objects.get(id=id)

@route.put('atualizarItem/{id}', response=ItensPedidosSchemaOut)
def atualizar_item(request, id: int, item: ItensPedidosSchemaIn):
    ItensPedidos.objects.filter(id=id).update(**item.dict())
    return ItensPedidos.objects.get(id=id)

@route.delete('deletarItem/{id}', response={200: str})
def deletar_item(request, id: int):
    ItensPedidos.objects.get(id=id).delete()
    return 'Item deletado com sucesso'

