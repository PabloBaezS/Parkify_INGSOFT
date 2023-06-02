# Importaciones necesarias
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import ensure_csrf_cookie

from .forms import SignUpForm, VehiculoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario\


def registro_usuario(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user = form.save()
            login(request, user)
            return render(request,'dashboard.html')
    else:
        form = SignUpForm()
    return render(request, 'registro.html', {'form': form})

@login_required
def logoutAccount(request):
    logout(request)
    return render(request, 'index.html')


@ensure_csrf_cookie
def loginAccount(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'dashboard.html')
        else:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')


def dashboard_usuario(request):
    # Obtener el usuario actual desde la base de datos
    user = Usuario.objects.get(pk=request.user.pk)

    # Renderizar la plantilla con la información del usuario
    return render(request, 'dashboard.html')


def index(request):
    return render(request, 'index.html')


def vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            vehiculo = form.save(commit=False)
            vehiculo.idUsuario = request.user.usuario
            vehiculo.save()
            return redirect('home')
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo.html', {'form': form})


def about(request):
    return render(request, 'about.html')

def parkify(request):
    return render(request, 'parkify.html')



