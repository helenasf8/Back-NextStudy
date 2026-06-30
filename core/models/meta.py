from django.conf import settings
from django.db import models


class MetaDiaria(models.Model):

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    data = models.DateField(
        auto_now_add=True
    )

    objetivo = models.IntegerField(
        default=10
    )

    realizados = models.IntegerField(
        default=0
    )

    acertos = models.IntegerField(
        default=0
    )

    xp = models.IntegerField(
        default=0
    )

    estudou = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f'{self.usuario} - {self.data}'
