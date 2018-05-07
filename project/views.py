from django.shortcuts import render,redirect, get_object_or_404
from .models import Post, Comment
from django.http import Http404, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from .forms import PostForm, CommentForm
from django.contrib import messages
from django.views.generic import CreateView,ListView,DetailView,UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
# Create your views here.

#Post view Line and Number


def post_list(request):

    qs = Post.objects.all().prefetch_related('comment_set') # 교수들이 어드민에 올린거 이런식으로 받아오기

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


def comment_list(request):
    comment_list = Comment.objects.all().select_related('post')
    return render(request, 'project/comment_list.html', {'comment_list':comment_list,
    })

def comment_new(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method=='POST':
        form = CommentForm(request.POST,request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            #messages.success(request,'New application was saved')
            return redirect('project:post_detail',post.pk) #post.get_absoluteurl() => post detail view
    else:
        form=CommentForm()
    return render(request,'project/comment_form.html', {'form':form})
'''
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST,request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('project:post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'project/add_comment_to_post.html', {'form': form})
'''
@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('project:post_detail', comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('project:post_detail', comment.post.pk)
