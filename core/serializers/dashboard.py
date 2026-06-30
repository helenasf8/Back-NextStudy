from rest_framework import serializers


class DashboardSerializer(serializers.Serializer):

    usuario = serializers.CharField()

    xp = serializers.IntegerField()

    meta_diaria = serializers.DictField()

    estatisticas = serializers.DictField()
