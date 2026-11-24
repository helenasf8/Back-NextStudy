from rest_framework import serializers

from core.models import QuestaoDiaria


class QuestaoDiariaSerializer(serializers.ModelSerializer):

    materia = serializers.CharField(
        source='materia.descricao'
    )

    pergunta = serializers.CharField(
        source='exercicio.pergunta'
    )

    tema = serializers.CharField(
        source='exercicio.tema'
    )

    alternativas = serializers.SerializerMethodField()

    class Meta:
        model = QuestaoDiaria

        fields = [
            'id',
            'materia',
            'tema',
            'pergunta',
            'alternativas',
            'respondida'
        ]

    def get_alternativas(self, obj):

        return [
            {
                'id': alternativa.id,
                'texto': alternativa.texto
            }
            for alternativa in obj.exercicio.alternativas.all()
        ]