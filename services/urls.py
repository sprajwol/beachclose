from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from services import views as services_views

urlpatterns = [
    path('', services_views.ServicesView.as_view(), name='services'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
