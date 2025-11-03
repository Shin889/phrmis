from django.conf.urls.static import static
from django.urls import path
from PHRMIS import settings

from . import views

urlpatterns = [
    path('', views.showLogin),
    path('administrator', views.admin),
    path('adminhome', views.admin_dashboard),
    path('eLogin', views.showeLogin),
    path('home', views.dashboard),
    path('logoutUser', views.logoutUser),
    path('personalinformation', views.personalinformation),
    path('register', views.register),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)