from django.test import TestCase
from django.contrib.auth.models import User

from rest_framework.test import APITestCase

from .models import Propietario
from .serializers import (
    MascotaSerializer,
    ConsultaVeterinariaSerializer
)


class SerializerTest(TestCase):

    def test_mascota_peso_cero_invalido(self):

        data = {
            'nombre': 'Max',
            'especie': 'Perro',
            'raza': 'Labrador',
            'fecha_nacimiento': '2022-05-10',
            'peso': 0,
            'activo': True,
            'propietario': 1
        }

        serializer = MascotaSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn('peso', serializer.errors)


    def test_consulta_costo_negativo_invalido(self):

        data = {
            'mascota': 1,
            'motivo': 'Consulta general',
            'diagnostico': 'Normal',
            'tratamiento': 'Ninguno',
            'costo': -100
        }

        serializer = ConsultaVeterinariaSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn('costo', serializer.errors)


class PerfilTest(APITestCase):

    def setUp(self):

        self.usuario = User.objects.create_user(
            username='usuario',
            password='12345678',
            email='usuario@gmail.com'
        )


    def test_perfil_usuario_anonimo(self):

        response = self.client.get(
            '/clinica/api/perfil/'
        )

        self.assertNotEqual(
            response.status_code,
            200
        )


    def test_perfil_usuario_autenticado(self):

        self.client.force_authenticate(
            user=self.usuario
        )

        response = self.client.get(
            '/clinica/api/perfil/'
        )

        self.assertEqual(
            response.status_code,
            200
        )
