# Ex02 Django ORM Web Application
# Date:11/04/2025
# AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

# ENTITY RELATIONSHIP DIAGRAM
## DESIGN STEPS
## STEP 1:
Clone the problem from GitHub

## STEP 2:
Create a new app in Django project

## STEP 3:
Enter the code for admin.py and models.py

## STEP 4:
Execute Django admin and create details for 10 books

# PROGRAM

models.py
```
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

```

admin.py
```
from django.contrib import admin
from .models import Movie,movieadmin

admin.site.register(Movie,movieadmin)
```

# OUTPUT


![alt text](<Screenshot 2025-04-22 224501.png>)


# RESULT
Thus the program for creating a database using ORM hass been executed successfully
