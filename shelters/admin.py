from django.contrib import admin
from .models import Shelter

@admin.register(Shelter)
class ShelterAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'is_verified', 'created_at']
    list_editable = ['is_verified']