from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404,redirect, HttpResponseRedirect
from django.contrib.auth.views import login as auth_login
from django.contrib.auth import authenticate
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers
from .forms import SignupForm,UserForm, ProfileForm
from .models import Profile,Team
from django.contrib.auth.models import User

from allauth.socialaccount.views import SignupView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.views.generic import UpdateView

User = get_user_model()

class MySignupView(SignupView):
    template_name = ('accounts/signup_form.html')
socialsignup = MySignupView.as_view()

@login_required
def update_profile(request):

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(profile)

    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'accounts/profile_update.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

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
