from datetime import date

from django.utils import timezone
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.models import MetaDiaria
from core.models.cronogramaItem import CronogramaItem
from core.serializers import MetaDiariaSerializer


class MetaDiariaViewSet(viewsets.ModelViewSet):
    serializer_class = MetaDiariaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        metasDiarias = MetaDiaria.objects.filter(usuario=self.request.user, data=date.today())
        if len(metasDiarias) == 0:
            siglas = ['SEG', 'TER', 'QUA', 'QUI', 'SEX', 'SAB', 'DOM']
            dia_num = timezone.now().date().weekday()
            sigla_hoje = siglas[dia_num]

            cronograma_de_hoje = CronogramaItem.objects.filter(
                cronograma__usuario=self.request.user, dia_semana=sigla_hoje
            )
            if len(cronograma_de_hoje) == 0:
                return []
            ## Você vai criar as metas diarias para esse dia.
            ## Ainda, vai pedir para o GPT (ou DeepSeek) gerar as questões com base nas suas atividades do dia 
            novaMeta = MetaDiaria()
            novaMeta.atividades = # ao que o GPT gerar
            breakpoint()

            return []
        if metasDiarias[0].atividades == {}:
            return []
        else:
            return metasDiarias

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
