from . models import *
from django.contrib.auth import authenticate, login, logout
from django.db import models
from django.db.models import Count
from django.shortcuts import redirect, render
from datetime import datetime
from django.db import IntegrityError
from django.contrib import messages
from .models import WorkExperience, PersonalInformation

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

def doLogin(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            return HttpResponse("Email : "+request.POST.get("email")+" Password : "+request.POST.get("password"))
        else:
            return HttpResponse("Invalid Login")

def getUserDetails(request):
    if request.user!=None:
        return HttpResponse("User : "+request.user.email+" User Type : "+str(request.user.usertype))
    else:
        return HttpResponse("Please Login First")

def personalinformation(request):
    if not request.user.is_authenticated:
        return redirect("/eLogin")
    error=""
    user=request.user
    employee=PersonalInformation.objects.get(user=user)
    if request.method=="POST":
        # Personal Information
        fn=request.POST['firstname']
        mn=request.POST['middlename']
        ln=request.POST['lastname']
        ne=request.POST['nameextension']
        en=request.POST['employeenumber']
        ea=request.POST['emailaddress']
        # password=request.POST['pwd', None]
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

        phb=request.POST['permhouseblockno']
        psn=request.POST['permstreetno']
        psv=request.POST['permsubdivisionvillage']
        pb=request.POST['permbarangay']
        pcm=request.POST['permcitymunicipality']
        ppr=request.POST['permprovince']
        pzc=request.POST['permzipcode']

        thb=request.POST['temphouseblockno']
        tsn=request.POST['tempstreetno']
        tsv=request.POST['tempsubdivisionvillage'] 
        tb=request.POST['tempbarangay']
        tcm=request.POST['tempcitymunicipality']
        tp=request.POST['tempprovince']
        tzc=request.POST['tempzipcode']

        emad=request.POST['emailaddress']
        tpn=request.POST['telephonenumber']
        mbn=request.POST['mobilephonenumber']

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
        employee.placeofbirth = pob
        employee.citizenship = cit
        employee.height = int(ht) if ht else None
        employee.weight = int(wt) if wt else None
        employee.bloodtype = bt
        employee.gsisno = gsis
        employee.pagibigno = pi
        employee.sssno = sss
        employee.tinno = tin
        employee.mobilephonenumber = mbn
        employee.telephonenumber = tpn

        employee.permhouseblockno = int(phb) if phb else None
        employee.permstreetno = psn
        employee.permsubdivisionvillage = psv
        employee.permbarangay = pb
        employee.permcitymunicipality = pcm
        employee.permprovince = ppr
        employee.permzipcode = int(pzc) if pzc else None

        employee.temphouseblockno = int(thb) if thb else None
        employee.tempstreetno = tsn
        employee.tempsubdivisionvillage = tsv
        employee.tempbarangay = tb
        employee.tempcitymunicipality = tcm
        employee.tempprovince = tp
        employee.tempzipcode = int(tzc) if tzc else None

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

        if dob:
            employee.dateofbirth = dob

        if 'profilepicture' in request.FILES:
            employee.profilepicture = request.FILES['profilepicture']

        try:
            employee.user.save()
            employee.save()
            error = "no"
        except Exception as e:
            print(e)
            error = "yes"

    return render(request, "personalinformation.html", locals())

def familybackground(request):
    if not request.user.is_authenticated:
        return redirect("/eLogin")
    error=""
    user=request.user

    employee, created = FamilyBackground.objects.get_or_create(user=user)    
    
    if request.method=="POST":
        try:
            ssn=request.POST['spousesurname']
            sfn=request.POST['spousefirstname']
            smn=request.POST['spousemiddlename']
            occ=request.POST['occupation']
            emp=request.POST['employer']
            ba=request.POST['businessaddress']
            tp=request.POST['telephone']
            nc=request.POST['nameofchildren']
            dob=request.POST['dateofbirth']
            fsn=request.POST['fathersurname']
            ffn=request.POST['fatherfirstname']
            fmn=request.POST['fathermiddlename']
            msn=request.POST['mothersurname']
            mfn=request.POST['motherfirstname']
            mmn=request.POST['mothermiddlename']

            employee.spousesurname = ssn
            employee.spousefirstname = sfn
            employee.spousemiddlename = smn
            employee.occupation = occ
            employee.employer = emp
            employee.businessaddress = ba
            employee.telephone = int(tp) if tp and tp.isdigit() else None
            employee.nameofchildren = nc
            employee.fathersurname = fsn
            employee.fatherfirstname = ffn
            employee.fathermiddlename = fmn
            employee.mothersurname = msn
            employee.motherfirstname = mfn
            employee.mothermiddlename = mmn

            if dob:
                try:
                    employee.dateofbirth = datetime.strptime(dob, "%Y-%m-%d").date()
                except ValueError:
                    employee.dateofbirth = None  
            else:
                employee.dateofbirth = None

            employee.save()
            error = "no"

        except Exception as e:
            print("Error saving Family Background:", e)
            error = "yes"

    return render(request, "familybackground.html", locals())

def educationalbackground(request):
    if not request.user.is_authenticated:
        return redirect("/eLogin")
    error=""
    user=request.user

    employee, created = EducationalBackground.objects.get_or_create(user=user)     
    
    if request.method=="POST":
        try:
            el=request.POST['educationlevel']
            sn=request.POST['schoolname']
            bedc=request.POST['basiceducationdegreecourse']   

            employee.educationlevel = el
            employee.schoolname = sn
            employee.basiceducationdegreecourse = bedc
        
            employee.save()
            error = "no"

        except Exception as e:
            print("Error saving Educational Background:", e)
            error = "yes"

    return render(request, "educationalbackground.html", locals())

def civilserviceeligibility(request):
    if not request.user.is_authenticated:
        return redirect("/eLogin")
    error=""
    user=request.user

    employee, created = CivilServiceEligibility.objects.get_or_create(user=user) 

    if request.method=="POST":
        try:
            en = request.POST.get('eligibilityname', '').strip()
            rtn = request.POST.get('rating', '').strip()
            doe = request.POST.get('dateofexamination', '').strip()
            poe = request.POST.get('placeofexamination', '').strip()
            ln = request.POST.get('licensenumber', '').strip()
            lv = request.POST.get('licensevalidity', '').strip()

            employee.eligibilityname = en
            employee.rating = rtn
            employee.placeofexamination = poe
            employee.licensenumber = ln

            if doe:
                try:
                    employee.dateofexamination = datetime.strptime(doe, "%Y-%m-%d").date()
                except ValueError:
                    employee.dateofexamination = None
            else:
                employee.dateofexamination = None

            if lv:
                try:
                    employee.licensevalidity = datetime.strptime(lv, "%Y-%m-%d").date()
                except ValueError:
                    employee.licensevalidity = None
            else:
                employee.licensevalidity = None

            employee.save()
            error = "no"

        except Exception as e:
            print("Error saving Civil Service Eligibility:", e)
            error = "yes"

    return render(request, "civilserviceeligibility.html", locals())

def workexperience(request):
    if not request.user.is_authenticated:
        return redirect("/eLogin")

    error = ""
    user = request.user

    try:
        employee = PersonalInformation.objects.get(user=user)
    except PersonalInformation.DoesNotExist:
        error = "personal_info_missing"
        return render(request, "workexperience.html", {"error": error})

    work_entry, created = WorkExperience.objects.get_or_create(employee=employee)

    if request.method == "POST":
        try:
            pt = request.POST['positiontitle']
            coa = request.POST['companyofficeagency']
            ms = request.POST['monthlysalary']
            sg = request.POST['salarygrade']
            aps = request.POST['appointmentstatus']
            gs = request.POST.get('governmentservice')
            fd = request.POST['fromdate']
            td = request.POST['todate']

            work_entry.positiontitle = pt
            work_entry.companyofficeagency = coa
            work_entry.monthlysalary = ms
            work_entry.salarygrade = sg
            work_entry.appointmentstatus = aps
            work_entry.governmentservice = True if gs else False

            if fd:
                try:
                    work_entry.fromdate = datetime.strptime(fd, "%Y-%m-%d").date()
                except ValueError:
                    work_entry.fromdate = None
            else:
                work_entry.fromdate = None

            if td:
                try:
                    work_entry.todate = datetime.strptime(td, "%Y-%m-%d").date()
                except ValueError:
                    work_entry.todate = None
            else:
                work_entry.todate = None

            work_entry.save()
            error = "no"

        except Exception as e:
            print("Error saving Work Experience:", e)
            error = "yes"

    work_info = WorkExperience.objects.filter(employee__user=request.user)
    return render(request, "workexperience.html", {
        "employee": employee,
        "work_entry": work_entry,
        "work_info": work_info,
        "error": error,
    })

def voluntarywork(request):
    if not request.user.is_authenticated:
        return redirect("/eLogin")
    error=""
    user=request.user

    employee, created = VoluntaryWork.objects.get_or_create(user=user)     
    
    if request.method=="POST":
        try:
            org=request.POST['organization']
            df=request.POST['datefrom']
            dt=request.POST['dateto']   
            noh=request.POST['numberofhours']   
            pn=request.POST['position']  

            employee.organization = org
            employee.datefrom = df
            employee.dateto = dt
            employee.numberofhours = noh
            employee.position = pn
        

            if df:
                try:
                    employee.datefrom = datetime.strptime(df, "%Y-%m-%d").date()
                except ValueError:
                    employee.datefrom = None
            else:
                employee.datefrom = None

            if dt:
                try:
                    employee.dateto = datetime.strptime(dt, "%Y-%m-%d").date()
                except ValueError:
                    employee.dateto= None
            else:
                employee.dateto = None
            employee.save()
            error = "no"

        except Exception as e:
            print("Error saving Voluntary Work:", e)
            error = "yes"

    return render(request, "voluntarywork.html", locals())


def learninganddevelopment(request):
    if not request.user.is_authenticated:
        return redirect("/eLogin")
    error=""
    user=request.user

    employee, created = LearningandDevelopment.objects.get_or_create(user=user)     
    
    if request.method=="POST":
        try:
            tol=request.POST['titleoflearning']
            dfm=request.POST['datefrom']
            dto=request.POST['dateto']   
            nohs=request.POST['numberofhours']   
            toi=request.POST['typeofid']  
            cd=request.POST['conducted']  
          
            employee.titleoflearning = tol
            employee.datefrom = dfm
            employee.dateto = dto
            employee.typeofid = toi
            employee.conducted = cd

            if nohs.strip():  
                try:
                    employee.numberofhours = int(nohs)
                except ValueError:
                    employee.numberofhours = None
            else:
                employee.numberofhours = None

            if dfm:
                try:
                    employee.datefrom = datetime.strptime(dfm, "%Y-%m-%d").date()
                except ValueError:
                    employee.datefrom = None
            else:
                employee.datefrom = None

            if dto:
                try:
                    employee.dateto = datetime.strptime(dto, "%Y-%m-%d").date()
                except ValueError:
                    employee.dateto= None
            else:
                employee.dateto = None
            employee.save()
            error = "no"

        except Exception as e:
            print("Error saving Learning and Development:", e)
            error = "yes"

    return render(request, "learninganddevelopment.html", locals())

def otherinformation(request):
    if not request.user.is_authenticated:
        return redirect("/eLogin")
    error=""
    user=request.user

    employee, created = OtherInformation.objects.get_or_create(user=user)     
    
    if request.method=="POST":
        try:
            sh=request.POST.get['skillshobbies']
            rec=request.POST.get['recognition']
            org=request.POST.get['organizations']
            ra3=request.POST.get['relatedaffinityb3rddegree']
            ra4=request.POST.get['relatedaffinityb4thdegree']
            rad=request.POST.get['relatedaffinitydetails']
            ao=request.POST.get['administrativeoffense']
            aod=request.POST.get['administrativeoffensedetails']
            ccc=request.POST.get['criminallychargedbeforecourt']
            ccd=request.POST.get['criminallychargeddetails']
            cdf=request.POST.get['criminallychargeddatefiled']
            ccs=request.POST.get['criminallychargedstatuscase']
            cov=request.POST.get['crimeorviolation']
            cd=request.POST.get['crimedetails']
            sfs=request.POST.get['separatedfromservice']
            ssd=request.POST.get['separatedfromservicedetails']
            lel=request.POST.get['localelectionlastyear']
            led=request.POST.get['localelectiondetails']
            rc3=request.POST.get['resignedtocampaignlast3months']
            rcd=request.POST.get['resignedtocampaigndetails']
            ais=request.POST.get['acquiredimmigrantstatus']
            isc=request.POS.getT['immigrantstatuscountry']
            ig=request.POST.get['indigenousgroup']
            ign=request.POST.get['indigenousgroupidno']
            pwd=request.POST.get['personwithdisability']
            pdn=request.POST.get['personwithdisabilityidno']
            sp=request.POST.get['soloparent']
            spn=request.POST.get['soloparentidno']
            r1n=request.POST.get['ref1name']
            r1a=request.POST.get['ref1address']
            r1t=request.POST.get['ref1telno']
            r2n=request.POST.get['ref2name']
            r2a=request.POST.get['ref2address']
            r2t=request.POST.get['ref2telno']
            r3n=request.POST.get['ref3name']
            r3a=request.POST.get['ref3address']
            r3t=request.POST.get['ref3telno']
            gid=request.POST.get['goviddescription']
            gin=request.POST.get['govidnumber']
            gdp=request.POST.get['goviddateplaceissued']

            employee.skillshobbies = sh
            employee.recognition = rec
            employee.organizations = org
            employee.relatedaffinityb3rddegree = ra3
            employee.relatedaffinityb4thdegree = ra4
            employee.relatedaffinitydetails = rad
            employee.administrativeoffense = ao
            employee.administrativeoffensedetails = aod
            employee.criminallychargedbeforecourt = ccc
            employee.criminallychargeddetails = ccd
            employee.criminallychargedstatuscase = ccs
            employee.crimeorviolation = cov
            employee.crimedetails = cd
            employee.separatedfromservice = sfs
            employee.separatedfromservicedetails = ssd
            employee.localelectionlastyear = lel
            employee.localelectiondetails = led
            employee.resignedtocampaignlast3months = rc3
            employee.resignedtocampaigndetails = rcd
            employee.acquiredimmigrantstatus = ais
            employee.immigrantstatuscountry = isc
            employee.indigenousgroup = ig
            employee.indigenousgroupidno = ign
            employee.personwithdisability = pwd
            employee.personwithdisabilityidno = pdn
            employee.soloparent = sp
            employee.soloparentidno = spn
            employee.ref1name = r1n
            employee.ref1address = r1a
            employee.ref1telno = r1t
            employee.ref2name = r2n
            employee.ref2address = r2a
            employee.ref2telno = r2t
            employee.ref3name = r3n
            employee.ref3address = r3a
            employee.ref3telno = r3t
            employee.goviddescription = gid
            employee.govidnumber = gin
            employee.goviddateplaceissued = gdp

            if cdf.strip():
                try:
                    employee.criminallychargeddatefiled = datetime.strptime(cdf, "%Y-%m-%d").date()
                except ValueError:
                    employee.criminallychargeddatefiled = None
            else:
                employee.criminallychargeddatefiled = None

            employee.save()
            error = "no"

        except Exception as e:
            print("Error saving Other Information:", e)
            error = "yes"

    return render(request, "otherinformation.html", locals())
    
def admin_dashboard(request):
    if not request.user.is_authenticated:
        return redirect("/administrator")

    employee = PersonalInformation.objects.select_related('user').all()

    work_info = WorkExperience.objects.select_related('employee', 'employee__user').all()

    positiontitle = (
        WorkExperience.objects
        .values('positiontitle')
        .order_by('positiontitle')
        .annotate(the_count=Count('positiontitle'))
    )

    office_counts = (
        WorkExperience.objects
        .values('companyofficeagency')
        .order_by('companyofficeagency')
        .annotate(the_count=Count('companyofficeagency'))
    )

    return render(request, "admin_dashboard.html", {
        'employee': employee,
        'work_info': work_info,
        'positiontitle': positiontitle,
        'office_counts': office_counts,
    })

def home(request):
    if not request.user.is_authenticated:
        return redirect("/eLogin")

    employee = PersonalInformation.objects.get(user=request.user)
    return render(request, "dashboard.html", {'employee': employee})

def logoutUser(request):
    logout(request)
    return redirect("/")

def register(request):
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        en = request.POST['employeenumber']
        ea = request.POST['emailaddress']
        password = request.POST['pwd']

        if PersonalInformation.objects.filter(employeenumber=en).exists():
            messages.error(request, "Employee number already exists.")
        else:
            try:
                user = User.objects.create_user(first_name=fn, last_name=ln, username=ea, password=password)
                PersonalInformation.objects.create(user=user, employeenumber=en)
                messages.success(request, "Registration successful.")
                return redirect('showeLogin')  
            except IntegrityError:
                messages.error(request, "An unexpected error occurred.")

    return render(request, "register.html")

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