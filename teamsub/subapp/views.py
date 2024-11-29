from django.shortcuts import render,redirect
from . import models
from . import forms

def index(request):
    
    return render(request, 'index.html',)

def list(request):
    movie_list =models.MovieInfo.objects.all()
    return render(request,'list.html',{'movie':movie_list})