from rest_framework import serializers


class EvolucaoSerializer(serializers.Serializer):

    dias = serializers.ListField()
