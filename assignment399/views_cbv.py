from django.views.generic import CreateView,ListView,DetailView,UpdateView, DeleteView
from .models import Assignment399
from django import forms
from django.urls import reverse_lazy

assignment399_list = ListView.as_view(model=Assignment399, paginate_by=5)

assignment399_delete = DeleteView.as_view(model = Assignment399, success_url=reverse_lazy('assignment399:assignment399_list'))


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment399
        fields = '__all__'

class PostCreateView(CreateView):
    model = Assignment399
    form_class = AssignmentForm
