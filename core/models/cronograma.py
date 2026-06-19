from django.db import models

from .user import User


class Cronograma(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='cronogramas'
    )

    nome = models.CharField(max_length=100)

    data_criacao = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.nome
