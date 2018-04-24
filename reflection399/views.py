from django.shortcuts import render,redirect, get_object_or_404
from .models import Reflection399
from django.http import Http404, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from .forms import Reflection399Form
from django.contrib import messages
from django.views.generic import CreateView,ListView,DetailView,UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.views.generic import DeleteView
from django.urls import reverse_lazy
# Create your views here.

def reflection399_list(request):
    qs = Reflection399.objects.all() # 교수들이 어드민에 올린거 이런식으로 받아오기
    q = request.GET.get('q','')
    if q:
        qs=qs.filter(team_number__icontains=q)

    return render(request, 'reflection399/reflection399_list.html', {'reflection399_list':qs, 'q':q, })

def reflection399_detail(request,id):
#    post=Post.objects.get(id=id)
    reflection399 = get_object_or_404(Reflection399, id=id)
    return render(request, 'reflection399/reflection399_detail.html',{'reflection399':reflection399 ,})


def reflection399_new(request):
    users = User.objects.get(username=request.user.username)

    if request.method=='POST':
        form = Reflection399Form(request.POST,request.FILES)


        if form.is_valid():
            reflection399=form.save()
            messages.success(request,'New reflection was saved')
            return redirect(reflection399) #post.get_absoluteurl() => post detail view
    else:
        form=Reflection399Form()

    return render(request,'reflection399/reflection399_form.html', {'form':form})

def reflection399_edit(request,id):
    reflection399 = get_object_or_404(Reflection399, id=id)
    if request.method=='POST':
        form = Reflection399Form(request.POST,request.FILES, instance=reflection399)
        if form.is_valid():
            reflection399=form.save()
            messages.success(request,'New reflection was edited')
            return redirect(reflection399) #post.get_absoluteurl() => post detail view
    else:
        form = Reflection399Form(instance=reflection399)
    return render(request,'reflection399/reflection399_form.html', {'form':form,})




reflection399_delete = DeleteView.as_view(model = Reflection399, success_url=reverse_lazy('reflection399:reflection399_list'))
