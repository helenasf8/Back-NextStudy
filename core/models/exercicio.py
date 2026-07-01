from django.db import models  # type: ignore

from .materia import Materia


class Exercicio(models.Model):
    DIFICULDADES = [
        ('facil', 'Fácil'),
        ('medio', 'Médio'),
        ('dificil', 'Difícil'),
    ]

    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='exercicios')

    tema = models.CharField(max_length=100)

    pergunta = models.TextField()

    dificuldade = models.CharField(max_length=50, choices=DIFICULDADES)

    gerado_ia = models.BooleanField(default=False)

    resolucao_passo_a_passo = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.materia.descricao} - {self.tema}'
