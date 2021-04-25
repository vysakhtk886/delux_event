from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Testfn(request):
    return HttpResponse('hloooo')
def html1(request):
    return render(request,'home.html')
