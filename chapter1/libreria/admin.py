from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.Genere)
admin.site.register(models.Autore)
admin.site.register(models.Libro)


