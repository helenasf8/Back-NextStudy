from rest_framework import serializers

from core.models import Conquista


class ConquistaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Conquista
        fields = [
            "id",
            "nome",
            "descricao",
            "pontos_recompensa",
            "icone",
        ]
