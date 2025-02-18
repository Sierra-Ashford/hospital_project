"""
URL configuration for hospital_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from hospital_app.views import dashboard
from django.shortcuts import redirect

def home_redirect(request):
    return redirect('dashboard')

urlpatterns = [
    path('admin/', admin.site.urls), #Admin panel
    path('', home_redirect, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('', include('hospital_app.urls')), #include('hospital_app.urls'): Connects the app's urls.py to the project
    path('accounts/', include('allauth.urls')), #Handles authentication via Django Allauth
    # re_path(r'^accounts/', include('allauth.urls')),

]

'''Without include(), Django wouldn’t know about the app’s URLs'''

#The '' (empty string) means this pattern applies to the base URL (http://127.0.0.1:8000/)
