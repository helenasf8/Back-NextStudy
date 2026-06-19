from rest_framework.serializers import ModelSerializer

from core.models import Cronograma


class CronogramaSerializer(ModelSerializer):

    class Meta:
        model = Cronograma
        fields = '__all__'
