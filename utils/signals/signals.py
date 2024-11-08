import uuid
from django.db.models.signals import pre_save
from django.dispatch import receiver
from usuario.models import Usuario


# Atribui um username único para o usuário, assim posso autenticar e criar varios usuarios
@receiver(pre_save, sender=Usuario)
def set_usuario_username(sender, instance, **kwargs):
    if not instance.username:
        instance.username = str(uuid.uuid4())
        