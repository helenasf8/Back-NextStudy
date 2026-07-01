from django.conf import settings
from django.db import models

from .conquista import Conquista


class UsuarioConquista(models.Model):

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    conquista = models.ForeignKey(
        Conquista,
        on_delete=models.CASCADE
    )

    data_conquista = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.usuario} - {self.conquista}"
