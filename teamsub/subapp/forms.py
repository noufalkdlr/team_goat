from django.forms import ModelForm
from . import models

class MovieForm(ModelForm):
    class Meta:
        model = models.MovieInfo
        fields = '__all__'