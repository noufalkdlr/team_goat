from django.db import models

class MovieInfo(models.Model):
    title = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='poster',default="")
