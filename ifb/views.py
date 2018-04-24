from django.shortcuts import render

# Create your views here.


def first_page(request):

    return render(request, 'ifb/first_page.html')

def ifb398_first_page(request):

    return render(request, 'ifb/ifb398_first_page.html')

def ifb399_first_page(request):

    return render(request, 'ifb/ifb399_first_page.html')
