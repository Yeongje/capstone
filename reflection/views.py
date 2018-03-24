from django.shortcuts import render,redirect, get_object_or_404
from .models import Reflection
from django.http import Http404, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from .forms import ReflectionForm
from django.contrib import messages
from django.views.generic import CreateView,ListView,DetailView,UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
# Create your views here.

def reflection_list(request):
    qs = Reflection.objects.all() # 교수들이 어드민에 올린거 이런식으로 받아오기
    q = request.GET.get('q','')
    if q:
        qs=qs.filter(team_number__icontains=q)

    return render(request, 'reflection/reflection_list.html', {'reflection_list':qs, 'q':q, })

def reflection_detail(request,id):
#    post=Post.objects.get(id=id)
    reflection = get_object_or_404(Reflection, id=id)
    return render(request, 'reflection/reflection_detail.html',{'reflection':reflection ,})


def reflection_new(request):
    if request.method=='POST':
        form = ReflectionForm(request.POST,request.FILES)
        if form.is_valid():
            reflection=form.save()
            messages.success(request,'New reflection was saved')
            return redirect(reflection) #post.get_absoluteurl() => post detail view
    else:
        form=ReflectionForm()
    return render(request,'reflection/reflection_form.html', {'form':form})

def reflection_edit(request,id):
    reflection = get_object_or_404(Reflection, id=id)
    if request.method=='POST':
        form = ReflectionForm(request.POST,request.FILES, instance=reflection)
        if form.is_valid():
            reflection=form.save()
            messages.success(request,'New reflection was edited')
            return redirect(reflection) #post.get_absoluteurl() => post detail view
    else:
        form = ReflectionForm(instance=reflection)
    return render(request,'reflection/reflection_form.html', {'form':form,})
