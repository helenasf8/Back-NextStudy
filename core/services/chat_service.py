from django.conf import settings
from ollama import Client


def conversar_com_ia(mensagens):

    client = Client(
        host=settings.OLLAMA_URL,
        timeout=300.0
    )

    system_message = {
        'role': 'system',
        'content': (
            'Você é o assistente virtual do NexStudy, '
            'uma plataforma de estudos para estudantes. '
            'Responda sempre em português brasileiro. '
            'Ajude os estudantes com suas dúvidas, '
            'explique conteúdos de maneira didática '
            'e apresente exemplos quando necessário. '
            'Se não souber uma resposta, informe isso.'
        )
    }

    response = client.chat(
        model=settings.OLLAMA_MODEL,

        messages=[
            system_message,
            *mensagens
        ],

        options={
            'temperature': 0.5,
            'num_gpu': 0,
            'num_ctx': 4096,
            'num_predict': 512
        },

        keep_alive='10m'
    )

    resposta = response.message.content

    if not resposta:
        raise ValueError('A IA não retornou uma resposta.')

    return resposta