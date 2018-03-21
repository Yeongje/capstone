from django.shortcuts import render,redirect, get_object_or_404
from .models import Reflection
from django.http import Http404, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from .forms import ReflectionForm
from django.contrib import messages
from django.views.generic import CreateView,ListView,DetailView,UpdateView, DeleteView
# Create your views here.

#Post view Line and Number
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
