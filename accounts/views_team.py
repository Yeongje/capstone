from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import SignupForm
from .models import Profile, Team
from django.contrib.auth.models import User




def students(request):
    profiles =  Profile.objects.all()
    context = {'profiles':profiles}
    return render(request, 'teams/students.html', context)


def teams(request,team_number):
    profiles = Profile.objects.filter(team_number = team_number)
    context = {'profiles':profiles,'team_number':team_number}
    return render(request,'teams/team.html',context)
