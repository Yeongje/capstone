from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render,get_object_or_404
from .forms import SignupForm
from .models import Profile, Team
from django.contrib.auth.models import User
from django.urls import reverse


@login_required
def students(request):
    profiles =  Profile.objects.all()
    profiles1 = Profile.objects.all()
    users = User.objects.get(username=request.user.username)
    if users:
        profiles1=profiles1.filter(user=users)

    context = {'profiles1':profiles1, 'profiles':profiles, 'users':users,}
    return render(request, 'teams/students.html', context)

@login_required
def team_navi(request):
    profiles =  Profile.objects.all()
    profiles1 = Profile.objects.all()
    users = User.objects.get(username=request.user.username)
    if users:
        profiles1=profiles1.filter(user=users)

    context = {'profiles1':profiles1, 'profiles':profiles, 'users':users,}
    return render(request, 'teams/team_navi.html', context)


def teams(request,team_number):
    profiles = Profile.objects.filter(team_number = team_number)
    context = {'profiles':profiles,'team_number':team_number}
    return render(request,'teams/team.html',context)

def team_list(request):
    profiles =  Profile.objects.all()
    users = User.objects.get(username=request.user.username)
    qs = Team.objects.all() # 교수들이 어드민에 올린거 이런식으로 받아오기
    q = request.GET.get('q','')
    if users and q:
        profiles=profiles.filter(user=users)
        qs=qs.filter(title__icontains=q)
    context= {'team_list':qs, 'profiles':profiles,'users':users, }

    return render(request, 'teams/team_list.html', context)
