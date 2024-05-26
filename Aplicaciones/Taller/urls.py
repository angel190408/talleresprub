from django.urls import path
from . import views

urlpatterns = [
    path('', views.talleres),
    path('alumnos/', views.alumnos),
    path('inscripcionTaller/', views.inscripcionTaller),
    path('inscripcionDirecta/<tallerPk>', views.inscripcionDirecta),
    path('inscribirAlumno/', views.inscribirAlumno),
    path('generarDocumento/<inscripcionPk>', views.generarDocumento),
    path('eliminarAlumno/<inscripcionPk>', views.eliminarAlumno), 
]