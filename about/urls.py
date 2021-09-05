from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from about import views as about_views

urlpatterns = [
    path('', about_views.AboutView.as_view(), name='about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
