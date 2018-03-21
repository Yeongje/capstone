from django.views.generic import CreateView,ListView,DetailView,UpdateView, DeleteView
from .models import Reflection
from django import forms
from django.urls import reverse_lazy

reflection_list = ListView.as_view(model=Reflection,paginate_by=10)

reflection_delete = DeleteView.as_view(model = Reflection, success_url=reverse_lazy('reflection:reflection_list'))

class ReflectionForm(forms.ModelForm):
    class Meta:
        model = Reflection
        fields = '__all__'

class ReflectionCreateView(CreateView):
    model = Reflection
    form_class = ReflectionForm

# post_detail = DetailView.as_view(model=Post, pk_url_kwarg='id')
