from django.shortcuts import render,redirect, get_object_or_404
from .models import Assignment399
from django.http import Http404, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from .forms import Assignment399Form
from django.views.generic import CreateView,ListView,DetailView,UpdateView, DeleteView
# Create your views here.

def assignment399_list(request):
    qs = Assignment399.objects.all() # 교수들이 어드민에 올린거 이런식으로 받아오기

    q = request.GET.get('q','')
    if q:
        qs=qs.filter(title__icontains=q)

    return render(request, 'assignment399/assignment_list.html', {'assignment399_list':qs, 'q':q, })

def assignment399_detail(request,id):
#    post=Post.objects.get(id=id)
    assignment399 = get_object_or_404(Assignment399, id=id)
    return render(request, 'assignment399/assignment399_detail.html',{'assignment399':assignment399 })


def assignment399_new(request):
    if request.method=='POST':
        form = Assignment399Form(request.POST,request.FILES)
        if form.is_valid():
            assignment399=form.save()
            return redirect(assignment399) #post.get_absoluteurl() => post detail view 고쳐야함;; 모르겠다
    else:
        form=Assignment399Form()
    return render(request,'assignment399/assignment399_form.html', {'form':form})

def assignment399_edit(request,id):

    assignment399 = get_object_or_404(Assignment399, id=id)
    if request.method=='POST':
        form = Assignment399Form(request.POST,request.FILES, instance=assignment399)
        if form.is_valid():
            assignment399=form.save()
            return redirect(assignment399) #post.get_absoluteurl() => post detail view
    else:
        form = Assignment399Form(instance=assignment399)
    return render(request,'assignment399/assignment399_form.html', {'form':form,})
