from django.contrib import admin
from .models import Auto, ModelAuto, UserAuto, BrandAuto


@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ('model', 'vin_num', 'status', 'brand', 'auto_user')
    list_filter = ('status', 'brand')
    search_fields = ('vin_num', )


@admin.register(ModelAuto)
class ModelAutoAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo_brand_auto', 'count_auto')
    list_filter = ('logo_brand_auto', )
    ordering = ('name', )


@admin.register(UserAuto)
class UserAutoAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')
    search_fields = ('phone', )


@admin.register(BrandAuto)
class BrandAutoAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo')
    ordering = ('name', )
