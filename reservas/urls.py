from django.urls import path
from . import views

app_name = "reservas"

urlpatterns = [
    path("", views.index, name="index"),
    path("seleccion/", views.seleccion, name="seleccion"),
    path("reservar/", views.reservar_mesa, name="reservar_mesa"),
    path("modificar/", views.modificar, name="modificar"),
    path("baja/", views.baja, name="baja"),
    path("modificar_reserva/", views.modificar_reserva, name="modificar_reserva"),
    path("modificar_descripcion", views.modificar_descripcion, name="modificar_descripcion"),
    path("baja_reserva/", views.baja_reserva, name="baja_reserva"),
    
]
