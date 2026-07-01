from django.contrib.auth import get_user_model
from django.db.models.manager import BaseManager
from rest_framework import mixins, parsers, viewsets
from rest_framework.permissions import IsAuthenticated

from core.models import Alternativa, Exercicio, Materia
from core.serializers import (
    AlternativaSerializer,
    ExercicioSerializer,
    MateriaSerializer,
    UserSerializer,
)
from uploader.models import Document, Image
from uploader.serializers import DocumentUploadSerializer, ImageUploadSerializer


# =========================
# BASE UPLOAD VIEWSET
# =========================
class CreateViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    pass


class DocumentUploadViewSet(CreateViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentUploadSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]


class ImageUploadViewSet(CreateViewSet):
    queryset: BaseManager[Image] = Image.objects.all()
    serializer_class = ImageUploadSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]


# =========================
# CORE VIEWSETS
# =========================
class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer
    permission_classes = [IsAuthenticated]


class ExercicioViewSet(viewsets.ModelViewSet):
    queryset = Exercicio.objects.all()
    serializer_class = ExercicioSerializer
    permission_classes = [IsAuthenticated]


class AlternativaViewSet(viewsets.ModelViewSet):
    queryset = Alternativa.objects.all()
    serializer_class = AlternativaSerializer
    permission_classes = [IsAuthenticated]
