from django.contrib import admin
from .models import*
from managementapp.models import User
# Register your models here.

admin.site.register(User)
admin.site.register(Profile)
