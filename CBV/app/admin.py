from django.contrib import admin
from .models import *
# Register your models here.


class SclCust(admin.ModelAdmin):
    list_display = ['sclname','sclprince','sclloc']

class StdCust(admin.ModelAdmin):
    list_display = ['sclname','stdname','stdage']
    
admin.site.register(School,SclCust)

admin.site.register(Student,StdCust)