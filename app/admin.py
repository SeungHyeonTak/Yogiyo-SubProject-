from django.contrib import admin
from app.models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at',)
    list_display_links = ('name',)
    list_filter = ('name',)


@admin.register(PaymentType)
class PaymentTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at',)
    list_display_links = ('name',)
    list_filter = ('name',)


@admin.register(ApplicationForm)
class ApplicationFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'business_name', 'license_number',)
    search_fields = ('business_name', 'license_number',)
    list_display_links = ('business_name',)
    list_filter = ('business_name',)


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'application_form', 'is_application_form', 'created_at',)
    list_display_links = ('is_application_form',)


@admin.register(BundleMenu)
class BundleMenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at',)
    list_display_links = ('name',)
    list_filter = ('name',)


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'created_at',)
    list_display_links = ('name',)
    list_filter = ('name',)


@admin.register(BundleOption)
class BundleOptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at',)
    list_display_links = ('name',)
    list_filter = ('name',)


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'created_at',)
    list_display_links = ('name',)
    list_filter = ('name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass
