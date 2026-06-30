from django.conf import settings
from django.db import models


class RespostaExercicio(models.Model):

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    exercicio = models.ForeignKey(
        "Exercicio",
        on_delete=models.CASCADE
    )

    alternativa_escolhida = models.ForeignKey(
        "Alternativa",
        on_delete=models.CASCADE
    )

    correta = models.BooleanField(
        default=False
    )

    pontos = models.IntegerField(
        default=0
    )

    data = models.DateTimeField(
        auto_now_add=True
    )

    def save(self, *args, **kwargs):

        self.correta = self.alternativa_escolhida.correta

        self.pontos = 10 if self.correta else 0

        super().save(*args, **kwargs)

        from core.models import MetaDiaria  # noqa: PLC0415

        meta, created = MetaDiaria.objects.get_or_create(
            usuario=self.usuario,
            data=self.data.date()
        )

        meta.realizados += 1

        if self.correta:
            meta.acertos += 1
            meta.xp += self.pontos

        meta.save()
