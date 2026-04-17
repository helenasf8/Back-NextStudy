from rest_framework.viewsets import ModelViewSet

from core.models import Materia
from core.serializers import MateriaSerializer


class MateriaViewSet(ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer
