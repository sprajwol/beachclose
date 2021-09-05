from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from contact import views as contact_views

urlpatterns = [
    path('', contact_views.ContactView.as_view(), name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
