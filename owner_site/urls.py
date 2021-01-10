from django.urls import path
from owner_site.views import index

urlpatterns = [
    path('', index, name='index'),
]
