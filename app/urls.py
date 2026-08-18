from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from core.views import (
    CronogramaItemViewSet,
    CronogramaViewSet,
    UserRegistrationView,
    UserViewSet,
)
from core.views.dashboard import DashboardView
from core.views.evolucao import EvolucaoView
from core.views.kanban import KanbanTarefaViewSet
from core.views.materia import MateriaViewSet
from core.views.meta import MetaDiariaViewSet
from core.views.resposta import RespostaExercicioViewSet
from uploader.router import router as uploader_router
from uploader.views import AlternativaViewSet, ExercicioViewSet

router = DefaultRouter()

# Usuários
router.register(
    r'usuarios',
    UserViewSet,
    basename='usuarios'
)

router.register(
    r'materia',
    MateriaViewSet,
    basename='materia'
)

router.register(
    r'exercicios',
    ExercicioViewSet,
    basename='exercicios'
)

router.register(
    r'alternativas',
    AlternativaViewSet,
    basename='alternativas'
)

router.register(
    r'respostas',
    RespostaExercicioViewSet,
    basename='respostas'
)

router.register(
    r'metas',
    MetaDiariaViewSet,
    basename='metas'
)

router.register(
    r'cronograma',
    CronogramaViewSet,
    basename='cronograma'
)


# Itens do cronograma
router.register(
    r'cronograma-item',
    CronogramaItemViewSet,
    basename='cronograma-item'
)

router.register(
    r'kanban',
    KanbanTarefaViewSet,
    basename='kanban'
)


urlpatterns = [

    path(
        'admin/',
        admin.site.urls
    ),


    path(
        'api/media/',
        include(uploader_router.urls)
    ),

    path(
        'api/schema/',
        SpectacularAPIView.as_view(),
        name='schema'
    ),


    path(
        'api/doc/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui'
    ),


    path(
        'api/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc'
    ),


    # JWT

    path(
        'api/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),


    path(
        'api/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),


    path(
        'api/token/verify/',
        TokenVerifyView.as_view(),
        name='token_verify'
    ),


    # Registro

    path(
        'api/registro/',
        UserRegistrationView.as_view(),
        name='user_registration'
    ),


    # Dashboard

    path(
        'api/dashboard/',
        DashboardView.as_view(),
        name='dashboard'
    ),


    # Evolução

    path(
        'api/evolucao/',
        EvolucaoView.as_view(),
        name='evolucao'
    ),


    # API principal

    path(
        'api/',
        include(router.urls)
    ),
]


urlpatterns += static(
    settings.MEDIA_ENDPOINT,
    document_root=settings.MEDIA_ROOT
)
