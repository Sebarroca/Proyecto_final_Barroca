from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import *
from .models import *


def inicio(request):
    cursos = Curso.objects.all()
    profesores = Profesor.objects.all()
    estudiantes = Estudiante.objects.all()
    return render(request,"plantillas/inicio.html",{"cursos": cursos, "profesores": profesores, "estudiantes": estudiantes})

def about(request):
    return render(request,"plantillas/about.html")

def buscarCurso(request):
    comision = request.GET.get('comision')
    nombre = request.GET.get('nombre')
    if comision and nombre:
        cursos = Curso.objects.filter(comision=comision, nombre__icontains=nombre)  # icontains es que contenga los caracteres
        return render(request, "plantillas/cursos.html", {"cursos": cursos, "comision": comision, "nombre": nombre})
    elif comision:
        cursos = Curso.objects.filter(comision=comision)
        return render(request, "plantillas/cursos.html", {"cursos": cursos, "comision": comision})
    elif nombre:
        cursos = Curso.objects.filter(nombre__icontains=nombre)
        return render(request, "plantillas/cursos.html", {"cursos": cursos, "nombre": nombre})
    else:
        mensaje = "No ha ingresado ningún valor"
        return render(request, "plantillas/cursos.html", {"mensaje": mensaje})
def buscarEstudiante(request):
    apellido=request.GET.get('apellido')
    if apellido:
        estudiantes=Estudiante.objects.filter(apellido__icontains=apellido)
        return render(request,"plantillas/estudiantes.html",{"estudiantes":estudiantes,"apellido":apellido}   )
    else:
        mensaje = "No ha ingresado ningún valor"
        return render(request, "plantillas/estudiantes.html", {"mensaje": mensaje})
def buscarProfesor(request):
    apellido = request.GET.get('apellido')
    especialidad = request.GET.get('especialidad')
    if apellido and especialidad:
        profesores = Profesor.objects.filter(apellido__icontains=apellido, especialidad__icontains=especialidad)
        return render(request, "plantillas/profesores.html", {"profesores": profesores, "apellido": apellido, "especialidad": especialidad})
    elif apellido:
        profesores = Profesor.objects.filter(apellido__icontains=apellido)
        return render(request, "plantillas/profesores.html", {"profesores": profesores, "apellido": apellido})
    elif especialidad:
        profesores = Profesor.objects.filter(especialidad__icontains=especialidad)
        return render(request, "plantillas/profesores.html", {"profesores": profesores, "especialidad": especialidad})
    else:
        mensaje = "No ha ingresado ningún valor"
        return render(request, "plantillas/profesores.html", {"mensaje": mensaje})

class CursoListView(LoginRequiredMixin,ListView):
    model=Curso
    context_object_name="cursos"  #nombre que le llega a template_name (para trabajar el for en html)
    template_name="plantillas/cursos.html"
class CursoDetalView(LoginRequiredMixin,DetailView):
    model=Curso
    template_name="plantillas/curso_detalle.html"
class CursoCreateView(LoginRequiredMixin,CreateView):
    model=Curso
    template_name="plantillas/curso_crear.html"
    success_url = reverse_lazy ('cursos')
    fields=['nombre','comision','autor','fecha']
class CursoUpdateView(LoginRequiredMixin,UpdateView):
    model=Curso
    template_name="plantillas/curso_editar.html"
    success_url=reverse_lazy('cursos')
    fields=['nombre',"comision",'fecha']
    def test_func(self):
        return self.request.user.is_superuser
class CursoDeleteView(LoginRequiredMixin,DeleteView):
    model=Curso
    template_name="plantillas/curso_borrar.html"
    success_url=reverse_lazy('cursos')
    def test_func(self):
        return self.request.user.is_superuser

class ProfesoresLista(LoginRequiredMixin,ListView):
    model=Profesor
    context_object_name="profesores"  #nombre que le llega a template_name (para trabajar el for en html)
    template_name="plantillas/profesores.html"
class ProfesoresDetalles(LoginRequiredMixin,DetailView):
    model=Profesor
    template_name="plantillas/profesores_detalle.html"
class ProfesoresCrear(LoginRequiredMixin,CreateView):
    model=Profesor
    template_name="plantillas/profesores_crear.html"
    success_url = reverse_lazy ('profesores')
    fields=['nombre','apellido','email','especialidad','autor','fecha']
class ProfesoresEditar(LoginRequiredMixin,UpdateView):
    model=Profesor
    template_name="plantillas/profesores_editar.html"
    success_url=reverse_lazy('profesores')
    fields=['nombre','apellido','email','especialidad','fecha']
    def test_func(self):
        return self.request.user.is_superuser
class ProfesoresBorrar(LoginRequiredMixin,DeleteView):
    model=Profesor
    template_name="plantillas/profesores_borrar.html"
    success_url=reverse_lazy('profesores')
    def test_func(self):
        return self.request.user.is_superuser

class EstudiantesLista(LoginRequiredMixin,ListView):
    model=Estudiante
    context_object_name="estudiantes"  #nombre que le llega a template_name (para trabajar el for en html)
    template_name="plantillas/estudiantes.html"
class EstudiantesDetalles(LoginRequiredMixin,DetailView):
    model=Estudiante
    template_name="plantillas/estudiantes_detalle.html"
class EstudiantesCrear(LoginRequiredMixin,CreateView):
    model=Estudiante
    template_name="plantillas/estudiantes_crear.html"
    success_url = reverse_lazy ('estudiantes')
    fields=['nombre','apellido','curso','email','autor','fecha']
class EstudiantesEditar(LoginRequiredMixin,UpdateView):
    model=Estudiante
    template_name="plantillas/estudiantes_editar.html"
    success_url=reverse_lazy('estudiantes')
    fields=['nombre','apellido','curso','email','fecha']
class EstudiantesBorrar(LoginRequiredMixin,DeleteView):
    model=Estudiante
    template_name="plantillas/estudiantes_borrar.html"
    success_url=reverse_lazy('estudiantes') 
