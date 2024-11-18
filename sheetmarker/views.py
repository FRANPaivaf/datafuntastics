from django.http import HttpResponse
from django.shortcuts import render
import datetime
from openpyxl import Workbook

static_values = {
    "direccion": "las flores 343434 | Concepcion",
    "telefono": "+56 37490116",
    "email": "francisca.paiva@gmail.com",
    "whatsapp": "+56937490117",
    "ig": "https://www.instagram.com/natgeoanimals/"
}
# Create your views here.
def v_index(request):
    return HttpResponse("sheetmarker index")

def v_macros(request):
    context = {
    "static_values": static_values,
    "features": [ "Soporta xls, xlsx, formatos libres.",
        "Permite importar, modificar y exportar",
        "cantidad de ejecuciones ilimitadas.",

        ] }

    """ opcion 1 contex ={
    "static_values": static_values,
    "feat1": "Soporta xls, xlsx, formatos libres.",
    "feat2": "Permite importar, modificar y exportar"
    ",
    "feat3": "cantidad de ejecuciones ilimitadas.", }"""
   
    return render(request, "sheetmarker/macros.html", context)

def v_powerbi(request):
    context = {
        "static_values": static_values,
        "features": ["Caract1", "Caract2",] 
    }
    return render(request, "sheetmarker/powerbi.html", context)

def v_analitica(request):
    context = {
    "static_values": static_values,
    "promos": [
        {
        "title": "10% Off",
        "color": "bg-primary",
        "rules": ["Regla 1", "Regla 2"]

        },
        {"title": "30% Off", "color": "bg-success"},
        {"title": "50% Off", "color": "bg-danger"}
        ]
 }
    return render(request, "sheetmarker/analitica.html", context)

def v_reporte_xls(request):
    # Crear un libro de Excel
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "Reporte de Ejemplo"

    # Agregar encabezados
    encabezados = ["ID", "Nombre", "Fecha"]
    worksheet.append(encabezados)

    # Agregar algunos datos de ejemplo
    datos = [
        [1, "Alice", datetime.date(2023, 11, 5)],
        [2, "Bob", datetime.date(2023, 11, 6)],
        [3, "Charlie", datetime.date(2023, 11, 7)],
    ]

    for fila in datos:
        worksheet.append(fila)

    # Preparar la respuesta HTTP con el archivo Excel
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = "attachment; filename=reporte.xlsx"

    # Guardar el libro en la respuesta
    workbook.save(response)
    return response