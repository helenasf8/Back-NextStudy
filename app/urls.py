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

import core.views
from core.views.materia import MateriaViewSet
from uploader.router import router as uploader_router

router = DefaultRouter()


router.register(
    r'usuarios',
    core.views.UserViewSet,
    basename='usuarios'
)

router.register(
    r'materia',
    MateriaViewSet,
    basename='materia'
)

router.register(
    r'exercicios',
    core.views.ExercicioViewSet,
    basename='exercicios'
)

router.register(
    r'alternativas',
    core.views.AlternativaViewSet,
    basename='alternativas'
)

router.register(
    r'respostas',
    core.views.RespostaExercicioViewSet,
    basename='respostas'
)

router.register(
    r'metas',
    core.views.MetaDiariaViewSet,
    basename='metas'
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
        core.views.UserRegistrationView.as_view(),
        name='user_registration'
    ),


    # Dashboard

    path(
        'api/dashboard/',
        core.views.DashboardView.as_view(),
        name='dashboard'
    ),


    # Evolução

    path(
        'api/evolucao/',
        core.views.EvolucaoView.as_view(),
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
