from django.core.management.base import BaseCommand
from usuario.models import Usuario
from pedido.models import Pedido
from itens_pedidos.models import ItensPedidos
from datetime import date
import random

# Criando comando para popular o banco de dados

class Command(BaseCommand):
    help = 'Popula o banco de dados com dados aleatórios'

    def handle(self, *args, **kwargs):
        for i in range(10):
            usuario , created = Usuario.objects.get_or_create(
                nome=f'Usuario {i}',
                defaults={
                    'email':f'usuario{i}@gmail.com',
                    'senha': '12345678'
                }
            )
            
            if created:
                self.stdout.write(self.style.SUCCESS(f'Usuário {usuario.nome} criado com sucesso'))
                
        # Criando os pedidos
        
        usuarios = Usuario.objects.all()
        
        for i, usuario, in enumerate(usuarios):
            pedido, created = Pedido.objects.get_or_create(
                usuario_id=usuario,
                data_pedido=date.today(),
                total=random.randint(10, 100),
                status=random.choice(['Pendente', 'Em_preparo', 'A_caminho', 'Entregue'])
            )
            
            if created:
                self.stdout.write(self.style.SUCCESS(f'Pedido {pedido.id} criado com sucesso'))

        # Criando os itens dos pedidos
        
        pedidos = Pedido.objects.all()
        
        for i, pedido in enumerate(pedidos):
            item, created = ItensPedidos.objects.get_or_create(
                pedido_id=pedido,
                nome=f'Item {i}',
                descricao=f'Descrição do item {i}',
                preco=random.randint(10, 100),
                categoria=random.choice(['Bebida', 'Sobremesa', 'Salada', 'Acompanhamento'])
            )
            
            if created:
                self.stdout.write(self.style.SUCCESS(f'Item {item.id} criado com sucesso'))
                
        self.stdout.write(self.style.SUCCESS('Dados populados com sucesso'))