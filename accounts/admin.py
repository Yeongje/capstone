from django.contrib import admin
from .models import Profile, Team
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','student_number']

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['team_number']
