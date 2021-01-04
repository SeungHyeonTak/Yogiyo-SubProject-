from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # api url
    path('', include('app.urls', namespace='app')),
    path('', include('account.urls', namespace='account')),
]
