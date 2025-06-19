from django.db import models

# Create your models here.

class Autore(models.Model):
    nome = models.CharField(max_length = 50)
    cognome = models.CharField(max_length = 50)

    class Meta:
        verbose_name_plural = "Autori"

class Genere(models.Model):
    descrizione = models.CharField(max_length = 30)

    class Meta:
        verbose_name_plural = "Generi"

class Libro(models.Model):
    titolo = models.CharField(max_length = 200)
    autore = models.ForeignKey(Autore, on_delete = models.PROTECT)
    genere = models.ForeignKey(Genere, on_delete = models.PROTECT)

    class Meta:
        verbose_name_plural = "Libri"

