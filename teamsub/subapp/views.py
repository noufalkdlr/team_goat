from django.shortcuts import render,redirect
from . import models
from . import forms

def index(request):

    if request.POST:
        frm = forms.MovieForm(request.POST)
        if frm.is_valid():
            frm.save()
    else:
        frm = forms.MovieForm()
    
    Movie_frm ={
        'frm':frm
    }
    
    return render(request, 'index.html',Movie_frm)

def list(request):
    movie_list =models.MovieInfo.objects.all()
    return render(request,'list.html',{'movie':movie_list})

def movie_delete(requset, id):
    dele = models.MovieInfo.objects.get(id=id)
    dele.delete()
    return redirect('/list')