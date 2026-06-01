from django.db import models
from campaigns.models import Campaign

class Transaction(models.Model):
    STATUS_CHOICES = [
        ('pending', 'در انتظار پرداخت'),
        ('success', 'پرداخت موفق'),
        ('failed', 'پرداخت ناموفق'),
    ]
    
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='transactions')
    amount = models.BigIntegerField(help_text="مبلغ به تومان")
    tracking_code = models.CharField(max_length=100, unique=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    donor_name = models.CharField(max_length=200, blank=True, help_text="اختیاری")
    payment_gateway_response = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.tracking_code} - {self.amount} تومان - {self.status}"