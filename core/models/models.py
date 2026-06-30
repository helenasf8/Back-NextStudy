from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class RespostaExercicio(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    exercicio = models.ForeignKey("Exercicio", on_delete=models.CASCADE)
    alternativa_escolhida = models.ForeignKey("Alternativa", on_delete=models.CASCADE)

    correta = models.BooleanField(default=False)
    pontos = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.correta = self.alternativa_escolhida.correta

        self.pontos = 10 if self.correta else 0

        super().save(*args, **kwargs)
