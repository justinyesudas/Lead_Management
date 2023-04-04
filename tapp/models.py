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
    First_Name=models.CharField(max_length=25)
    Last_Name=models.CharField(max_length=25)
    Date_of_Birth=models.DateField()
    Name_of_Guardian=models.CharField(max_length=25)
    Guardian_Number=models.IntegerField(max_length=10)
    course=models.ForeignKey(details,on_delete=models.CASCADE)
    State_Name=models.ForeignKey(State,on_delete=models.CASCADE)
    District_Name=models.ForeignKey(District,on_delete=models.CASCADE)
    place=models.CharField(max_length=30)
    Whatsapp_Number=models.IntegerField(max_length=10)
    Contact_Number=models.IntegerField(max_length=10)
    batchname = models.ForeignKey(batch,on_delete=models.CASCADE)
    def __str__(self):
        return self.First_Name,self.Last_Name,self.Date_of_Birth,self.Name_of_Guardian,self.Guardian_Number,self.Whatsapp_Number,self.Contact_Number,self.batchname,self.course,self.State_Name,self.District_Name,self.place




class Branche(models.Model):
    Branch_name=models.CharField(max_length=200)
    def __str__(self):
        return self.Branch_name