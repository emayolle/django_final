from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=15)
    genres = models.ManyToManyField(Genre, related_name='movies')

    def __str__(self):
        return f"{self.title} ({self.year})"