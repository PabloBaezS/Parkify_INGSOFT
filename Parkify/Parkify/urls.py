from django.urls import path
from django.contrib.auth import views as auth_views
from Perfil.views import login_usuario,registro_usuario,dashboard_usuario,logout_usuario, index
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', index, name='index'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login_usuario'),
    path('registro/', registro_usuario, name='registro_usuario'),
    path('dashboard/', dashboard_usuario, name='dashboard_usuario'),
    path('logout/', logout_usuario, name='logout_usuario'),
]

