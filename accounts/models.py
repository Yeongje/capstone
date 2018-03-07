from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class Team(models.Model):
    team_number = models.CharField(max_length=10,blank=True)

class Profile(models.Model):
     user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.PROTECT)
     student_number = models.CharField(max_length=20)
     major = models.CharField(max_length=10,blank=True)
     gpa = models.CharField(max_length=10,blank=True)
#     team = models.ForeignKey('Team',on_delete=models.PROTECT)
# 이거하면 회원가입 오류 뜸.
