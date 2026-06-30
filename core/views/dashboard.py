from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import (
    MetaDiaria,
    RespostaExercicio,
)
from core.serializers import DashboardSerializer


class DashboardView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        usuario = request.user

        respostas = RespostaExercicio.objects.filter(
            usuario=usuario
        )

        total = respostas.count()

        acertos = respostas.filter(
            correta=True
        ).count()

        taxa = 0

        if total > 0:
            taxa = int((acertos / total) * 100)

        meta = MetaDiaria.objects.filter(
            usuario=usuario,
            data=timezone.now().date()
        ).first()

        dados = {

            "usuario": usuario.username,

            "xp": meta.xp if meta else 0,


            "meta_diaria": {

                "objetivo": meta.objetivo if meta else 0,

                "realizados": meta.realizados if meta else 0,

                "acertos": meta.acertos if meta else 0,

            },


            "estatisticas": {

                "exercicios_resolvidos": total,

                "taxa_acerto": taxa,

            }

        }

        serializer = DashboardSerializer(dados)

        return Response(serializer.data)
