from django.db import models
from usuario.models import Usuario

# Create your models here.

class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_pedido = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=15)

    def __str__(self):
        return self.id