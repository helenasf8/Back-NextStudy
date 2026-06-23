from rest_framework.viewsets import ModelViewSet  # type: ignore

from core.models import Alternativa
from core.serializers import AlternativaSerializer


class AlternativaViewSet(ModelViewSet):
    queryset = Alternativa.objects.all()

    serializer_class = AlternativaSerializer
