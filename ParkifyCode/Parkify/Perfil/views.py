from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Usuario
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def login_usuario(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if email.endswith('@eafit.edu.co'):
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard_usuario')
            else:
                messages.error(request, 'Credenciales inválidas, por favor intente de nuevo')
    return render(request, 'login.html')


def registro_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'El nombre de usuario ya está en uso')
                return redirect('registro_usuario')
            else:
                if email.endswith('@eafit.edu.co'):
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    user.save()
                    messages.success(request, 'Registro completado exitosamente')
                    return redirect('dashboard_usuario')
                else:
                    messages.error(request, 'El correo electrónico no es institucional')
                    return redirect('registro_usuario')
        else:
            messages.error(request, 'Las contraseñas no coinciden')
            return redirect('registro_usuario')
    return HttpResponse('')



def dashboard_usuario(request):
    user = request.user
    context = {'user': user}
    return render(request, 'dashboard.html', context)


def logout_usuario(request):
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente')
    return redirect('login_usuario')


def index(request):
    return render(request, 'index.html')
