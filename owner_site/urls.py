from django.urls import path
from owner_site import views
from owner_site.owner.join import views as join
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.owner_index, name='owner'),
    path('owner/login/', views.owner_login, name='owner_login'),
    path('owner/signup/', views.owner_signup, name="owner_signup"),
    path('owner/join/process/', join.process, name="join_process"),
    path('owner/join/request/', join.online_entry, name='join_request'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('ajax/join/license_number/validate/', join.ajax_license_validate),
    path('ajax/join/phone_number_sms/authentication/', join.ajax_phone_sms_authentication),
    path('ajax/join/sms_code_validate/', join.ajax_sms_code_validate),
]
