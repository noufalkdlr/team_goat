from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('list/',views.list,name='list'),
    path('deletemovie/<int:id>',views.movie_delete,name = 'deletemovie')
    
]