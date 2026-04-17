from rest_framework.serializers import ModelSerializer

from core.models import Materia


class MateriaSerializer(ModelSerializer):
    class Meta:
        model = Materia
        fields = '__all__'
