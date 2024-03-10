from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='prueba'),
    path('test/', views.Test, name='Test'),
    path('Login', views.Login, name='Log-in'),
    path('SignUp', views.SignUp, name='SignUp'),
    path('Help', views.Help, name='Help')
]
