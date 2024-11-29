from django.shortcuts import render
from . import models

def index(request):
    return render(request,'index.html')

def list(request):
    movie_list =models.MovieInfo.objects.all()
    return render(request,'list.html',{'movie':movie_list})