from django.shortcuts import render
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4 


# Create your views here.

def v_index(request):
    return HttpResponse("Librarium index")

def v_reporte_pdf(request): #<----- View
    # Crear la respuesta HTTP con el tipo de contenido para PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'

    # Crear el objeto canvas de ReportLab para generar el PDF
    p = canvas.Canvas(response, pagesize=A4)
    ancho, alto = A4  # Tamaño de la página

    # Agregar contenido al PDF
    p.setFont("Helvetica", 12)
    p.drawString(100, alto - 100, "Hola, este es un PDF generado desde Django.")
    p.drawString(100, alto - 120, "Puedes personalizar este contenido como desees.")

    # Finalizar y cerrar el PDF
    p.showPage()
    p.save()

    return response