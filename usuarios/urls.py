from django.urls import path
from django.contrib.auth.views import LogoutView
from usuarios.views import *


urlpatterns = [
    path('login/',login_request, name="Login"),
    path('register/',register, name='Register'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='Logout'),
    path('editar_perfil/',editar_perfil, name='editar_perfil'),
    path('editar_pass/',CambiarContrasenia.as_view(),name="editar_pass"), 

]