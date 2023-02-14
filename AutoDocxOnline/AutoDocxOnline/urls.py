from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/', include('djoser.urls')),  # Работа с пользователями.
    path('api/', include('djoser.urls.authtoken')),  # Работа с токенами.
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
