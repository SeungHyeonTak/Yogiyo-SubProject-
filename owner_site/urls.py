from django.urls import path
from owner_site.views import owner_index, owner_login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', owner_index, name='owner'),
    path('owner/login/', owner_login, name='owner_login'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
