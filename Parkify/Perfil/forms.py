from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from Perfil.models import Usuario


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    phone = forms.CharField(max_length=20)
    homeAddress = forms.CharField(max_length=200)

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class login(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus': True}))

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                "This account is inactive.",
                code='inactive',
            )


class VehiculoForm(forms.Form):
    modelo = forms.CharField(label='Modelo', max_length=50)
    tipo_vehiculo_choices = [('moto', 'Moto'), ('carro', 'Carro')]
    tipo_vehiculo = forms.ChoiceField(choices=tipo_vehiculo_choices, label='Tipo de Vehículo')
    combustible_choices = [('eléctrico', 'Eléctrico'), ('gasolina', 'Gasolina'), ('hibrido', 'Híbrido'), ('otros', 'Otros')]
    combustible = forms.ChoiceField(choices=combustible_choices, label='Combustible')
