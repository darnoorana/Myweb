from django.contrib import admin
from .models import Ad

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'url')
    list_filter = ('is_active',)
    search_fields = ('title', 'url')
