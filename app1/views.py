from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def welcome(request):
    return render(request,'welcome.html')


def app2home(request):
    return render(request,'home.html')
