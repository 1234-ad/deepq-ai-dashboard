from django.contrib import admin
from .models import WorldBankData


@admin.register(WorldBankData)
class WorldBankDataAdmin(admin.ModelAdmin):
    list_display = ['country_name', 'indicator_name', 'year', 'value']
    list_filter = ['country_name', 'indicator_name', 'year']
    search_fields = ['country_name', 'indicator_name']
    ordering = ['-year', 'country_name']