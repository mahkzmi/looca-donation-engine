from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['tracking_code', 'campaign', 'amount', 'status', 'created_at']
    list_filter = ['status', 'campaign']
    search_fields = ['tracking_code', 'donor_name']
    readonly_fields = ['tracking_code', 'payment_gateway_response']