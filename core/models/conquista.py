from django.db import models


class Conquista(models.Model):

    nome = models.CharField(
        max_length=100
    )

    descricao = models.TextField()

    pontos_recompensa = models.IntegerField(
        default=0
    )

    icone = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nome
