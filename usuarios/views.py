from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import UserRegisterForm, UserEditForm
from .models import Avatar
def login_request(request):
    msg_login=""
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():  # Si pasó la validación de Django
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username= usuario, password=contrasenia)
            if user is not None:
                login(request, user)
                return render(request, "plantillas/inicio.html", {"mensaje":f"Bienvenido {usuario}"})         
        msg_login="Usuario o contraseña incorrectos"
    form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form, "msg_login":msg_login } )

def register(request):
    msg_register=""
    if request.method =="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"plantillas/inicio.html")
        msg_register="Error"
    form = UserRegisterForm()
    return render(request,"users/register.html" , {"form":form, "msg_register":msg_register}  )

@login_required
def editar_perfil(request):
    usuario = request.user
    if request.method == "POST":
        miFormulario = UserEditForm(request.POST, request.FILES, instance=usuario)
        if miFormulario.is_valid():
            if hasattr(usuario, 'avatar'):
                if miFormulario.cleaned_data.get('imagen'):
                    usuario.avatar.imagen = miFormulario.cleaned_data.get('imagen')
                    usuario.avatar.save()
            else:
                # Crear un nuevo avatar si no existe
                avatar = Avatar(user=usuario, imagen=miFormulario.cleaned_data.get('imagen'))
                avatar.save()
            miFormulario.save()
            return render(request, "plantillas/inicio.html")
    else:
        miFormulario = UserEditForm(instance=usuario)
    return render(request, "users/editar_perfil.html", {"miFormulario": miFormulario, "usuario": usuario})

class CambiarContrasenia(LoginRequiredMixin,PasswordChangeView):
    template_name="users/editar_pass.html"
    success_url=reverse_lazy ('editar_perfil')
