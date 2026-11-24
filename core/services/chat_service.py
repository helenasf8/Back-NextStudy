
from django.conf import settings
from groq import Groq


def conversar_com_ia(mensagens):

    client = Groq(
        api_key=settings.GROQ_API_KEY,
        timeout=60.0
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

    response = client.chat.completions.create(
        model=settings.GROQ_MODEL,

        messages=[
            system_message,
            *mensagens
        ],

        temperature=0.5,
        max_completion_tokens=2048
    )

    resposta = response.choices[0].message.content

    if not resposta:
        raise ValueError(
            'A IA não retornou uma resposta.'
        )

    return resposta
