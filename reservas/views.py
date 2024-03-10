from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Mesa, Cliente
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
@login_required
def index(request):
    return render(request, "reservas/index.html")


def seleccion(request):
    disponibles = mesas_disponibles()
    return render(request, "reservas/seleccion.html", {
        "mesas": disponibles,
    })

def reservar_mesa(request):
    if request.method == "POST":
        id_mesa = int(request.POST.get("mesa"))
        #agregar mesa a cliente y cambiar estado de mesa a Ocupado
        try:
            mesa = Mesa.objects.get(id=id_mesa)
            mesa.ocupado = True
            mesa.descripcion = str(request.POST.get("descripcion"))
            mesa.cliente = request.user.cliente
            mesa.save()
            return render(request, "reservas/index.html", {'success_message': 'Reserva realizada con éxito.'})
        except Mesa.DoesNotExist:
            return HttpResponseRedirect(reverse("index"))
        
#Cambia la descripción de la mesa.
def modificar(request):
    mesascliente = mesas_cliente(request.user.cliente.id)
    return render(request, "reservas/modificar.html", {
        "mesas": mesascliente 
    })

def baja(request):
    mesascliente = mesas_cliente(request.user.cliente.id)
    return render(request, "reservas/baja.html", {
        "mesas": mesascliente
    })

def baja_reserva(request):
    if request.method == "POST":
        mesa_id = request.POST.get('mesa_id')
        mesa = Mesa.objects.get(id=mesa_id)
        mesa.descripcion = ""
        mesa.cliente = None
        mesa.ocupado = False
        mesa.save()
        return render(request, "reservas/index.html", {'success_message': 'Reserva dada de baja con éxito.'})  #Falta hacer comentarios de exito, o alert

#devuelve todas las mesas que contienen al cliente
def mesas_cliente(id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    mesas = Mesa.objects.all()
    mesas_del_cliente = []
    for mesa in mesas:
        if mesa.cliente == cliente:
            mesas_del_cliente.append(mesa)
    return mesas_del_cliente

#devuelve todas las mesas libres
def mesas_disponibles():
    mesas = Mesa.objects.all()
    disponibles = []
    for mesa in mesas:
        if not mesa.ocupado:
            disponibles.append(mesa)
    return disponibles

def modificar_reserva(request):#esta mal todavia
    if request.method == "POST":
        mesa_id = request.POST.get('mesa_id')
        mesa = Mesa.objects.get(id=mesa_id)
        return render(request, "reservas/modificar_reserva.html", {
        "mesa": mesa
    })
            
def modificar_descripcion(request):
    if request.method == "POST":
        mesa_id = request.POST.get('mesa_id')
        descripcion = request.POST.get('text')
        mesa = Mesa.objects.get(id=mesa_id)
        mesa.descripcion = descripcion
        mesa.save()
        return render(request, "reservas/index.html", {'success_message': 'Reserva modificada con éxito.'}) 
    
