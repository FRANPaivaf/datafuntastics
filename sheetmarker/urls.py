from django.urls import path
from . import views

urlpatterns = [
    path("", views.v_index, name="v_index"),
    path("reporte_xls", views.v_reporte_xls, name="v_reporte_xls")
]