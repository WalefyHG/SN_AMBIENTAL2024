from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
# Create your models here.


# Criação da classe Usuario para o banco de dados

class Usuario(AbstractUser):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=50)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    # Conflitos que são resolvidos com a mudança do related_name
    groups = models.ManyToManyField(
        Group,
        related_name='usuario_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='usuario_seting', 
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.nome