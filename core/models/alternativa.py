from django.db import models  # type: ignore

from .exercicio import Exercicio


class Alternativa(models.Model):
    exercicio = models.ForeignKey(Exercicio, on_delete=models.CASCADE, related_name='alternativas')

    texto = models.CharField(max_length=255)

    correta = models.BooleanField(default=False)

    def __str__(self):
        return self.texto
