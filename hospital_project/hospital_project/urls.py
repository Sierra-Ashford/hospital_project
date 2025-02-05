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
from django.urls import path, include
from hospital_app.views import home

urlpatterns = [
    path('admin/', admin.site.urls), #Admin panel
    path('patients/', include('hospital_app.urls')), #include('hospital_app.urls'): Connects the app's urls.py to the project
    path('accounts/', include('allauth.urls')), #Django Allauth URLs
    path('', home, name='home'),
]
'''Without include(), Django wouldn’t know about the app’s URLs'''

#The '' (empty string) means this pattern applies to the base URL (http://127.0.0.1:8000/)
