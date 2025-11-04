from . models import *
from django.contrib.auth import authenticate, login, logout
from django.db import models
from django.db.models import Count
from django.shortcuts import redirect, render

# Create your views here.

# def index(request):
#     return render(request, "login_v3.html")

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect("/eLogin")
    return render(request, "dashboard.html")

def admin(request):
    error=""
    if request.method=="POST":
        u=request.POST['un']
        p=request.POST['pword']
        user=authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    return render(request, "admin.html", locals())

def personalinformation(request):
    if not request.user.is_authenticated:
        return redirect("/eLogin")
    error=""
    user=request.user
    employee=PersonalInformation.objects.get(user=user)
    if request.method=="POST":
        # Pesonal Information
        fn=request.POST['firstname']
        mn=request.POST['middlename']
        ln=request.POST['lastname']
        ne=request.POST['nameextension']
        en=request.POST['employeenumber']
        ea=request.POST['emailaddress']
        password=request.POST['pwd']
        sx=request.POST['sex']
        cs=request.POST['civilstatus']
        dob=request.POST['dateofbirth']
        cit=request.POST['citizenship']
        pob=request.POST['placeofbirth']
        ht=request.POST['height']
        wt=request.POST['weight']
        bt=request.POST['bloodtype']
        gsis=request.POST['gsisno']
        pi=request.POST['pagibigno']
        sss=request.POST['sssno']
        tin=request.POST['tinno']

        # Permanent Residence
        phb=request.POST['permhouseblockno']
        psn=request.POST['permstreetno']
        psv=request.POST['permsubdivisionvillage']
        pb=request.POST['permbarangay']
        pcm=request.POST['permcitymunicipality']
        ppr=request.POST['permprovince']
        pzc=request.POST['permzipcode']

        # Temporary Residence
        thb=request.POST['temphouseblockno']
        tsn=request.POST['tempstreetno']
        tsv=request.POST['tempsubdivisionvillage'] 
        tb=request.POST['tempbarangay']
        tcm=request.POST['tempcitymunicipality']
        tp=request.POST['tempprovince']
        tzc=request.POST['tempzipcode']

        
        tpn=request.POST['telephonenumber']
        mbn=request.POST['mobilephonenumber']
        pp=request.FILES.get('profilepicture')

        # Address Details
        # st=request.POST['street']
        # brgy=request.POST['barangay']
        # mun=request.POST['municipality']

        # Contact Details
        # mobilen=request.POST['mobilenumber']
        # fm=request.POST['fbm']

        # Work Details
        # cd=request.POST['collegedepartment']
        # ar=request.POST['academicrank']
        # desig=request.POST['designation']
        # soa=request.POST['statusofappointment']
        # doa=request.POST['dofappointment']
        # mf=request.POST['membershipfee']

        # Personal Details
        employee.user.first_name = fn
        employee.middlename = mn
        employee.user.last_name = ln
        employee.nameextension = ne
        employee.employeenumber = en
        employee.user.username = ea
        employee.user.email = ea
        # employee.user.password = password
        employee.sex = sx
        employee.civilstatus = cs
        if dob:
            employee.dateofbirth = dob
        employee.placeofbirth = pob
        employee.citizenship = cit
        employee.height = ht
        employee.weight = wt
        employee.bloodtype = bt
        employee.gsisno = gsis
        employee.pagibigno = pi
        employee.sssno = sss
        employee.tinno = tin
        employee.telephonenumber = tpn
        employee.mobilephonenumber = mbn
        if pp:
            employee.profilepicture = pp
        employee.permhouseblockno = phb
        employee.permstreetno = psn
        employee.permsubdivisionvillage = psv
        employee.permbarangay = pb
        employee.permcitymunicipality = pcm
        employee.permprovince = ppr
        employee.permzipcode = pzc
        employee.temphouseblockno = thb
        employee.tempstreetno = tsn
        employee.tempsubdivisionvillage = tsv
        employee.tempzipcode = tzc
        employee.tempprovince = tp
        employee.tempcitymunicipality = tcm
        employee.tempbarangay = tb
        

        # Address Details
        # employee.streetaddress = st
        # employee.barangayaddress = brgy
        # employee.municipalityaddress = mun

        # Contact Details
        # employee.mobilenumber = mobilen
        # employee.fb = fm

        # Work Details
        # employee.collegedepartment = cd
        # employee.academicrank = ar
        # employee.designation = desig
        # employee.statusofappointment = soa
        # employee.dateofappointment = doa
        # if doa:
        #     employee.dateofappointment = doa
        # employee.membershipfee = mf
        try:
            employee.save()
            employee.user.save()
            user=User.objects.create_user(first_name=fn,last_name=ln,username=ea,password=password)
            PersonalInformation.objects.create(user=user,employeenumber=en,middlename=mn,nameextension=ne)
            error = "no"
        except:
            error = "yes"
    return render(request, "personalinformation.html", locals())

def admin_dashboard(request):
    if not request.user.is_authenticated:
        return redirect("/administrator")
    employee=PersonalInformation.objects.all()
    colleged=PersonalInformation.objects.values('collegedepartment').order_by('collegedepartment').annotate(the_count=Count('collegedepartment'))
    #print(colleged)
    return render(request, "admin_dashboard.html", locals())

def logoutUser(request):
    logout(request)
    return redirect("/")

def register(request):
    error=""
    if request.method=="POST":
        fn=request.POST['firstname']
        ln=request.POST['lastname']
        en=request.POST['employeenumber']
        ea=request.POST['emailaddress']
        password=request.POST['pwd']
        try:
            user=User.objects.create_user(first_name=fn,last_name=ln,username=ea,password=password)
            PersonalInformation.objects.create(user=user,employeenumber=en)
            error = "no"
        except:
            error = "yes"
    return render(request, "register.html", locals())

def showeLogin(request):
    error=""
    if request.method=="POST":
        u=request.POST['emailid']
        p=request.POST['password']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            error="no"
        else:
            error="yes"
    return render(request, "elogin.html", locals())

def showLogin(request): 
    error=""
    if request.method=="POST":
        u=request.POST['emailid']
        p=request.POST['password']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            error="no"
        else:
            error="yes"   
    return render(request, "login.html", locals())