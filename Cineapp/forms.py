from django.contrib.auth.models import Group 
from datetime import datetime
from django import forms
from .models import Usuario, Pelicula
from django.forms import ModelForm

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'name', 'email', 'password']
        labels = {
            'username': 'Nombre de usuario',
            'name': 'Nombre',
            'email': 'Correo electrónico',
            'password': 'Contraseña',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input-contenedor'}),
            'name': forms.TextInput(attrs={'class': 'input-contenedor'}),
            'email': forms.TextInput(attrs={'class': 'input-contenedor'}),
            'password': forms.TextInput(attrs={'class': 'input-contenedor'}),
        }

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['title', 'description', 'genre', 'release_year', 'duration', 'director', 'lead_actors', 'poster', 'trailer', 'language']
        labels = {
            'title': 'Título',
            'description': 'Descripción',
            'genre': 'Género',
            'release_year': 'Año de lanzamiento',
            'duration': 'Duración (minutos)',
            'director': 'Director',
            'lead_actors': 'Actores principales',
            'poster': 'Póster',
            'trailer': 'Enlace al tráiler',
            'language': 'Idioma',
        }