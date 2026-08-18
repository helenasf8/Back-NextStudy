from rest_framework import serializers

from core.models import UsuarioConquista


class UsuarioConquistaSerializer(serializers.ModelSerializer):

    class Meta:
        model = UsuarioConquista
        fields = [
            "id",
            "usuario",
            "conquista",
            "data_conquista",
        ]

        read_only_fields = [
            "data_conquista",
        ]
