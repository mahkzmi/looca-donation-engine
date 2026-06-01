from django.urls import path
from . import views

app_name = 'campaigns'

urlpatterns = [
    path('<int:campaign_id>/', views.campaign_detail, name='detail'),
]