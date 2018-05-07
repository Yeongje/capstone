from django.contrib import admin
from .models import Profile, Team
# Register your models here.


from django.conf import settings

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


#admin.site.register(Profile)
#admin.site.register(Team)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','student_number','team_number','number']

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['number']
