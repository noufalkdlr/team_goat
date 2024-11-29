from django.shortcuts import render
from . import models
from . import forms

def index(request):
    frm = forms.MovieForm()
    return render(request,'index.html',{'frm':frm})

def list(request):
    movie_list =models.MovieInfo.objects.all()
    return render(request,'list.html',{'movie':movie_list})