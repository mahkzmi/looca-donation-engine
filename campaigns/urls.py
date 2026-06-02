from django.urls import path
from . import views

app_name = 'campaigns'

urlpatterns = [
    path('<int:campaign_id>/', views.campaign_detail, name='detail'),
    path('crypto/<int:campaign_id>/', views.crypto_checkout, name='crypto_checkout'),
    path('verify/<int:transaction_id>/', views.verify_crypto, name='verify_crypto'),
]