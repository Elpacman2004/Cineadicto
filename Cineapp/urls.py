from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='prueba'),
    path('test/', views.Test, name='Test'),
    path('Login', views.Login, name='Log-in'),
    path('SignUp', views.SignUp, name='SignUp'),
    path('Help', views.Help, name='Help'),
    path('Cineapp', views.Cineapp, name='Cineapp'),
    path('Logout', views.lgout, name='Logout'),
    path('buscar-peliculas/', views.buscar_peliculas, name='buscar-peliculas'),
    path('detalles-pelicula/<int:pelicula_id>/', views.detalles_pelicula, name='detalles-pelicula'),
    
]
