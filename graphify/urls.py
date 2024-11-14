from django.urls import path
from . import views

urlpatterns = [
    path("", views.v_index, name = "index"),
    path("reporte_png", views.v_reporte_png, name = "reporte_png"),
    path("lista_reportes", views.v_lista_reportes, name = "lista_reportes"),
    path("lista_imagenes", views.v_lista_imagenes, name = "lista_imagenes"),


]
