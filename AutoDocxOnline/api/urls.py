from django.urls import path, include
from django.conf.urls import url

from rest_framework.routers import DefaultRouter as Router
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from api.views import (
    DocumentViewSet,
    DocumentsPackageViewSet,
    upload,
)

v1_router = Router()
v1_router.register('documents', DocumentViewSet, basename='documents')
v1_router.register(
    'documents_package',
    DocumentsPackageViewSet,
    basename='documents_package',
)
v1_router.register(
    r'load/(?P<document_id>\d+)',
    upload,
    basename='upload'
)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]

schema_view = get_schema_view(
   openapi.Info(
      title="Docs API",
      default_version='v1',
      description="Документация для приложения documents",
      # terms_of_service="URL страницы с пользовательским соглашением",
      contact=openapi.Contact(email="admin@kittygram.ru"),
      license=openapi.License(name="BSD License"),
   ),

   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
   url(r'^swagger(?P<format>\.json|\.yaml)$', 
       schema_view.without_ui(cache_timeout=0), name='schema-json'),
   url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), 
       name='schema-swagger-ui'),
   url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), 
       name='schema-redoc'),
]
