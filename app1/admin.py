from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Student)

class Studentadmin(admin.ModelAdmin):
    list_display= ['id','name','email','roll','address']

