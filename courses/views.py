from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from reportlab.pdfgen import canvas
from reportlab.platypus import Table
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib import colors
from django.views.generic.detail import DetailView
from django.conf import settings
from io import BytesIO
from reportlab.pdfgen import canvas
from django.views.generic import View
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Course

class ReportePDF(View):  
     
    def cabecera(self, pdf):
        
        #cabecera con los titulos a aparecer
        pdf.setFont("Helvetica", 16)
        pdf.drawString(230, 790, u"****** CRUD ******")
        pdf.setFont("Helvetica", 14)
        pdf.drawString(230, 770, u"  ****  REPORTE **** ")

        #Cabecera con una fecha 
        pdf.setFont('Helvetica-Bold', 12)
        pdf.drawString(480,750,'24/03/2017')
        pdf.line(460,747,560,747)  

  
    def tabla(self,pdf,y):
        #Creamos una tupla de encabezados para neustra tabla
        encabezados = ('Nombre', 'Fecha inicio', 'Fecha fin','nombre de Imagen')
        #Creamos una lista de tuplas que van a contener los cursos 
        #para agregar la imagen se coloca la importacion de Image
        #se agrega imagen(cource.picture, width: 500, height: 200)
        detalles = [(course.name, course.start_date, course.end_date, course.picture) for course in Course.objects.all()]
        #detalles = [(name,start_date, end_date)]
        detalle_orden = Table([encabezados] + detalles, colWidths=[40 , 150 , 150 ,150])
        #Aplicamos estilos a las celdas de la tabla
        detalle_orden.setStyle(TableStyle(
            [
                #La primera fila(encabezados) va a estar centrada
                ('ALIGN',(0,0),(0,0),'CENTER'),
                ('GRID', (0, 0), (-1, -1), 1, colors.red), 
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]
        ))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 60,y)

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='application/pdf')
        #con esta linea podemos desacargar el pdf con el nombre que se coloque
        response['Content-Disposition'] = 'attachment; filename=Reporte-Crud.pdf'

        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        self.cabecera(pdf)
        y = 600
        self.tabla(pdf, y)
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response


class CourseList(ListView):
    model = Course
class CourseDetail(DetailView):
    model = Course
class CourseCreation(CreateView):
    model = Course
    success_url = reverse_lazy('courses:list')
    fields = ['name', 'start_date', 'end_date', 'picture']
class CourseUpdate(UpdateView):
    model = Course
    success_url = reverse_lazy('courses:list')
    fields = ['name', 'start_date', 'end_date', 'picture']
class CourseDelete(DeleteView):
    model = Course
    success_url = reverse_lazy('courses:list')

