from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.models import KanbanTarefa
from core.serializers import KanbanTarefaSerializer


class KanbanTarefaViewSet(viewsets.ModelViewSet):

    serializer_class = KanbanTarefaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return KanbanTarefa.objects.filter(
            usuario=self.request.user
        )

    def perform_create(self, serializer):

        serializer.save(
            usuario=self.request.user
        )
