from django.db import models

# Create your models here.


# Criação da classe Usuario para o banco de dados

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    senha = models.CharField(max_length=50)

    def __str__(self):
        return self.nome