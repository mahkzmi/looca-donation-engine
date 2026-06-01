from django.shortcuts import render, get_object_or_404
from .models import Campaign

def campaign_detail(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id, is_active=True)
    
    # برای دیباگ: در ترمینال چاپ کن
    print("====")
    print("Method:", request.method)
    print("POST data:", request.POST)
    print("====")
    
    if request.method == 'POST':
        amount = request.POST.get('amount')
        donor_name = request.POST.get('donor_name', '')
        
        print("Amount:", amount)
        print("Donor:", donor_name)
        
        # حتی اگر amount نال بود، برو به pending
        return render(request, 'campaigns/pending.html', {
            'campaign': campaign,
            'test_message': 'این یک تست است'
        })
    
    return render(request, 'campaigns/detail.html', {
        'campaign': campaign
    })