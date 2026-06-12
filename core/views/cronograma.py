from rest_framework.viewsets import ModelViewSet

from core.models import Cronograma
from core.serializers import CronogramaSerializer


class CronogramaViewSet(ModelViewSet):

    serializer_class = CronogramaSerializer

    def get_queryset(self):
        return Cronograma.objects.filter(
            usuario=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(
            usuario=self.request.user
        )