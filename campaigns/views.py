from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Campaign
from payments.models import Transaction
import uuid
import qrcode
from io import BytesIO
import base64


def campaign_detail(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id, is_active=True)
    
    if request.method == 'POST':
        amount = request.POST.get('amount')
        donor_name = request.POST.get('donor_name', '')
        donor_email = request.POST.get('donor_email', '')
        
        # اعتبارسنجی مبلغ
        try:
            amount = int(amount)
            if amount < 1000:
                messages.error(request, 'حداقل مبلغ ۱,۰۰۰ تومان است')
                return render(request, 'campaigns/detail.html', {'campaign': campaign})
        except:
            messages.error(request, 'مبلغ نامعتبر است')
            return render(request, 'campaigns/detail.html', {'campaign': campaign})
        
        # ساخت کد رهگیری
        tracking_code = str(uuid.uuid4())[:8].upper()
        
        # ساخت تراکنش
        transaction = Transaction.objects.create(
            campaign=campaign,
            amount=amount,
            tracking_code=tracking_code,
            donor_name=donor_name,
            donor_email=donor_email,
            status='pending'
        )
        
        # نمایش صفحه پیگیری
        return render(request, 'campaigns/pending.html', {
            'transaction': transaction,
            'campaign': campaign
        })
    
    return render(request, 'campaigns/detail.html', {
        'campaign': campaign
    })


def crypto_checkout(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id, is_active=True)
    
    if request.method == 'POST':
        amount_toman = request.POST.get('amount')
        donor_name = request.POST.get('donor_name', '')
        donor_email = request.POST.get('donor_email', '')
        selected_currency = request.POST.get('currency', 'USDT')
        
        # اعتبارسنجی مبلغ
        try:
            amount = int(amount_toman)
            if amount < 10000:
                messages.error(request, 'حداقل مبلغ ۱۰,۰۰۰ تومان است')
                return redirect('campaigns:detail', campaign_id=campaign.id)
        except:
            messages.error(request, 'مبلغ نامعتبر است')
            return redirect('campaigns:detail', campaign_id=campaign.id)
        
        # آدرس کیف پول‌های واقعی - اینها رو با آدرس واقعی خودت جایگزین کن
        MY_WALLET_ADDRESSES = {
            'USDT': '0x742d35Cc6634C0532925a3b844Bc9e7595f0b4b8',  # آدرس تستی - عوض کن
            'BTC': 'bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh',   # آدرس تستی - عوض کن
            'ETH': '0x742d35Cc6634C0532925a3b844Bc9e7595f0b4b8',   # آدرس تستی - عوض کن
        }
        
        # نرخ‌های تقریبی ارزها (تومان به دلار و سپس به ارز دیجیتال)
        # در حالت واقعی می‌تونی از API نرخ لحظه‌ای استفاده کنی
        CRYPTO_RATES = {
            'USDT': 60000,      # 1 USDT = 60,000 Toman
            'BTC': 3500000000,  # 1 BTC = 3.5 Billion Toman
            'ETH': 180000000,   # 1 ETH = 180 Million Toman
        }
        
        # محاسبه مبلغ ارز دیجیتال
        rate = CRYPTO_RATES.get(selected_currency, 60000)
        crypto_amount = round(amount / rate, 8)
        
        # ساخت کد رهگیری یکتا
        tracking_code = str(uuid.uuid4())[:8].upper()
        
        # ساخت تراکنش
        transaction = Transaction.objects.create(
            campaign=campaign,
            amount=amount,
            tracking_code=tracking_code,
            donor_name=donor_name,
            donor_email=donor_email,
            status='pending',
            crypto_currency=selected_currency,
            crypto_amount=crypto_amount,
            receiver_address=MY_WALLET_ADDRESSES.get(selected_currency, '')
        )
        
        # ساخت QR Code از آدرس کیف پول
        payment_data = f"{transaction.receiver_address}"
        qr = qrcode.QRCode(box_size=5, border=2)
        qr.add_data(payment_data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        qr_base64 = base64.b64encode(buffer.getvalue()).decode()
        
        context = {
            'campaign': campaign,
            'transaction': transaction,
            'crypto_amount': crypto_amount,
            'crypto_currency': selected_currency,
            'receiver_address': transaction.receiver_address,
            'qr_code_base64': qr_base64,
        }
        return render(request, 'campaigns/crypto_payment.html', context)
    
    # درخواست GET - نمایش فرم
    return render(request, 'campaigns/crypto_form.html', {'campaign': campaign})


def verify_crypto(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    
    if request.method == 'POST':
        # در نسخه ساده: فرض می‌کنیم کاربر پرداخت کرده
        # در نسخه واقعی: اینجا باید از یک blockchain explorer API استفاده کنی
        
        transaction.status = 'success'
        transaction.save()
        
        # آپدیت مبلغ جمع‌آوری شده کمپین
        campaign = transaction.campaign
        campaign.collected_amount += transaction.amount
        campaign.save()
        
        messages.success(request, "پرداخت شما با موفقیت تأیید شد! از حمایت شما سپاسگزاریم.")
        return redirect('campaigns:detail', campaign_id=transaction.campaign.id)
    
    return redirect('campaigns:detail', campaign_id=transaction.campaign.id)