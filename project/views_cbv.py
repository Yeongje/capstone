from django.views.generic import CreateView,ListView,DetailView,UpdateView, DeleteView
from .models import Post
from django import forms
from django.urls import reverse_lazy

post_list = ListView.as_view(model=Post,paginate_by=5)

post_delete = DeleteView.as_view(model = Post, success_url=reverse_lazy('project:post_list'))

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
