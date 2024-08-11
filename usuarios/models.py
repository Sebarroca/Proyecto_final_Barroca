from django.db import models
from django.contrib.auth.models import User



class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #sise borra la cuenta, se borra la imagen asociada    null=True, blank = True
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
    def __str__(self):
        return f"Imagen de {self.user.username}"
        #return f"{self.user} - {self.imagen}"

