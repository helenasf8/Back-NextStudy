from django.db import models
from .cronograma import Cronograma
from .materia import Materia


class CronogramaItem(models.Model):
    DIAS_SEMANA = [
        ('SEG', 'Segunda'), ('TER', 'Terça'), ('QUA', 'Quarta'),
        ('QUI', 'Quinta'), ('SEX', 'Sexta'), ('SAB', 'Sábado'), ('DOM', 'Domingo'),
    ]

    STATUS_CHOICES = [
        ('PARA_FAZER', 'Para Fazer'),
        ('EM_ANDAMENTO', 'Em Andamento'),
        ('CONCLUIDO', 'Concluído'),
    ]

    cronograma = models.ForeignKey(Cronograma, on_delete=models.CASCADE, related_name='itens')
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    topico = models.CharField(max_length=150)
    dia_semana = models.CharField(max_length=3, choices=DIAS_SEMANA)
    horario = models.TimeField()
    duracao_minutos = models.PositiveIntegerField()
    concluido = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PARA_FAZER')
    ordem = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        # mantém "concluido" sempre sincronizado com o status,
        # assim a tela de Planilha continua funcionando sem mudanças
        self.concluido = self.status == 'CONCLUIDO'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.materia.descricao} - {self.dia_semana}'