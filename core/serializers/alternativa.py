from rest_framework.serializers import ModelSerializer

from core.models import Alternativa


class AlternativaSerializer(ModelSerializer):
    class Meta:
        model = Alternativa
        fields = '__all__'
