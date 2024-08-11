from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class Curso(models.Model):                  
    nombre=models.CharField(max_length=30) 
    comision=models.IntegerField()
    autor=models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    fecha=models.DateField(null=True)    
    def __str__(self):
        return f"{self.nombre} {self.comision}"

class Estudiante(models.Model): 
    solo_letras = RegexValidator(r'^[a-zA-Záéíóúñ]+$', 'No se permiten números.')
    nombre=models.CharField(max_length=30, validators=[solo_letras])
    apellido=models.CharField(max_length=30, validators=[solo_letras])
    curso=models.CharField(max_length=30, null=True)    
    email=models.EmailField()   
    autor=models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    fecha=models.DateField(null=True)                 
    def __str__(self):
        return f"{self.nombre} {self.apellido} -{self.curso} - {self.email}"

class Profesor(models.Model):
    solo_letras = RegexValidator(r'^[a-zA-Záéíóúñ]+$', 'No se permiten números.')
    nombre=models.CharField(max_length=30, validators=[solo_letras])
    apellido=models.CharField(max_length=30, validators=[solo_letras])
    email=models.EmailField()
    especialidad=models.CharField(max_length=30)
    autor=models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    fecha=models.DateField(null=True)  
    def __str__(self):
        return f"{self.nombre} {self.apellido} -{self.especialidad} - {self.email}"


