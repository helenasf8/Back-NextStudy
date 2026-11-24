import logging

from django.db import transaction
from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from core.models import RespostaExercicio

from core.models import (
    User,
    CronogramaItem,
    Exercicio,
    Alternativa,
    MetaDiaria,
    QuestaoDiaria
)

from core.serializers.questaoDiaria import (
    QuestaoDiariaSerializer
)

from core.services.ollama_service import gerar_questao


logger = logging.getLogger(__name__)


class QuestaoDiariaView(APIView):

    permission_classes = [IsAuthenticated]

    def montar_resposta(self, meta):

        pendentes = meta.questoes.filter(
            respondida=False
        ).select_related(
            'materia', 'exercicio'
        ).prefetch_related(
            'exercicio__alternativas'
        )

        total = meta.questoes.count()
        realizadas = meta.questoes.filter(
            respondida=True
        ).count()

        serializer = QuestaoDiariaSerializer(
            pendentes,
            many=True
        )

        return {
            'total': total,
            'realizadas': realizadas,
            'concluidas': total > 0 and realizadas == total,
            'questoes': serializer.data
        }

    def get(self, request):

        hoje = timezone.localdate()

        meta = MetaDiaria.objects.filter(
            usuario=request.user,
            data=hoje
        ).first()

        if not meta:
            return Response({
                'total': 0,
                'realizadas': 0,
                'concluidas': False,
                'questoes': []
            })

        return Response(self.montar_resposta(meta))

    def post(self, request):

        hoje = timezone.localdate()

        itens = CronogramaItem.objects.filter(
            cronograma__usuario=request.user
        ).select_related('materia')

        materias = {}

        for item in itens:

            materia_id = item.materia_id

            if materia_id not in materias:
                materias[materia_id] = {
                    'materia': item.materia,
                    'topicos': []
                }

            topicos = materias[materia_id]['topicos']

            if item.topico not in topicos:
                topicos.append(item.topico)

        try:
            with transaction.atomic():

                User.objects.select_for_update().get(
                    pk=request.user.pk
                )

                meta, _ = MetaDiaria.objects.get_or_create(
                    usuario=request.user,
                    data=hoje,
                    defaults={'objetivo': 0}
                )

                # Evita gerar novas questões no mesmo dia.
                if meta.questoes.exists():
                    return Response(
                        self.montar_resposta(meta)
                    )

                for dados in materias.values():

                    materia = dados['materia']
                    topicos = ', '.join(dados['topicos'])

                    questao = gerar_questao(
                        materia.descricao,
                        topicos
                    )

                    exercicio = Exercicio.objects.create(
                        materia=materia,
                        tema=topicos[:100] or materia.descricao,
                        pergunta=questao['pergunta'],
                        dificuldade='medio',
                        gerado_ia=True,
                        resolucao_passo_a_passo=(
                            questao['explicacao']
                        )
                    )

                    for indice, texto in enumerate(
                        questao['alternativas']
                    ):

                        Alternativa.objects.create(
                            exercicio=exercicio,
                            texto=texto,
                            correta=indice == questao['correta']
                        )

                    QuestaoDiaria.objects.create(
                        meta=meta,
                        materia=materia,
                        exercicio=exercicio
                    )

                meta.objetivo = meta.questoes.count()
                meta.save(update_fields=['objetivo'])

                return Response(
                    self.montar_resposta(meta)
                )

        except Exception:

            logger.exception('Erro ao gerar metas diárias')

            return Response(
                {
                    'detail': (
                        'Não foi possível gerar as questões. '
                        'Tente novamente mais tarde.'
                    )
                },
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )
        
class ResponderQuestaoDiariaView(APIView):
    
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def post(self, request, pk):

        hoje = timezone.localdate()

        User.objects.select_for_update().get(
            pk=request.user.pk
        )

        questao = QuestaoDiaria.objects.select_for_update().filter(
            pk=pk,
            meta__usuario=request.user,
            meta__data=hoje
        ).first()

        if not questao:

            return Response(
                {'detail': 'Questão não encontrada.'},
                status=status.HTTP_404_NOT_FOUND
            )

        if questao.respondida:

            return Response(
                {'detail': 'Questão já respondida.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        alternativa_id = request.data.get('alternativa')

        if type(alternativa_id) is not int:

            return Response(
                {'detail': 'Selecione uma alternativa válida.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        alternativa = Alternativa.objects.filter(
            id=alternativa_id,
            exercicio=questao.exercicio
        ).first()

        if not alternativa:

            return Response(
                {'detail': 'Alternativa inválida.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        RespostaExercicio.objects.create(
            usuario=request.user,
            exercicio=questao.exercicio,
            alternativa_escolhida=alternativa
        )

        questao.respondida = True
        questao.acertou = alternativa.correta
        questao.alternativa_escolhida = alternativa

        questao.save()

        gabarito = questao.exercicio.alternativas.get(
            correta=True
        )

        concluidas = not questao.meta.questoes.filter(
            respondida=False
        ).exists()

        return Response({
            'correta': alternativa.correta,
            'resposta_correta': gabarito.texto,
            'explicacao': (
                questao.exercicio.resolucao_passo_a_passo
            ),
            'concluidas': concluidas
        })