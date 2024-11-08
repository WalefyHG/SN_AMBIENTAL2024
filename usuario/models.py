from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


# Criação da classe Usuario para o banco de dados

class Usuario(AbstractUser):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=50)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.nome