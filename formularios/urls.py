from django.urls import path
from formularios.views import *
urlpatterns = [
    path('', inicio,name="inicio"),
    path('about', about,name="about"),

    path('buscarCurso/',buscarCurso,name="buscarCurso"),
    path('buscarProfesor/',buscarProfesor,name="buscarProfesor"),
    path('buscarEstudiante/',buscarEstudiante,name="buscarEstudiante"),


    path('Cursos/',CursoListView.as_view(),name="cursos"), 
    path('CrearCurso/',CursoCreateView.as_view(),name="CrearCurso"), 
    path('DetalleCurso/<pk>/',CursoDetalView.as_view(),name="DetalleCurso"), 
    path('EditarCurso/<pk>/',CursoUpdateView.as_view(),name="EditarCurso"), 
    path('EliminarCurso/<pk>/',CursoDeleteView.as_view(),name="BorrarCurso"), 

    path('profesores/',ProfesoresLista.as_view(),name="profesores"), 
    path('ProfesoresCrear/',ProfesoresCrear.as_view(),name="ProfesoresCrear"), 
    path('ProfesoresDetalles/<pk>/',ProfesoresDetalles.as_view(),name="ProfesoresDetalles"), 
    path('ProfesoresEditar/<pk>/',ProfesoresEditar.as_view(),name="ProfesoresEditar"), 
    path('ProfesoresBorrar/<pk>/',ProfesoresBorrar.as_view(),name="ProfesoresBorrar"), #pk es que la vista neceista un id

    path('estudiantes/',EstudiantesLista.as_view(),name="estudiantes"), 
    path('EstudiantesCrear/',EstudiantesCrear.as_view(),name="EstudiantesCrear"), 
    path('EstudiantesDetalles/<pk>/',EstudiantesDetalles.as_view(),name="EstudiantesDetalles"), 
    path('EstudiantesEditar/<pk>/',EstudiantesEditar.as_view(),name="EstudiantesEditar"), 
    path('EstudiantesBorrar/<pk>/',EstudiantesBorrar.as_view(),name="EstudiantesBorrar"), 

]
