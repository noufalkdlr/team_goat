from django.shortcuts import render
from . import models

def index(request):
    return render(request,'index.html')

def list(request):
    return render(request,'list.html')