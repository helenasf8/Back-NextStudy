from django.conf import settings
from django.db import models


class KanbanTarefa(models.Model):

    STATUS_CHOICES = [
        ("FAZER", "Para Fazer"),
        ("ANDAMENTO", "Em Andamento"),
        ("CONCLUIDO", "Concluído"),
    ]

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    titulo = models.CharField(
        max_length=200
    )

    descricao = models.TextField(
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="FAZER"
    )

    ordem = models.IntegerField(
        default=0
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    atualizado_em = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.titulo
