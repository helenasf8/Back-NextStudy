from rest_framework.viewsets import ModelViewSet

from core.models import Cronograma
from core.serializers import CronogramaSerializer


class CronogramaViewSet(ModelViewSet):
    queryset = Cronograma.objects.all()
    serializer_class = CronogramaSerializer
