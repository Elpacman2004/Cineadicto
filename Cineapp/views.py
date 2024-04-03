from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UsuarioForm, Pelicula
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import time
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.conf import settings
import requests



# Create your views here.
def home (request):
    return render(request, 'Home/Home.html')

def Test (request):
    return render(request, 'Login-SignUp/Registrarse.html')


def SignUp(request):
    if request.method == 'GET':
        print('Enviando formulario.')
        return render(request, 'Login-SignUp/SignUp.html', {
        })
    else:
        print(request.POST)
        if request.POST['password1'] == request.POST['password2']:
            try:
                usuario = User.objects.create(username=request.POST['username'], first_name=request.POST['name'], email=request.POST['email'], password=request.POST['password1'])
                usuario.save()
                login (request, usuario)
                return redirect('Cineapp')
            except IntegrityError:
                return render(request, 'Login-SignUp/SignUp.html', {
                    'Error': "El usuario ya existe"
                })
        return render(request, 'Login-SignUp/SignUp.html', {
            'Error': 'Las contraseñas no coinciden'
        })


    
def Help (request):
    return HttpResponse ('<h2>Remplazar el "HttpResponse" por un "render(request, "ruta/nombre de el archivo.html")"<h2/>')

def Cineapp (request):
    return render(request, 'CimeadictosViews/Princi.html')

def lgout (request):
    logout(request)
    return redirect('')

def lgin(request):
    if request.method == 'GET':
        print('Enviando formulario.')
        return render(request, 'Login-SignUp/SignUpP.html', {
            'form': AuthenticationForm
        })
    else:
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        User = authenticate(request, username=username, password=password)
        print(f"Resultado de autenticación para el usuario {username}: {User}")
        if User is None:
            return render(request, 'Login-SignUp/SignUpP.html', {
                'form': AuthenticationForm,
                'Error': 'Usuario o contraseña incorrecta'
            })
        else:
            login (request, User)
            return redirect('Cineapp')

        


def buscar_peliculas(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')  # Obtener el término de búsqueda de la URL
        api_key = '4c28c07e6116ea4ce1c5bcebbef281b1'  # Reemplaza 'tu_api_key' con tu propia API key de TMDB

        # Construir la URL de la API de TMDB para buscar películas
        url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={query}&language=es-ES'

        # Realizar la solicitud GET a la API de TMDB
        response = requests.get(url)

        if response.status_code == 200:
            # Obtener los datos de películas de la respuesta JSON
            datos = response.json()['results']
            # Agregar la URL del trailer para cada película si está disponible
            for pelicula in datos:
                trailer_url = obtener_trailer_url(pelicula['id'], api_key)
                pelicula['trailer_url'] = trailer_url

                pelicula['imagen_url'] = f"https://image.tmdb.org/t/p/w200/{pelicula['poster_path']}"
                pelicula['title'] = pelicula['title']
                pelicula['overview'] = pelicula['overview']
            return render(request, 'resultado_busqueda.html', {'peliculas': datos})
        else:
            return render(request, 'error.html', {'mensaje': 'Error al obtener datos de la API de TMDB'})

def obtener_trailer_url(pelicula_id, api_key):
    # Construir la URL de la API de TMDB para obtener los videos de una película
    url = f'https://api.themoviedb.org/3/movie/{pelicula_id}/videos?api_key={api_key}&language=es'
   
    # Realizar la solicitud GET a la API de TMDB
    response = requests.get(url)

    if response.status_code == 200:
        # Obtener los datos de videos de la respuesta JSON
        videos = response.json()['results']
        # Buscar el primer video de tipo 'Trailer' y devolver su URL
        for video in videos:
            if video['type'] == 'Trailer':
                return f'https://www.youtube.com/watch?v={video["key"]}'
    
    # Si no se encuentra ningún trailer, devolver None
    return None

def detalles_pelicula(request, pelicula_id):
    # Aquí realizas una solicitud a la API de TMDB para obtener los detalles de la película
    # Utilizas el ID de la película para construir la URL de la solicitud
    url = f'https://api.themoviedb.org/3/movie/{pelicula_id}'
    params = {
        'api_key': '4c28c07e6116ea4ce1c5bcebbef281b1',  # Reemplaza 'tu_api_key' con tu clave de API de TMDB
        'language': 'es'  # Opcional: define el idioma de los detalles de la película
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        pelicula = response.json()
        return render(request, 'detalles_pelicula.html', {'pelicula': pelicula})
    else:
        return render(request, 'error.html', {'mensaje': 'Error al obtener detalles de la película'})

def Listapeliculas(request):
    # URL de la API de TMDb para obtener la lista de películas
    url = 'https://api.themoviedb.org/3/discover/movie'
    
    # Parámetros de la solicitud GET a la API de TMDb
    params = {
        'api_key': '4c28c07e6116ea4ce1c5bcebbef281b1',  # Reemplaza 'TU_API_KEY' con tu propia API key de TMDb
        'language': 'es',  # Opcional: puedes cambiar el idioma de las películas
    }

    # Realizar la solicitud GET a la API de TMDb
    response = requests.get(url, params=params)

    # Verificar si la solicitud fue exitosa (código de respuesta 200)
    if response.status_code == 200:
        # Obtener los datos de las películas de la respuesta JSON
        data = response.json()['results']
        # Renderizar la plantilla con los datos de las películas
        return render(request, 'lista_peliculas.html', {'peliculas': data})
    else:
        # Si la solicitud no fue exitosa, mostrar un mensaje de error
        return render(request, 'error.html', {'mensaje': 'Error al obtener datos de la API de TMDb'})