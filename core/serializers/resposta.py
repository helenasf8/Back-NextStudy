from rest_framework import serializers

from core.models import RespostaExercicio


class RespostaExercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespostaExercicio
        fields = "__all__"
        read_only_fields = ["correta", "pontos"]
