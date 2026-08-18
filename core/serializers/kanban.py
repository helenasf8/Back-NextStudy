from rest_framework import serializers

from core.models import KanbanTarefa


class KanbanTarefaSerializer(serializers.ModelSerializer):

    class Meta:
        model = KanbanTarefa
        fields = [
            'id',
            'usuario',
            'titulo',
            'descricao',
            'status',
            'ordem',
            'criado_em',
            'atualizado_em',
        ]

        read_only_fields = [
            'id',
            'usuario',
            'criado_em',
            'atualizado_em',
        ]
