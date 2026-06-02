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
     # فیلدهای جدید برای سیستم بدون واسطه (Direct Crypto)
    crypto_currency = models.CharField(max_length=10, blank=True, default='USDT', help_text="e.g., USDT, BTC, ETH")
    crypto_amount = models.FloatField(null=True, blank=True, help_text="Amount in crypto to send")
    receiver_address = models.CharField(max_length=200, blank=True, help_text="Your wallet address")
    tx_hash = models.CharField(max_length=200, blank=True, help_text="Transaction hash on blockchain")
    confirmed_at = models.DateTimeField(null=True, blank=True)
    
    def calculate_crypto_amount(self, toman_amount, currency='USDT'):
        """تبدیل تومان به ارز دیجیتال با نرخ تقریبی"""
        # در حالت واقعی، می‌توانی هر ۱ ساعت یکبار از یک API ساده نرخ بگیری
        # یا یک نرخ ثابت (مثلاً 1 USDT = 60,000 Toman) در نظر بگیری
        usd_rate = 180000  # 1 USDT = 180,000 Toman
        if currency == 'USDT':
            return round(toman_amount / usd_rate, 2)
        return 0
    

     # فیلدهای اهداکننده
    donor_name = models.CharField(max_length=200, blank=True, help_text="اختیاری")
    donor_email = models.CharField(max_length=200, blank=True, help_text="اختیاری - برای دریافت رسید")
    
    
    def __str__(self):
        return f"{self.tracking_code} - {self.amount} تومان - {self.status}"