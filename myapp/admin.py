from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id","user","c_name","owner_name","Type") 
    list_editable = ("user","c_name","owner_name","Type") 

    
class ProblemsAdmin(admin.ModelAdmin):
    list_display = ("id","user","c_name","problem","from_date","to_date","image","video_url")  
    list_editable = ("user","c_name","problem","from_date","to_date","image","video_url")  
    
    
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id","user","s_name","mobile","branch","education","state","district","address")
    list_editable = ("user","s_name","mobile","branch","education","state","district","address")
    
    
class SolutionAdmin(admin.ModelAdmin):
    list_display = ("id","user","s_name","problem","from_date","to_date")  
    list_editable = ("user","s_name","problem","from_date","to_date")  
    
    
class Solution_progressAdmin(admin.ModelAdmin):
    list_display = ("id","user","s_name","progress_details","progress","date","image","video_url")
    list_editable = ("user","s_name","progress_details","progress","date","image","video_url")
    

admin.site.register(User,UserAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Problems, ProblemsAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Solution, SolutionAdmin)
admin.site.register(Solution_progress, Solution_progressAdmin)
