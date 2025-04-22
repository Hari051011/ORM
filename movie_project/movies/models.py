from django.db import models
from django.contrib import admin
class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    release_year = models.PositiveIntegerField()
    genre = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=3, decimal_places=1)

class movieadmin(admin.ModelAdmin):
    list_display=("movie_id","title","director","release_year","genre","rating")