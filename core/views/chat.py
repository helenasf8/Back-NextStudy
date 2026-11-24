import logging

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from core.services.chat_service import conversar_com_ia


logger = logging.getLogger(__name__)


class ChatView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        mensagens = request.data.get('mensagens', [])

        if not isinstance(mensagens, list) or not mensagens:
            return Response(
                {'detail': 'Envie uma mensagem.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        mensagens_validas = []

        for mensagem in mensagens[-10:]:

            if not isinstance(mensagem, dict):
                return Response(
                    {'detail': 'Mensagem inválida.'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            role = mensagem.get('role')
            content = mensagem.get('content')

            if (
                role not in ['user', 'assistant']
                or not isinstance(content, str)
                or not content.strip()
                or len(content) > 5000
            ):
                return Response(
                    {'detail': 'Mensagem inválida.'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            mensagens_validas.append({
                'role': role,
                'content': content.strip()
            })

        if mensagens_validas[-1]['role'] != 'user':
            return Response(
                {'detail': 'Envie uma pergunta.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:

            resposta = conversar_com_ia(
                mensagens_validas
            )

            return Response(
                {'resposta': resposta},
                status=status.HTTP_200_OK
            )

        except Exception:

            logger.exception('Erro no chat do NexStudy')

            return Response(
                {
                    'detail': (
                        'Não foi possível obter uma resposta da IA.'
                    )
                },
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )