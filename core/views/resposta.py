from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.models import RespostaExercicio
from core.serializers.resposta import RespostaExercicioSerializer


class RespostaExercicioViewSet(viewsets.ModelViewSet):
    queryset = RespostaExercicio.objects.all()
    serializer_class = RespostaExercicioSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
