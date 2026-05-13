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

from core.views import UserRegistrationView, UserViewSet
from core.views.materia import MateriaViewSet
from uploader.router import router as uploader_router  # Importação do uploader

router = DefaultRouter()

router.register(r'usuarios', UserViewSet, basename='usuarios')
router.register(r'materia', MateriaViewSet, basename='materia')

urlpatterns = [
    path('admin/', admin.site.urls),

    # OpenAPI 3
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/doc/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),

    # Autenticação JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # Registro de usuários
    path('api/registro/', UserRegistrationView.as_view(), name='user_registration'),

    # API Principal e Uploader
    path('api/', include(router.urls)),
    path('api/media/', include(uploader_router.urls)),  # Rota do uploader adicionada aqui
]

# Configuração para servir arquivos de mídia durante o desenvolvimento
urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
