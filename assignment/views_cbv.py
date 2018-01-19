from django.views.generic import CreateView,ListView,DetailView,UpdateView, DeleteView
from .models import Assignment
from django import forms
from django.urls import reverse_lazy

assignment_list = ListView.as_view(model=Assignment, paginate_by=5)

assignment_delete = DeleteView.as_view(model = Assignment, success_url=reverse_lazy('assignment:assignment_list'))


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = '__all__'

class PostCreateView(CreateView):
    model = Assignment
    form_class = AssignmentForm
