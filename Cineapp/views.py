from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistroForm
from .models import Usuarios
from django.contrib.auth.forms import UserCreationForm
import time
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError


# Create your views here.
def home (request):
    return render(request, 'Home/Home.html')

def Test (request):
    return render(request, 'Login-SignUp/Registrarse.html')
def Login (request):
    return HttpResponse ('<h2>Remplazar el "HttpResponse" por un "render(request, "ruta/nombre de el archivo.html")"<h2/>')


def SignUp(request):
    if request.method == 'GET':
        print('Enviando formulario.')
        return render(request, 'Login-SignUp/SignUp.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                Usuario = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                Usuario.save()
                login (request, Usuario)
                return redirect('Cineapp')
            except IntegrityError:
                return render(request, 'SignUp.html', {
                    'form': UserCreationForm,
                    'Error': "El usuario ya existe"
                })
        return render(request, 'SignUp.html', {
            'form': UserCreationForm,
            'Error': 'Las contraseñas no coinciden'
        })


    
def Help (request):
    return HttpResponse ('<h2>Remplazar el "HttpResponse" por un "render(request, "ruta/nombre de el archivo.html")"<h2/>')

def Cineapp (request):
    return render(request, 'CimeadictosViews/Cineapp.html')