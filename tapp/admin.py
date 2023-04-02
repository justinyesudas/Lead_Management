from django.contrib import admin
from .models import EnquirySource,followupstatus,batch,details,Qualifications

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