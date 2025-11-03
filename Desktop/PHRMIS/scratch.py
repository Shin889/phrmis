

class PersonalDataSheet(models.Model):
    relatedaffinityb3rd_degree = models.BooleanField(default=False)
    relatedaffinityb4th_degree = models.BooleanField(default=False)
    relatedaffinitydetails = models.CharField(max_length=50)
    
    administrativeoffense = models.BooleanField(default=False)
    administrativeoffensedetails = models.TextField()
    criminallychargedbeforecourt = models.BooleanField(default=False)
    criminallychargeddetails = models.TextField()
    criminallychargeddatefiled = models.DateField()
    criminallychargedstatuscase = models.CharField(max_length=50)
    
    crimeorviolation = models.BooleanField(default=False)
    crimedetails = models.TextField()
    
    separatedfromservice = models.BooleanField(default=False)
    separatedfromservicedetails = models.TextField()
    
    localelectionlastyear = models.BooleanField(default=False)
    localelectiondetails = models.TextField()
    resignedtocampaignlast3months = models.BooleanField(default=False)
    resignedtocampaigndetails = models.TextField()
    
    acquiredimmigrantstatus = models.BooleanField(default=False)
    immigrantstatuscountry = models.CharField(max_length=100)
    
    indigenousgroup = models.BooleanField(default=False)
    indigenousgroupidno = models.CharField(max_length=50)
    personwithdisability = models.BooleanField(default=False)
    personwithdisabilityidno = models.CharField(max_length=20)
    soloparent = models.BooleanField(default=False)
    soloparentidno = models.CharField(max_length=50)
    
class References(models.Model):
    ref1name = models.CharField(max_length=100)
    ref1address = models.CharField(max_length=100)
    ref1telno = models.CharField(max_length=50)
    
    ref2name = models.CharField(max_length=100)
    ref2address = models.CharField(max_length=100)
    ref2telno = models.CharField(max_length=50)
    
    ref3name = models.CharField(max_length=100)
    ref3address = models.CharField(max_length=100)
    ref3tel_no = models.CharField(max_length=50)

class Government (models.Model):
    goviddescription = models.CharField(max_length=50)
    govidnumber = models.CharField(max_length=20)
    goviddateplaceissued = models.CharField(max_length=50)  
    
