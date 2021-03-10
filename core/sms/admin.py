from django.contrib import admin
from core.sms.models import *


@admin.register(AuthSms)
class AuthSmsAdmin(admin.ModelAdmin):
    search_fields: tuple = ('phone_number',)
    list_display: tuple = ('phone_number', 'auth_number', 'created_at',)
    list_display_links: tuple = ('phone_number',)
    list_filter: tuple = ('phone_number',)
