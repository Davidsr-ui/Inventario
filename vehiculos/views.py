from django.shortcuts import render, redirect, get_object_or_404
from .models import Vehiculo, TipoVehiculo
from .forms import VehiculoForm, TipoVehiculoForm


# =========================
# HOME
# =========================

def inicio(request):
    vehiculos = Vehiculo.objects.all()

    return render(request, 'vehiculos/inicio.html', {
        'vehiculos': vehiculos
    })


# =========================
# CRUD TIPOS
# =========================

def lista_tipos(request):
    tipos = TipoVehiculo.objects.all()

    return render(request, 'tipos/lista.html', {
        'tipos': tipos
    })


def crear_tipo(request):
    form = TipoVehiculoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('lista_tipos')

    return render(request, 'tipos/form.html', {
        'form': form,
        'titulo': 'Crear Tipo'
    })


def editar_tipo(request, id):
    tipo = get_object_or_404(TipoVehiculo, id=id)

    form = TipoVehiculoForm(
        request.POST or None,
        request.FILES or None,
        instance=tipo
    )

    if form.is_valid():
        form.save()
        return redirect('lista_tipos')

    return render(request, 'tipos/form.html', {
        'form': form,
        'titulo': 'Editar Tipo'
    })


def eliminar_tipo(request, id):
    tipo = get_object_or_404(TipoVehiculo, id=id)
    tipo.delete()

    return redirect('lista_tipos')


# =========================
# CRUD VEHICULOS
# =========================

def lista_vehiculos(request):

    vehiculos = Vehiculo.objects.all()

    return render(request,
                  'vehiculos/lista.html',
                  {'vehiculos': vehiculos})


def crear_vehiculo(request):
    form = VehiculoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('lista_vehiculos')

    return render(request, 'vehiculos/form.html', {
        'form': form,
        'titulo': 'Crear Vehículo'
    })


def editar_vehiculo(request, id):
    vehiculo = get_object_or_404(Vehiculo, id=id)

    form = VehiculoForm(
        request.POST or None,
        request.FILES or None,
        instance=vehiculo
    )

    if form.is_valid():
        form.save()
        return redirect('lista_vehiculos')

    return render(request, 'vehiculos/form.html', {
        'form': form,
        'titulo': 'Editar Vehículo'
    })


def eliminar_vehiculo(request, id):
    vehiculo = get_object_or_404(Vehiculo, id=id)
    vehiculo.delete()

    return redirect('lista_vehiculos')