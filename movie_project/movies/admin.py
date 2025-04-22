from django.contrib import admin
from .models import Movie,movieadmin

admin.site.register(Movie,movieadmin)
