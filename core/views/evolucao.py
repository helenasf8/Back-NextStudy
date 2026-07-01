from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import MetaDiaria
from core.serializers import EvolucaoSerializer


class EvolucaoView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        usuario = request.user

        metas = MetaDiaria.objects.filter(
            usuario=usuario
        ).order_by(
            "data"
        )

        dias = []

        for meta in metas:

            dias.append(
                {
                    "data": meta.data,
                    "resolvidos": meta.realizados,
                    "acertos": meta.acertos,
                    "xp": meta.xp,
                }
            )

        serializer = EvolucaoSerializer(
            {
                "dias": dias
            }
        )

        return Response(serializer.data)
