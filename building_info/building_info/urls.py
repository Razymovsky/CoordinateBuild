from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from buildings.views import OrganizationViewSet, EntranceViewSet

# Настройка маршрутов API
router = DefaultRouter()
router.register(r'organizations', OrganizationViewSet)
router.register(r'entrances', EntranceViewSet)

# Настройка Swagger
schema_view = get_schema_view(
   openapi.Info(
      title="Building Info API",
      default_version='v1',
      description="API для работы с организациями и входами",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@buildinginfo.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],  # Ограничить доступ для админа
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/', include(router.urls)),  # API маршруты
]