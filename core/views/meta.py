from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.models import MetaDiaria
from core.serializers import MetaDiariaSerializer


class MetaDiariaViewSet(viewsets.ModelViewSet):

    serializer_class = MetaDiariaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return MetaDiaria.objects.filter(
            usuario=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(
            usuario=self.request.user
        )
