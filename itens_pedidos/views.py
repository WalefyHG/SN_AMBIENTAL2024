from typing import List
from ninja import Router
from itens_pedidos.models import ItensPedidos
from itens_pedidos.schemas import ItensPedidosSchemaIn, ItensPedidosSchemaOut, ItensPedidosCategoriaType, ItensPedidosSchemaPut
from pedido.models import Pedido

route = Router()

# Listando todos os itens

@route.get('listarItens' , response=List[ItensPedidosSchemaOut])
def listar_itens(request):
    return ItensPedidos.objects.all()


# Criando um item
@route.post('criarItem')
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

# Listando item pelo id

@route.get('listarItem/{id}', response=ItensPedidosSchemaOut)
def listar_item(request, id: int):
    return ItensPedidos.objects.get(id=id)

# Atualizando Item pelo id

@route.put('atualizarItem/{id}', response=ItensPedidosSchemaOut)
def atualizar_item(request, id: int, item: ItensPedidosSchemaPut, item_status: ItensPedidosCategoriaType):
    item = ItensPedidos.objects.filter(id=id).update(**item.dict(), categoria=item_status.value)
    item.save()
    return item

# Deletando item pelo id

@route.delete('deletarItem/{id}', response={200: str})
def deletar_item(request, id: int):
    ItensPedidos.objects.get(id=id).delete()
    return 'Item deletado com sucesso'

