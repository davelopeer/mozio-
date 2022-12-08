from django.contrib import admin
from django.urls import path, include,re_path
from rest_framework import permissions

urlpatterns = [
  path('admin/', admin.site.urls),
  path('api-auth/', include('rest_framework.urls')),
]


# Routers
from rest_framework import routers
from provider.api.viewsets import ProviderViewSet
from area.api.viewsets import ServiceAreaViewSet, FindPolygonsViewSet

router_v1 = routers.DefaultRouter()

router_v1.register(r'providers', ProviderViewSet)
router_v1.register(r'areas', ServiceAreaViewSet)
router_v1.register(r'find-polygons', FindPolygonsViewSet)

urlpatterns += [
  path('api/v1/', include(router_v1.urls))
]


# --------------------------
# Documentation with Swagger 
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="ServiceArea API",
      default_version='v1',
      description="A API for retrieving user poligon area from coordinates.",
      # terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="davidbarenco@gmail.com"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns += [
  re_path('docs(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
  re_path('docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
  re_path('redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]