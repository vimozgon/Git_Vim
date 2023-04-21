from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', include('board.urls')),
                  path('admin/', admin.site.urls),
                  path('accounts/', include('accounts.urls')),
                  path('accounts/', include('allauth.urls')),
                  path('pages/', include('django.contrib.flatpages.urls')),
                  path('ckeditor/', include('ckeditor_uploader.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
