from django.urls import path
from . import views

app_name = 'shelters'

urlpatterns = [
    path('login/', views.shelter_login, name='login'),
    path('logout/', views.shelter_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('campaign/<int:campaign_id>/transactions/', views.campaign_transactions, name='transactions'),
]