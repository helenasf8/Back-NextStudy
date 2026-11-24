from django.db import models

from .meta import MetaDiaria
from .exercicio import Exercicio
from .alternativa import Alternativa
from .materia import Materia


class QuestaoDiaria(models.Model):

    meta = models.ForeignKey(
        MetaDiaria,
        on_delete=models.CASCADE,
        related_name='questoes'
    )

    materia = models.ForeignKey(
        Materia,
        on_delete=models.CASCADE
    )

    exercicio = models.ForeignKey(
        Exercicio,
        on_delete=models.CASCADE
    )

    respondida = models.BooleanField(
        default=False
    )

    acertou = models.BooleanField(
        default=False
    )

    alternativa_escolhida = models.ForeignKey(
        Alternativa,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['meta', 'materia'],
                name='uma_questao_por_materia_diaria'
            )
        ]

    def __str__(self):
        return f'{self.meta} - {self.materia.descricao}'