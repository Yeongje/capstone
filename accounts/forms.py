from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UserChangeForm
from .models import Profile
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):

    student_number = forms.CharField()
    major = forms.CharField()
    gpa = forms.CharField()

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

    def save(self):
        user = super().save()
        profile = Profile.objects.create(
            user = user,
            student_number= self.cleaned_data['student_number'],
            major= self.cleaned_data['major'],
            gpa= self.cleaned_data['gpa'])
        return user


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('student_number','team_number','major', 'gpa')
