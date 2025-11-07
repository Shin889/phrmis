from django.conf.urls.static import static
from django.urls import path
from PHRMIS import settings

from . import views

urlpatterns = [
    path('', views.showLogin),
    path('administrator', views.admin),
    path('adminhome', views.admin_dashboard),
    path('eLogin', views.showeLogin, name='showeLogin'),
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
    path('get_employees_by_office/', views.get_employees_by_office, name='get_employees_by_office'),
    path("get_employee_details/", views.get_employee_details, name="get_employee_details"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)