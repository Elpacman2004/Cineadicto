from django.contrib.auth.models import Group 
from datetime import datetime
from django import forms
from Cineapp.models import Usuarios
from django.forms import ModelForm

class RegistroForm(ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nombre', 'email', 'password', 'fecha_nacimiento', 'preferencias'] 
        class MyCustomField(forms.Field):
            widgets = {
                'nombre': forms.TextInput(attrs={'class': 'form-control'}),
                'email': forms.EmailInput(attrs={'class': 'form-control'}),
                'password': forms.PasswordInput(attrs={'class': 'form-control'}), 
                'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control'}),
                'preferencias': forms.Textarea(attrs={'class': 'form-control'}),  
        }
    def clean(self):
        super().clean()
        errors = {}
   
        if self.cleaned_data['fecha_nacimiento'] > datetime.today() - datetime.timedelta(days=365 * 13):
            errors['fecha_nacimiento'] = 'Debes ser mayor de 13 años.'

        if Usuarios.objects.filter(email=self.cleaned_data['email']).exists():
            errors['email'] = 'El correo electrónico ya está registrado.'

        if errors:
            raise forms.ValidationError(errors)

        return self.cleaned_data