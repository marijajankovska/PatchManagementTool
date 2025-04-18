"""
URL configuration for patch_tool project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django import views
from django.contrib import admin
from django.urls import path

# project_name/urls.py

from django.contrib import admin
from patch_tool_app import views
# Correctly import the view from the app


urlpatterns = [
    path('admin/', admin.site.urls),
    path('main_page/', views.main_page, name='main_page'),
    path('calendar/', views.patch_calendar, name='patch_calendar'),
]
