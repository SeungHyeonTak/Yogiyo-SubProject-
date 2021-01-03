from django.contrib import admin
from account.models import User, Owner


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'nickname', 'is_active', 'is_withdrawal', 'is_superuser', 'created_at')
    list_display_links = ('email',)
    list_filter = ('nickname', )


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_register', 'is_cancel', )
    list_display_links = ('name', )
    list_filter = ('name', )
