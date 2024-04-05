from django.contrib import admin
from django.db import models
import movie_searcher
# Register your models here.

for model in movie_searcher.models.__dict__.values():
    try:
        if issubclass(model, models.Model):
            admin.site.register(model)
    except TypeError:
        pass