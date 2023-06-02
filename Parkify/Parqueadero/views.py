from django.shortcuts import render, redirect
from .forms import ParqueaderoForm, ErrorForm, CeldaForm
from .models import Parqueadero, Error, Celda

def crear_parqueadero(request):
    if request.method == 'POST':
        form = ParqueaderoForm(request.POST)
        if form.is_valid():
            parqueadero = form.save()
            return redirect('detalle_parqueadero', pk=parqueadero.pk)
    else:
        form = ParqueaderoForm()
    return render(request, 'crear_parqueadero.html', {'form': form})

def detalle_parqueadero(request, pk):
    parqueadero = Parqueadero.objects.get(pk=pk)
    return render(request, 'detalle_parqueadero.html', {'parqueadero': parqueadero})

def agregar_error(request, pk):
    parqueadero = Parqueadero.objects.get(pk=pk)
    if request.method == 'POST':
        form = ErrorForm(request.POST)
        if form.is_valid():
            error = form.save()
            parqueadero.errores.add(error)
            return redirect('detalle_parqueadero', pk=pk)
    else:
        form = ErrorForm()
    return render(request, 'agregar_error.html', {'form': form})

def agregar_celda(request):
    if request.method == 'POST':
        form = CeldaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_celdas')
    else:
        form = CeldaForm()
    return render(request, 'agregar_celda.html', {'form': form})

def listar_celdas(request):
    celdas = Celda.objects.all()
    return render(request, 'listar_celdas.html', {'celdas': celdas})


def parqueadero():
    return None