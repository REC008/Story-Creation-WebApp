# backend/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from story_creator.urls import urlpatterns  # Correct import

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(urlpatterns)),  # Use the imported urlpatterns directly
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
