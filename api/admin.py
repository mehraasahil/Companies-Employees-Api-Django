from django.contrib import admin
from api.models import Company,Employee
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    # list_display=('name','location','type')
    list_display=('name','type')

class EmployeeAdmin(admin.ModelAdmin):
    # list_display=('name','email','company')
    list_display=('name','email','company','phone','position')    

admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)