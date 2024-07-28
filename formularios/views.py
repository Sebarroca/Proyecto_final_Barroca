from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *

# Create your views here.

def inicio(request):
    cursos = Curso.objects.all()
    profesores = Profesor.objects.all()
    estudiantes = Estudiante.objects.all()
    return render(request,"plantillas/inicio.html",{"cursos": cursos, "profesores": profesores, "estudiantes": estudiantes})

def cursos(request):
    if request.method == "POST":
            miFormulario = CursoForm(request.POST) 
            if miFormulario.is_valid():   
                informacion = miFormulario.cleaned_data
                curso = Curso(nombre=informacion["nombre"], comision=informacion["comision"]) 
                curso.save()
            
                return render(request, "plantillas/cursos.html")
    else:
            miFormulario = CursoForm() 
    return render(request, "plantillas/cursos.html", {"miFormulario": miFormulario})

def estudiantes(request):
    if request.method == "POST":
            miFormulario = EstudianteForm(request.POST) 
            if miFormulario.is_valid():   
                informacion = miFormulario.cleaned_data
                curso = Estudiante(nombre=informacion["nombre"], apellido=informacion["apellido"], curso=informacion["curso"], email=informacion["email"]) 
                curso.save()
                return render(request, "plantillas/estudiantes.html")
    else:
            miFormulario = EstudianteForm() 
    return render(request, "plantillas/estudiantes.html", {"miFormulario": miFormulario})

def profesores(request):
    if request.method == "POST":
            miFormulario = ProfesorForm(request.POST) 
            if miFormulario.is_valid():   
                informacion = miFormulario.cleaned_data
                curso = Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], especialidad=informacion["especialidad"]) 
                curso.save()
                return render(request, "plantillas/profesores.html")
    else:
            miFormulario = ProfesorForm() 
    return render(request, "plantillas/profesores.html", {"miFormulario": miFormulario})

def buscarCurso(request):
    comision = request.GET.get('comision')
    nombre = request.GET.get('nombre')
    if comision and nombre:
        cursos = Curso.objects.filter(comision=comision, nombre__icontains=nombre)
        return render(request, "plantillas/inicio.html", {"cursos": cursos, "comision": comision, "nombre": nombre})
    elif comision:
        cursos = Curso.objects.filter(comision=comision)
        return render(request, "plantillas/inicio.html", {"cursos": cursos, "comision": comision})
    elif nombre:
        cursos = Curso.objects.filter(nombre__icontains=nombre)
        return render(request, "plantillas/inicio.html", {"cursos": cursos, "nombre": nombre})
    else:
        return render(request,"plantillas/inicio.html")
    
def buscarEstudiante(request):
    apellido=request.GET.get('apellido')
    if apellido:
        estudiantes=Estudiante.objects.filter(apellido__iexact=apellido)
        return render(request,"plantillas/inicio.html",{"estudiantes":estudiantes,"apellido":apellido}   )
    else:
        return render(request,"plantillas/inicio.html")


def buscarProfesor(request):
    apellido = request.GET.get('apellido')
    especialidad = request.GET.get('especialidad')
    if apellido and especialidad:
        profesor = Profesor.objects.filter(apellido__icontains=apellido, especialidad__icontains=especialidad)
        return render(request, "plantillas/inicio.html", {"profesor": profesor, "apellido": apellido, "especialidad": especialidad})
    elif apellido:
        profesor = Profesor.objects.filter(apellido__icontains=apellido)
        return render(request, "plantillas/inicio.html", {"profesor": profesor, "apellido": apellido})
    elif especialidad:
        profesor = Profesor.objects.filter(especialidad__icontains=especialidad)
        return render(request, "plantillas/inicio.html", {"profesor": profesor, "especialidad": especialidad})
    else:
        return render(request,"plantillas/inicio.html")