from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (request):
    return render(request, 'Home.html')

def Test (request):
    return render(request, 'layouts/Base.html')
def Login (request):
    return HttpResponse ('<h2>Remplazar el "HttpResponse" por un "render(request, "ruta/nombre de el archivo.html")"<h2/>')
def SignUp (request):
    return HttpResponse ('<h2>Remplazar el "HttpResponse" por un "render(request, "ruta/nombre de el archivo.html")"<h2/>')
def Help (request):
    return HttpResponse ('<h2>Remplazar el "HttpResponse" por un "render(request, "ruta/nombre de el archivo.html")"<h2/>')