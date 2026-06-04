from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Shelter
from campaigns.models import Campaign
from payments.models import Transaction

def shelter_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            try:
                shelter = Shelter.objects.get(user=user)
                login(request, user)
                return redirect('shelters:dashboard')
            except Shelter.DoesNotExist:
                messages.error(request, 'این کاربر به هیچ پناهگاهی متصل نیست')
        else:
            messages.error(request, 'نام کاربری یا رمز عبور اشتباه است')
    
    return render(request, 'shelters/login.html')

def shelter_logout(request):
    logout(request)
    return redirect('shelters:login')

@login_required
def dashboard(request):
    try:
        shelter = request.user.shelter
    except:
        messages.error(request, 'شما به پناهگاهی متصل نیستید')
        return redirect('shelters:login')
    
    campaigns = Campaign.objects.filter(shelter=shelter).order_by('-created_at')
    
    total_donations = 0
    total_amount = 0
    for campaign in campaigns:
        total_donations += campaign.transactions.filter(status='success').count()
        total_amount += campaign.collected_amount
    
    context = {
        'shelter': shelter,
        'campaigns': campaigns,
        'total_campaigns': campaigns.count(),
        'total_donations': total_donations,
        'total_amount': total_amount,
    }
    return render(request, 'shelters/dashboard.html', context)

@login_required
def campaign_transactions(request, campaign_id):
    try:
        shelter = request.user.shelter
    except:
        return redirect('shelters:login')
    
    campaign = get_object_or_404(Campaign, id=campaign_id, shelter=shelter)
    transactions = campaign.transactions.filter(status='success').order_by('-created_at')
    
    return render(request, 'shelters/transactions.html', {
        'campaign': campaign,
        'transactions': transactions,
    })