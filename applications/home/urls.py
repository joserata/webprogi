from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DefinicionesViewSet,
    DocumentosViewSet,
    NormatividadViewSet,
    EventosViewSet,
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configura el esquema de Swagger
schema_view = get_schema_view(
   openapi.Info(
      title="API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@api.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'definiciones', DefinicionesViewSet, basename='definiciones')
router.register(r'documentos', DocumentosViewSet, basename='documentos')
router.register(r'normatividad', NormatividadViewSet, basename='normatividad')
router.register(r'eventos', EventosViewSet, basename='eventos')

urlpatterns = [
    path('api/', include(router.urls)),
    # URL de Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-schema'),
]
