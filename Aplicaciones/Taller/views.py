from django.shortcuts import render, redirect
from django.http import FileResponse
from .models import *
from django.contrib import messages
from django.contrib.staticfiles.storage import staticfiles_storage

from io import BytesIO
import locale
from datetime import datetime
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Create your views here.

def talleres(request):
    talleres = Taller.objects.all()
    return render(request, "tabs/talleres.html", {"talleres": talleres, "nbar": "talleres"})

def alumnos(request):
    alumnos = AlumnoTaller.objects.all()
    return render(request, "tabs/alumnos.html", {"alumnos": alumnos, "nbar": "alumnos"})

def inscripcionTaller(request):
    # Talleres para seleccion
    talleres = Taller.objects.all()

    # Alumnos para seleccion
    alumnos = Alumno.objects.all()

    return render(request, "forms/inscripcion.html", {"talleres": talleres, "nbar": "inscripcion"})

def inscripcionDirecta(request, tallerPk):
    print("alta directa para taller [{0}]".format(tallerPk))

    # Variable para taller seccionado
    taller = Taller.objects.get(pk = tallerPk)
    
    # Talleres para seleccion
    talleres = Taller.objects.all()

    # Alumnos para seleccion
    alumnos = Alumno.objects.all()

    return render(request, "forms/inscripcion.html", {
        "seleccionTaller": taller,
        "talleres": talleres,
        "nbar": "inscripcion"
        })

def inscribirAlumno(request):
    taller = Taller.objects.get(pk = request.POST["idTaller"])

    alumno = Alumno.objects.create(
        numeroControl = request.POST["numeroControl"], nombreCompleto = request.POST["nombreCompleto"]
    )
    
    AlumnoTaller.objects.create(
        taller = taller,
        alumno = alumno
    )

    return redirect('/alumnos')

def generarDocumento(request, inscripcionPk):
    inscripcion = AlumnoTaller.objects.get(pk = inscripcionPk)
    
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    p.drawString(50, 430, inscripcion.alumno.nombreCompleto)
    p.drawString(50, 400, inscripcion.taller.nombre)
    p.drawString(50, 370, "Tec NM campus Apizaco")
    p.drawString(50, 340, datetime.now().strftime("%d de %B de %Y"))

    p.showPage()
    p.save()
 
    buffer.seek(0)

    return FileResponse(buffer, as_attachment=True, filename=str(inscripcion.alumno.numeroControl) + "-diploma.pdf")


def eliminarAlumno(request, inscripcionPk):
    inscripcion = AlumnoTaller.objects.get(pk = inscripcionPk)
    inscripcion.delete()
    
    messages.success(request, 'Se elimino alumno')

    return redirect('/alumnos')
