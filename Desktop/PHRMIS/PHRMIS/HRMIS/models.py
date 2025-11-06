from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser, User

class NameField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(NameField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).title()

Blood_Type_Choices = (
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
)

Civil_Status_Choices=(
    ('MARRIED', 'Married'),
    ('WIDOWED', 'Widowed'),
    ('SEPARATED', 'Separated'),
    ('DIVORCED', 'Divorced'),
    ('SINGLE', 'Single'),    
)

Name_Extension_Choices=(
    ('JR', 'Jr'),
    ('SR','Sr'),
)

Level_Choices=(
    ('ELEMENTARY', 'Elementary'),
    ('SECONDARY', 'Secondary'),
    ('VOCATIONAL', 'Vocational/Trade Course'),
    ('COLLEGE', 'College'),
    ('GRADUATE', 'Graduate Studies'),
)

Sex_Choices=(
    ('MALE', 'Male'),
    ('FEMALE', 'Female'),
)

class PersonalInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nameextension = NameField(max_length=50, choices=Name_Extension_Choices)
    middlename = NameField(max_length=20)

    employeenumber = models.CharField(max_length=10, unique=True)
    
    dateofbirth = models.DateField(null=True)
    citizenship = models.CharField(max_length=30)
    placeofbirth = models.CharField(max_length=50)
    height = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    bloodtype = models.CharField(max_length=5, choices=Blood_Type_Choices) 
    gsisno = models.CharField(max_length=15)
    pagibigno = models.CharField(max_length=15)
    philhealthno = models.CharField(max_length=15)    
    sssno = models.CharField(max_length=15)
    tinno = models.CharField(max_length=15)

#   permanent residence address
    permhouseblockno = models.IntegerField(null=True, blank=True)
    permstreetno = models.CharField(max_length=100)
    permsubdivisionvillage = models.CharField(max_length=20)
    permbarangay = models.CharField(max_length=30)
    permcitymunicipality = models.CharField(max_length=30)
    permprovince = models.CharField(max_length=30)
    permzipcode = models.IntegerField(null=True, blank=True)

#   temporary residence address
    temphouseblockno = models.IntegerField(null=True, blank=True)
    tempstreetno = models.CharField(max_length=100)
    tempsubdivisionvillage = models.CharField(max_length=20)
    tempbarangay = models.CharField(max_length=30)
    tempcitymunicipality = models.CharField(max_length=30)
    tempprovince = models.CharField(max_length=30)
    tempzipcode = models.IntegerField(null=True, blank=True)

    # emailaddress = models.EmailField(max_length=50)
    telephonenumber = models.CharField(max_length=15)
    mobilenumber = models.CharField(max_length=11)
    sex = models.CharField(max_length=50, choices=Sex_Choices)
    civilstatus = models.CharField(max_length=50, choices=Civil_Status_Choices)
    profilepicture = models.ImageField(null=True, blank=True)
    objects=models.Manager()
    def __str__(self):
        return self.user.username
    
class FamilyBackground(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    spousesurname = models.CharField(max_length=50)
    spousefirstname = models.CharField(max_length=50)
    spousemiddlename = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)
    employer = models.CharField(max_length=50)
    businessaddress = models.CharField(max_length=100)
    telephone = models.IntegerField(null=True, blank=True)
    nameofchildren = models.CharField(max_length=50)
    dateofbirth = models.DateField(null=True)
    fathersurname = models.CharField(max_length=50)
    fatherfirstname = models.CharField(max_length=50) 
    fathermiddlename = models.CharField(max_length=50)
    mothersurname = models.CharField(max_length=50)
    motherfirstname = models.CharField(max_length=50)
    mothermiddlename = models.CharField(max_length=50)

class EducationalBackground(models.Model):   
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    educationlevel = models.CharField(max_length=20, choices=Level_Choices)
    schoolname = models.CharField(max_length=50)
    basiceducationdegreecourse = models.CharField(max_length=50)

class CivilServiceEligibility(models.Model):  
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    eligibilityname = models.CharField(max_length=50)
    rating = models.CharField(max_length=10)
    dateofexamination = models.DateField(null=True, blank=True)
    placeofexamination = models.CharField(max_length=50)
    licensenumber = models.CharField(max_length=10)
    licensevalidity = models.DateField(null=True, blank=True)

class WorkExperience(models.Model):
    employee = models.ForeignKey(PersonalInformation, on_delete=models.CASCADE, related_name='work_experiences')
    positiontitle = models.CharField(max_length=30)
    companyofficeagency = models.CharField(max_length=50)
    monthlysalary = models.CharField(max_length=10)
    salarygrade = models.CharField(max_length=10)
    appointmentstatus = models.CharField(max_length=20)
    governmentservice = models.BooleanField(default=False)
    fromdate = models.DateField(null=True, blank=True)
    todate = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.employee.employeenumber} - {self.positiontitle}"

class VoluntaryWork(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.CharField(max_length=100)  
    datefrom = models.DateField(null=True, blank=True)                 
    dateto = models.DateField(null=True, blank=True) 
    numberofhours = models.IntegerField(null=True, blank=True)  
    position = models.CharField(max_length=100) 

class LearningandDevelopment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    titleoflearning = models.CharField(max_length=100)  
    datefrom = models.DateField(null=True, blank=True)                 
    dateto = models.DateField(null=True, blank=True) 
    numberofhours = models.IntegerField(null=True, blank=True)  
    typeofid = models.CharField(max_length=100) 
    conducted = models.CharField(max_length=100) 

class OtherInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skillshobbies = models.CharField(max_length=100, blank=True, null=True)
    recognition = models.CharField(max_length=100, blank=True, null=True)
    organizations = models.CharField(max_length=100, blank=True, null=True)

    relatedaffinityb3rddegree = models.BooleanField(default=False)
    relatedaffinityb4thdegree = models.BooleanField(default=False)
    relatedaffinitydetails = models.CharField(max_length=50, blank=True, null=True)
    
    administrativeoffense = models.BooleanField(default=False)
    administrativeoffensedetails = models.TextField(blank=True, null=True)
    criminallychargedbeforecourt = models.BooleanField(default=False)
    criminallychargeddetails = models.TextField(blank=True, null=True)
    criminallychargeddatefiled = models.DateField(blank=True, null=True)
    criminallychargedstatuscase = models.CharField(max_length=50, blank=True, null=True)
    
    crimeorviolation = models.BooleanField(default=False)
    crimedetails = models.TextField(blank=True, null=True)
    
    separatedfromservice = models.BooleanField(default=False)
    separatedfromservicedetails = models.TextField(blank=True, null=True)
    
    localelectionlastyear = models.BooleanField(default=False)
    localelectiondetails = models.TextField(blank=True, null=True)
    resignedtocampaignlast3months = models.BooleanField(default=False)
    resignedtocampaigndetails = models.TextField(blank=True, null=True)
    
    acquiredimmigrantstatus = models.BooleanField(default=False)
    immigrantstatuscountry = models.CharField(max_length=100, blank=True, null=True)
    
    indigenousgroup = models.BooleanField(default=False)
    indigenousgroupidno = models.CharField(max_length=50, blank=True, null=True)
    personwithdisability = models.BooleanField(default=False)
    personwithdisabilityidno = models.CharField(max_length=20, blank=True, null=True)
    soloparent = models.BooleanField(default=False)
    soloparentidno = models.CharField(max_length=50, blank=True, null=True)

    ref1name = models.CharField(max_length=100, blank=True, null=True)
    ref1address = models.CharField(max_length=100, blank=True, null=True)
    ref1telno = models.CharField(max_length=50, blank=True, null=True)
    
    ref2name = models.CharField(max_length=100, blank=True, null=True)
    ref2address = models.CharField(max_length=100, blank=True, null=True)
    ref2telno = models.CharField(max_length=50, blank=True, null=True)
    
    ref3name = models.CharField(max_length=100, blank=True, null=True)
    ref3address = models.CharField(max_length=100, blank=True, null=True)
    ref3telno = models.CharField(max_length=50, blank=True, null=True)

    goviddescription = models.CharField(max_length=50, blank=True, null=True)
    govidnumber = models.CharField(max_length=20, blank=True, null=True)
    goviddateplaceissued = models.CharField(max_length=50, blank=True, null=True)
 

# class SpecialskillsHobbies(models.Model): 
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     skillshobbies = models.CharField(max_length=100)

# class NonAcademicDistinction(models.Model): 
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     recognition = models.CharField(max_length=100)

# class Membership(models.Model): 
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     organizations = models.CharField(max_length=100)

# class PersonalDataSheet(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     relatedaffinityb3rddegree = models.BooleanField(default=False)
#     relatedaffinityb4thdegree = models.BooleanField(default=False)
#     relatedaffinitydetails = models.CharField(max_length=50)
    
#     administrativeoffense = models.BooleanField(default=False)
#     administrativeoffensedetails = models.TextField()
#     criminallychargedbeforecourt = models.BooleanField(default=False)
#     criminallychargeddetails = models.TextField()
#     criminallychargeddatefiled = models.DateField()
#     criminallychargedstatuscase = models.CharField(max_length=50)
    
#     crimeorviolation = models.BooleanField(default=False)
#     crimedetails = models.TextField()
    
#     separatedfromservice = models.BooleanField(default=False)
#     separatedfromservicedetails = models.TextField()
    
#     localelectionlastyear = models.BooleanField(default=False)
#     localelectiondetails = models.TextField()
#     resignedtocampaignlast3months = models.BooleanField(default=False)
#     resignedtocampaigndetails = models.TextField()
    
#     acquiredimmigrantstatus = models.BooleanField(default=False)
#     immigrantstatuscountry = models.CharField(max_length=100)
    
#     indigenousgroup = models.BooleanField(default=False)
#     indigenousgroupidno = models.CharField(max_length=50)
#     personwithdisability = models.BooleanField(default=False)
#     personwithdisabilityidno = models.CharField(max_length=20)
#     soloparent = models.BooleanField(default=False)
#     soloparentidno = models.CharField(max_length=50)
    
# class References(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
    # ref1name = models.CharField(max_length=100)
    # ref1address = models.CharField(max_length=100)
    # ref1telno = models.CharField(max_length=50)
    
    # ref2name = models.CharField(max_length=100)
    # ref2address = models.CharField(max_length=100)
    # ref2telno = models.CharField(max_length=50)
    
    # ref3name = models.CharField(max_length=100)
    # ref3address = models.CharField(max_length=100)
    # ref3telno = models.CharField(max_length=50)

# class Government (models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     goviddescription = models.CharField(max_length=50)
#     govidnumber = models.CharField(max_length=20)
#     goviddateplaceissued = models.CharField(max_length=50)  

# Create your models here.
