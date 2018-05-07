from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
from django.contrib.auth.models import AbstractUser


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.PROTECT)
    student_number = models.CharField(max_length=20,null=True,blank=True)
    team_number = models.IntegerField(default=0,null=True,blank=True)
    major = models.CharField(max_length=10,null=True,blank=True)
    gpa = models.CharField(max_length=10,null=True,blank=True)
    number = models.ForeignKey('Team', null=True, blank=True, on_delete=models.SET_NULL)
    
    class Meta:
        ordering = ['team_number',]

    def __str__(self):
        return self.user.username



class Team(models.Model):
    team_number = models.ForeignKey('Profile', null=True, blank=True, on_delete=models.SET_NULL)
    number = models.IntegerField(default=0,null=True,blank=True)
    number_member = models.IntegerField(default=0,null=True,blank=True)


def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    if created:
        profile, is_created = Profile.objects.get_or_create(user=instance)

post_save.connect(post_save_user_receiver, sender=User)


     #team = models.ForeignKey('Team',on_delete=models.PROTECT)
# 이거하면 회원가입 오류 뜸.
