from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema

from core.models import User
from core.serializers import (
    UserRegistrationSerializer,
    UserSerializer
)


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(
            id=self.request.user.id
        )

    @extend_schema(
        summary="Dados do usuário autenticado",
        description="Retorna ou atualiza os dados do usuário autenticado.",
        responses={200: UserSerializer, 401: None},
    )
    @action(
        detail=False,
        methods=['get', 'patch'],
        permission_classes=[IsAuthenticated]
    )
    def me(self, request):
        user = request.user

        if request.method == 'GET':
            serializer = self.get_serializer(user)

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        serializer = self.get_serializer(
            user,
            data=request.data,
            partial=True
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


class UserRegistrationView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]