from django.shortcuts import render,redirect, get_object_or_404
from .models import Assignment
from django.http import Http404, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from .forms import AssignmentForm
from django.views.generic import CreateView,ListView,DetailView,UpdateView, DeleteView
from django.contrib import messages
# Create your views here.

def assignment_list(request):
    qs = Assignment.objects.all() # 교수들이 어드민에 올린거 이런식으로 받아오기

    q = request.GET.get('q','')
    if q:
        qs=qs.filter(title__icontains=q)

    return render(request, 'assignment/assignment_list.html', {'assignment_list':qs, 'q':q, })

def assignment_detail(request,id):
#    post=Post.objects.get(id=id)
    assignment = get_object_or_404(Assignment, id=id)
    return render(request, 'assignment/assignment_detail.html',{'assignment':assignment })


def assignment_new(request):
    if request.method=='POST':
        form = AssignmentForm(request.POST,request.FILES)
        if form.is_valid():
            assignment=form.save()
            messages.success(request,'New post was saved')
            return redirect(assignment) #post.get_absoluteurl() => post detail view 고쳐야함;; 모르겠다
    else:
        form=AssignmentForm()
    return render(request,'assignment/assignment_form.html', {'form':form})

def assignment_edit(request,id):

    assignment = get_object_or_404(Assignment, id=id)
    if request.method=='POST':
        form = AssignmentForm(request.POST,request.FILES, instance=assignment)
        if form.is_valid():
            assignment=form.save()
            return redirect(assignment) #post.get_absoluteurl() => post detail view
    else:
        form = AssignmentForm(instance=assignment)
    return render(request,'assignment/assignment_form.html', {'form':form,})
