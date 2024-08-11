from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from formularios.models import Profesor

class EliminarProfesor(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")  # crear usuario de prueba
        self.client = Client()
        self.client.login(username="testuser", password="12345")
        self.profesor = Profesor.objects.create(
            nombre="Juan",
            apellido="Gomez",
            email="a@ejemplo.com",
            especialidad="codigo"
        )
        self.url = reverse("ProfesoresBorrar", args=[self.profesor.id])  # path de urls.py
    def test_eliminar_profesor(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "plantillas/profesores_borrar.html")
        self.client.post(self.url)
        self.assertQuerysetEqual(Profesor.objects.all(), [])

