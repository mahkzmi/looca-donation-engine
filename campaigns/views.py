from django.shortcuts import render, get_object_or_404
from .models import Campaign

def campaign_detail(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id, is_active=True)
    return render(request, 'campaigns/detail.html', {
        'campaign': campaign
    })