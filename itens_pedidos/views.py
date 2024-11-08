from typing import List
from ninja import Router
from itens_pedidos.models import ItensPedidos
from itens_pedidos.schemas import ItensPedidosSchemaIn, ItensPedidosSchemaOut, ItensPedidosCategoriaType, ItensPedidosSchemaPut
from pedido.models import Pedido

route = Router()

# Listando todos os itens

@route.get('listarItens' , response=List[ItensPedidosSchemaOut])
def listar_itens(request):
    # Retorna uma lista com todos os itens
    return ItensPedidos.objects.all()


# Criando um item
@route.post('criarItem')
def criar_item(request, item: ItensPedidosSchemaIn, itens_pedidos_status: ItensPedidosCategoriaType):
    # Pega o pedido pelo id e caso não ache ele dá erro 404
    pedido = Pedido.objects.get_object_or_404(id=item.pedido_id)
    
    # Cria o item a partir dos dados selecionados
    item = ItensPedidos.objects.create(
        pedido_id=pedido,
        nome=item.nome,
        descricao=item.descricao,
        preco=item.preco,
        categoria= itens_pedidos_status.value
    )
    item.save()
    # Retorna uma mensagem de sucesso
    return "Item criado com sucesso"

# Listando item pelo id

@route.get('listarItem/{id}', response=ItensPedidosSchemaOut)
def listar_item(request, id: int):
    # Retorna o item pelo id
    return ItensPedidos.objects.get(id=id)

# Atualizando Item pelo id

@route.put('atualizarItem/{id}', response=ItensPedidosSchemaOut)
def atualizar_item(request, id: int, item: ItensPedidosSchemaPut, item_status: ItensPedidosCategoriaType):
    item_obj = ItensPedidos.objects.filter(id=id)
    
    # Verifica se existe itens no payload e atualiza o item
    if item.nome:
        item_obj.nome = item.nome
    if item.descricao:
        item_obj.descricao = item.descricao
    if item.preco:
        item_obj.preco = item.preco
    if item.categoria:
        item_obj.categoria = item_status.value
    # Salva o item no banco de dados
    item_obj.save()
    # Retorna o objeto atualizado
    return item_obj

# Deletando item pelo id

@route.delete('deletarItem/{id}', response={200: str})
def deletar_item(request, id: int):
    # Busca o item pelo id e deleta ele
    ItensPedidos.objects.get(id=id).delete()
    # Retorna uma mensagem de sucesso
    return 'Item deletado com sucesso'

