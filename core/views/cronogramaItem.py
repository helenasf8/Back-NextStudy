from rest_framework.viewsets import ModelViewSet

from core.models import CronogramaItem
from core.serializers import CronogramaItemSerializer


class CronogramaItemViewSet(ModelViewSet):

    serializer_class = CronogramaItemSerializer

    def get_queryset(self):
        return CronogramaItem.objects.filter(
            cronograma__usuario=self.request.user
        )
