from django.shortcuts import render,redirect, get_object_or_404
from .models import Post
from django.http import Http404, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from .forms import PostForm
from django.contrib import messages
from django.views.generic import CreateView,ListView,DetailView,UpdateView, DeleteView
# Create your views here.

#Post view Line and Number


def post_list(request):

    qs = Post.objects.all() # 교수들이 어드민에 올린거 이런식으로 받아오기

    q = request.GET.get('q','')
    if q:
        qs=qs.filter(title__icontains=q)

    return render(request, 'project/post_list.html', {'post_list':qs, 'q':q, })

def post_detail(request,id):
#    post=Post.objects.get(id=id)
    post = get_object_or_404(Post, id=id)
    return render(request, 'project/post_detail.html',{'post':post ,})


def post_new(request):
    if request.method=='POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save()
            messages.success(request,'New post was saved')
            return redirect(post) #post.get_absoluteurl() => post detail view
    else:
        form=PostForm()
    return render(request,'project/post_form.html', {'form':form})

def post_edit(request,id):

    post = get_object_or_404(Post, id=id)
    if request.method=='POST':
        form = PostForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            post=form.save()
            messages.success(request,'New post was edited')
            return redirect(post) #post.get_absoluteurl() => post detail view
    else:
        form = PostForm(instance=post)
    return render(request,'project/post_form.html', {'form':form,})
