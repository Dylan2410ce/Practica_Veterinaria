from django.urls import path
from . import views

urlpatterns = [
    path('clinica/api/perfil/', views.perfil, name='perfil'),

    path('clinica/api/mascotas/',views.api_mascotas,name='api_mascotas'),

    path('clinica/api/mascotas/<int:pk>/',views.detalle_mascotas, name='detalle_mascotas'),

    path('clinica/api/propietarios/',views.api_propietarios,name='api_propietarios'),

    path('clinica/api/consultas/',views.api_consultas,name='api_consultas'),

    path('clinica/api/estadisticas/',views.estadisticas,name='estadisticas'),

    path('clinica/api/sesion/',views.sesion,name='sesion'),
]
