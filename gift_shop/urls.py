from django.apps import apps
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from gift_shop import settings

urlpatterns = [
  path('i18n/', include('django.conf.urls.i18n')),
  path('admin/', admin.site.urls),
  path('', include(apps.get_app_config('oscar').urls[0])),
  path('home/', include('home.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
