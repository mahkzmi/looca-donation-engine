from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('campaigns/', include('campaigns.urls')),
    path('shelters/', include('shelters.urls')),

]
