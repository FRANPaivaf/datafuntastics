from django.urls import path
from . import views

urlpatterns = [
    path("", views.v_index, name="v_index"),
    path("reporte_pdf", views.v_reporte_pdf, name="v_reporte_pdf"),
    path("data_analitica", views.v_data_analitica, name="v_data_analitica"),
    path("data_frames", views.v_data_frames, name="v_data_frames"),
    path("servicios", views.v_servicios, name="v_servicios"),
]