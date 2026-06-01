from django.contrib import admin
from .models import Campaign

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ['title', 'shelter', 'target_amount', 'collected_amount', 'is_active', 'created_at']
    list_editable = ['is_active']
    list_filter = ['shelter', 'is_active']
    search_fields = ['title', 'shelter__name']