from typing import List
from ninja import Router
from itens_pedidos.models import ItensPedidos
from itens_pedidos.schemas import ItensPedidosSchemaIn, ItensPedidosSchemaOut, ItensPedidosCategoriaType, ItensPedidosSchemaPut
from pedido.models import Pedido
from django.shortcuts import get_object_or_404
from ninja.pagination import paginate

route = Router()

# Endpoint para listar todos os itens

@route.get('listarItens' , response=List[ItensPedidosSchemaOut])
@paginate
def listar_itens(request):
    # Retorna uma lista com todos os itens
    return ItensPedidos.objects.all()


# Endpoint para criar um item
@route.post('criarItem')
def criar_item(request, item: ItensPedidosSchemaIn, itens_pedidos_status: ItensPedidosCategoriaType):
    # Pega o pedido pelo id e caso não ache ele dá erro 404
    pedido = get_object_or_404(Pedido, id=item.pedido_id)
    
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

# Endpoint para listar um item pelo id

@route.get('listarItem/{id}', response=ItensPedidosSchemaOut)
@paginate
def listar_item(request, id: int):
    
    # Verifica se o item existe, caso não exista ele dá erro 404
    item = get_object_or_404(ItensPedidos, id=id)
    # Retorna o item
    return item

# Endpoint para atualizar o item pelo id

@route.put('atualizarItem/{id}', response=ItensPedidosSchemaOut)
def atualizar_item(request, id: int, item: ItensPedidosSchemaPut, item_status: ItensPedidosCategoriaType):
    # Verifica se o item existe, caso não exista ele dá erro 404
    item_obj = get_object_or_404(ItensPedidos, id=id)
    
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

# Endpoint para deletar o item pelo id

@route.delete('deletarItem/{id}', response={200: str})
def deletar_item(request, id: int):
    # Busca o item pelo id e deleta ele, caso não exista ele dá erro 404
    item = get_object_or_404(ItensPedidos, id=id)
    item.delete()
    # Retorna uma mensagem de sucesso
    return 'Item deletado com sucesso'

