from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.views import login as auth_login
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers
from .forms import SignupForm
from .models import Profile
from django.contrib.auth.models import User


# social login
def login(request):
    providers = []
    for provider in get_providers():  # settings/INSTALLED_APPS

        # social_app속성은 provider에는 없는 속성입니다.
        try:
            # 실제 Provider 별 Client id/secret 이 등록이 되어있는가?
            provider.social_app = SocialApp.objects.get(provider=provider.id, sites=settings.SITE_ID)
        except SocialApp.DoesNotExist:
            provider.social_app = None
        providers.append(provider)

    return auth_login(request,
        #authentication_form=LoginForm,
        template_name='accounts/login_form.html',
        extra_context={'providers': providers})


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
