from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.models import Conquista, UsuarioConquista
from core.serializers import (
    ConquistaSerializer,
    UsuarioConquistaSerializer,
)


class ConquistaViewSet(viewsets.ModelViewSet):

    queryset = Conquista.objects.all()

    serializer_class = ConquistaSerializer

    permission_classes = [IsAuthenticated]


class UsuarioConquistaViewSet(viewsets.ModelViewSet):

    serializer_class = UsuarioConquistaSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return UsuarioConquista.objects.filter(
            usuario=self.request.user
        )

    def perform_create(self, serializer):

        serializer.save(
            usuario=self.request.user
        )
