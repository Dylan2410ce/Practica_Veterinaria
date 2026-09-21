Sistema de Gestión Veterinaria

Proyecto de IF0009 Desarrollo de Software IV

Sistema desarrollado con Django y Django REST Framework para gestionar propietarios, mascotas y consultas veterinarias.

Instalación
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate

Ejecución
python manage.py runserver

Pruebas
python manage.py test


Incluye CRUD, validaciones, filtros, paginación, autenticación, permisos y sesiones.
