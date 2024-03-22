from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from app_regisztracio.views import valaszto, regisztracio

urlpatterns = [
    path('', valaszto),
    path('regisztracio/', regisztracio),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
