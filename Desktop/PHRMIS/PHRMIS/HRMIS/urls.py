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
    path('familybackground', views.familybackground),
    path('educationalbackground', views.educationalbackground),
    path('civilserviceeligibility', views.civilserviceeligibility),
    path('workexperience', views.workexperience),
    path('voluntarywork', views.voluntarywork),
    path('learninganddevelopment', views.learninganddevelopment, name='learningandevelopment'),
    path('otherinformation', views.otherinformation),
    path('register', views.register),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)