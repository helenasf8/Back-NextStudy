from rest_framework.serializers import ModelSerializer

from core.models import CronogramaItem


class CronogramaItemSerializer(ModelSerializer):

    class Meta:
        model = CronogramaItem
        fields = '__all__'
