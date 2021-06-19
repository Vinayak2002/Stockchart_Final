from django.contrib import admin

from .models import Userdetails

# Register your models here.
"""
In this way we register the created model in the admin app. 
"""
admin.site.register(Userdetails)