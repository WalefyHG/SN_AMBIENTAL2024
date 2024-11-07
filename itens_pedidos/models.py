from django.db import models
from pedido.models import Pedido

# Create your models here.

class ItensPedidos(models.Model):
    
    CATEGORY_CHOICES = (
        ('1', 'Bebida'),
        ('2', 'Sobremesa'),
        ('3', 'Salada'),
        ('4', 'Acompanhamento')
    )
    
    
    id = models.AutoField(primary_key=True)
    pedido_id = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    nome = models.CharField(max_length=90)
    descricao = models.TextField(max_length=130)
    preco = models.DecimalField(max_digits=12, decimal_places=2)
    categoria = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.id