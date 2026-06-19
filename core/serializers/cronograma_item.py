from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from core.models import CronogramaItem


class CronogramaItemSerializer(ModelSerializer):

    materia_nome = serializers.CharField(
        source='materia.descricao',
        read_only=True
    )

    class Meta:
        model = CronogramaItem

        fields = [
            'id',
            'cronograma',
            'materia',
            'materia_nome',
            'topico',
            'dia_semana',
            'horario',
            'duracao_minutos',
            'concluido'
        ]