from django.contrib import admin
from .models import signup

# Register your models here.
@admin.register(signup)
class AdminSignup(admin.ModelAdmin):
    list_display=['username','password','email','dob']