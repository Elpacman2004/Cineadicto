from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.validators import EmailValidator

# Create your models here.

class Usuarios(AbstractUser):
    username = models.CharField(max_length=150, unique=True, default='default_username')
    password = models.CharField(max_length=100, default='mi_password_predeterminado')
    correo_electronico = models.EmailField(max_length=255, unique=True, validators=[EmailValidator()])
    nombre = models.CharField(max_length=50, blank=False)
    apellidos = models.CharField(max_length=100, blank=False)
    fecha_nacimiento = models.DateField(blank=False)
    preferencias = models.JSONField(null=True, blank=True)
    groups = models.ManyToManyField(Group, related_name='cineapp_usuarios')
    user_permissions = models.ManyToManyField(Permission, related_name='cineapp_usuarios_permissions')

class UsuarioGroups(models.Model):
    Usuarios = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

class UsuarioUserPermissions(models.Model):
    Usuarios = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario.nombre} {self.usuario.apellidos} ({self.usuario.correo_electronico})"