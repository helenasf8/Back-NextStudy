from rest_framework.viewsets import ModelViewSet

from core.models import CronogramaItem
from core.serializers import CronogramaItemSerializer


class CronogramaItemViewSet(ModelViewSet):
    queryset = CronogramaItem.objects.all()
    serializer_class = CronogramaItemSerializer
