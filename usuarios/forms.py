#from django.apps import AppConfig
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm #formulario que trae django por defecto, pero se le pueden agregar modifacciones
from django.contrib.auth.models import User


#class UsuariosConfig(AppConfig):
#    default_auto_field = 'django.db.models.BigAutoField'
#    name = 'usuarios'


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(min_length=4, max_length=30)
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"hola" for k in fields}

class UserEditForm(UserChangeForm):
    password=None
    username = forms.CharField(disabled=True)
    email=forms.EmailField(label="Ingrese su email")
    first_name=forms.CharField(label="Nombre",required=False)
    last_name=forms.CharField(label="Apellido",required=False)
    
    descripcion=forms.CharField(label="Descripción adicional",required=False)
    imagen=forms.ImageField(label="Avatar",required=False)
    class Meta:
        model=User
        fields= ['username','email','first_name','last_name','descripcion','imagen' ]


