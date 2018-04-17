from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile


class SignupForm(UserCreationForm):

    student_number = forms.CharField()

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

    def save(self):
        user = super().save()
        profile = Profile.objects.create(
            user = user,
            student_number= self.cleaned_data['student_number'])
        return user

#class LoginForm(AuthenticationForm):
#    answer = forms.IntegerField(label='3+3=?')
#        if self.cleaned_data.get('answer', None) != 6:
#            raise forms.ValidationError('wrong')
#        return answer
