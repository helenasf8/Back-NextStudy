from rest_framework import serializers

from core.models import MetaDiaria


class MetaDiariaSerializer(serializers.ModelSerializer):

    class Meta:
        model = MetaDiaria
        fields = '__all__'
        read_only_fields = (
            'data',
            'realizados',
            'acertos',
            'xp',
        )
