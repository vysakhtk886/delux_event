from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def Testfn(request):
#     return HttpResponse('hloooo')
def home(request):
    return render(request,'home.html')
def login(request):
    return render(request,'login_page.html')
def register(request):
    return render(request,'registration_page.html')
