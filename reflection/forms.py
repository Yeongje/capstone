from django import forms
from .models import Reflection

class ReflectionForm(forms.ModelForm):
    class Meta:
        model = Reflection
        fields = '__all__'




#    def __init__(self, user, *args, **kwargs):
#        super(ReflectionForm,self).__init__(*args, **kwargs)self.fields['student_name'].queryset = Member.objects.filter(user=user)
