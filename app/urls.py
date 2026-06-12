from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from django.conf import settings
from django.conf.urls.static import static

from uploader.router import router as uploader_router

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


from core.views import (
    UserRegistrationView,
    UserViewSet,
    CronogramaViewSet,
    CronogramaItemViewSet,
)

from core.views.materia import MateriaViewSet


router = DefaultRouter()


# Usuários
router.register(
    r'usuarios',
    UserViewSet,
    basename='usuarios'
)


# Matérias
router.register(
    r'materia',
    MateriaViewSet,
    basename='materia'
)


# Cronogramas
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



urlpatterns = [

    path(
        'admin/',
        admin.site.urls
    ),


    # Upload de imagens
    path(
        'api/media/',
        include(uploader_router.urls)
    ),


    # Documentação API
    path(
        'api/schema/',
        SpectacularAPIView.as_view(),
        name='schema',
    ),

    path(
        'api/doc/',
        SpectacularSwaggerView.as_view(
            url_name='schema'
        ),
        name='swagger-ui',
    ),

    path(
        'api/redoc/',
        SpectacularRedocView.as_view(
            url_name='schema'
        ),
        name='redoc',
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



    # Rotas da API
    path(
        'api/',
        include(router.urls)
    ),

]


urlpatterns += static(
    settings.MEDIA_ENDPOINT,
    document_root=settings.MEDIA_ROOT
)