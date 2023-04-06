from django.db import models

# Create your models here.

class EnquirySource(models.Model):
    Enquiry_Source_Name=models.CharField(max_length=75)
    def __str__(self):
        return self.Enquiry_Source_Name

class followupstatus(models.Model):
    followupstatusname=models.CharField(max_length=10)
    def __str__(self):
        return self.followupstatusname



class batch(models.Model):
    batchname=models.CharField(max_length=10)
    def __str__(self):
        return self.batchname
class details(models.Model):
    batchname=models.ForeignKey(batch,on_delete=models.CASCADE)
    course=models.CharField(max_length=30)
    trainer=models.CharField(max_length=30)
    Start_date=models.DateField()
    End_date=models.DateField()
    def __str__(self):
        return self.course,trainer,Start_date,End_date

class Qualifications(models.Model):
    Qualifications_Name=models.CharField(max_length=15)
    def __str__(self):
        return self.Qualifications_Name

class State(models.Model):
    State_Name=models.CharField(max_length=20)
    def __str__(self):
        return self.State_Name

class District(models.Model):
    State_Name=models.ForeignKey(State,on_delete=models.CASCADE)
    District_Name=models.CharField(max_length=30)
    def __str__(self):
        return self.District_Name

    
class StudentRegistration(models.Model):
    First_Name=models.CharField(max_length=30,blank=True,null=True)
    Last_Name=models.CharField(max_length=30,blank=True,null=True)
    Date_of_Birth=models.DateField()
    Qualifications_Name=models.CharField(max_length=30,blank=True,null=True)
    course = models.CharField(max_length=30, blank=True, null=True)
    batchname = models.CharField(max_length=30, blank=True, null=True)
    Registration_Number=models.CharField(max_length=30, blank=True, null=True)
    email=models.EmailField(max_length=30,blank=True,null=True)
    State_Name = models.CharField(max_length=30, blank=True, null=True)
    address=models.TextField(max_length=50,blank=True,null=True)
    District_Name = models.CharField(max_length=30, blank=True, null=True)
    place = models.CharField(max_length=30, blank=True, null=True)
    pincode=models.CharField(max_length=7,blank=True,null=True)
    Contact_Number = models.BigIntegerField(max_length=30, blank=True, null=True)
    Whatsapp_Number = models.BigIntegerField(max_length=30, blank=True, null=True)
    Name_of_Guardian=models.CharField(max_length=30,blank=True,null=True)
    Guardian_Number=models.BigIntegerField(max_length=30,blank=True,null=True)

    def __str__(self):
        return self.First_Name,self.Last_Name,self.Date_of_Birth,self.Qualifications_Name,self.Name_of_Guardian,self.Guardian_Number,\
            self.Whatsapp_Number,self.Contact_Number,self.batchname,self.course,self.State_Name,self.District_Name,\
            self.place,self.Registration_Number,self.email,self.address,self.pincode



class Branche(models.Model):
    Branch_name=models.CharField(max_length=200)
    def __str__(self):
        return self.Branch_name


class Companie(models.Model):
    Company_Name=models.CharField(max_length=100)
    def __str__(self):
        return self.Company_Name