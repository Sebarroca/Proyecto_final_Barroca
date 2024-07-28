from django.db import models

class Curso(models.Model):                  
    nombre=models.CharField(max_length=30) 
    comision=models.IntegerField()


class Estudiante(models.Model): 
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    curso=models.CharField(max_length=30, null=True)    
    email=models.EmailField()                  

class Profesor(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
    especialidad=models.CharField(max_length=30)

