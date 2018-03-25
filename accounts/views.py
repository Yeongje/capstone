from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import SignupForm
from .models import Profile
from django.contrib.auth.models import User


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(settings.LOGIN_URL)  # default : "/accounts/login/"
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html', {
        'form': form,
    })


@login_required
def profile(request):
    profiles =  Profile.objects.all()
    users = User.objects.get(username=request.user.username) # request User name
    if users:
        profiles=profiles.filter(user=users)

    return render(request, 'accounts/profile.html',{'profile':profiles,'users':users,})

def students(request):
    profiles =  Profile.objects.all()
    context = {'profiles':profiles}
    return render(request, 'teams/students.html', context)
