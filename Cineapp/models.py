from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.validators import EmailValidator
from django.utils import timezone

# Create your models here.

class Usuario(models.Model):
    username = models.CharField(max_length=250, verbose_name="Nombre de usuario")
    name = models.CharField(max_length=250, verbose_name="Nombre")
    email = models.EmailField(max_length=250, verbose_name="Correo electrónico")
    password = models.CharField(max_length=250, verbose_name="Contraseña")

    def __str__(self):
        return self.username

class Pelicula(models.Model):
    title = models.CharField(null=True, max_length=250, verbose_name="Título")
    description = models.TextField(null=True, verbose_name="Descripción")
    genre = models.CharField(null=True, max_length=100, verbose_name="Género")
    release_year = models.PositiveIntegerField(null=True, verbose_name="Año de lanzamiento")
    duration = models.PositiveIntegerField(null=True, verbose_name="Duración (minutos)")
    rating = models.DecimalField(null=True, max_digits=3, decimal_places=1, verbose_name="Calificación")
    director = models.CharField(null=True, max_length=250, verbose_name="Director")
    lead_actors = models.TextField(null=True, verbose_name="Actores principales")
    poster = models.ImageField(null=True, upload_to="posters/", verbose_name="Póster")
    trailer = models.URLField(null=True, verbose_name="Enlace al tráiler")
    language = models.CharField(null=True, max_length=50, verbose_name="Idioma")
    date_added = models.DateTimeField(null=True, auto_now_add=True, verbose_name="Fecha de agregado a la base de datos")


    def __str__(self):
        return self.title