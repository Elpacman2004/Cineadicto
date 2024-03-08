from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (request):
    return HttpResponse('<center>Remplazar el la parte donde dice "HttpResponse" con render(request, "Ubicacion de el archivo/Nombre de el archivo.html")<center/>')