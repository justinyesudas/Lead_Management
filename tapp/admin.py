from django.contrib import admin
from .models import EnquirySource,followupstatus,batch,details,Qualifications,State,District,StudentRegistration,Branche,Companie

# Register your models here.

class EnquirySource_Admin(admin.ModelAdmin):
    list_display=('Enquiry_Source_Name',)
admin.site.register(EnquirySource,EnquirySource_Admin)

class followupstatusAdmin(admin.ModelAdmin):
    list_display=('followupstatusname',)
admin.site.register(followupstatus,followupstatusAdmin)


class batchAdmin(admin.ModelAdmin):
    list_display=('batchname',)
admin.site.register(batch,batchAdmin)

class detailsAdmin(admin.ModelAdmin):
    list_display=('course','trainer','Start_date','End_date')
admin.site.register(details,detailsAdmin)

class Qualifications_Admin(admin.ModelAdmin):
    list_display=('Qualifications_Name',)
admin.site.register(Qualifications,Qualifications_Admin)


class State_Admin(admin.ModelAdmin):
    list_display=('State_Name',)
admin.site.register(State,State_Admin)

class District_Admin(admin.ModelAdmin):
    list_display=('State_Name','District_Name')
admin.site.register(District,District_Admin)


class StudentRegistration_Admin(admin.ModelAdmin):
    list_display=('First_Name','Last_Name','Date_of_Birth','Qualifications_Name','course','batchname',
                  'Registration_Number','email','State_Name','address','District_Name','place',
                  'pincode','Contact_Number','Whatsapp_Number','Name_of_Guardian','Guardian_Number')
admin.site.register(StudentRegistration,StudentRegistration_Admin)



class branchadmin(admin.ModelAdmin):
    list_display=('Branch_name',)
admin.site.register(Branche,branchadmin)


class Companie_Admin(admin.ModelAdmin):
    list_display=('Company_Name',)
admin.site.register(Companie,Companie_Admin)
