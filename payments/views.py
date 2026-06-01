from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Campaign
from payments.models import Transaction
import uuid

def campaign_detail(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id, is_active=True)
    
    if request.method == 'POST':
        amount = request.POST.get('amount')
        donor_name = request.POST.get('donor_name', '')
        
        if amount and int(amount) > 0:
            # ساخت کد رهگیری یکتا
            tracking_code = str(uuid.uuid4())[:8].upper()
            
            # ثبت تراکنش
            transaction = Transaction.objects.create(
                campaign=campaign,
                amount=int(amount),
                tracking_code=tracking_code,
                donor_name=donor_name,
                status='pending'
            )
            
            # فعلاً به صفحه پیغام می‌فرستیم (بعداً به درگاه وصل می‌شود)
            return render(request, 'campaigns/pending.html', {
                'transaction': transaction,
                'campaign': campaign
            })
    
    return render(request, 'campaigns/detail.html', {
        'campaign': campaign
    })