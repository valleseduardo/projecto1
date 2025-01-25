from django import forms
from .models import Estudiante, Profesor, Curso
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class EstudianteForm(forms.ModelForm):
    class Meta:
        model= Estudiante
        fields= ["nombre", "apellido", "email"]


class ProfesorForm(forms.ModelForm):
    class Meta:
        model=Profesor
        fields=["nombre", "apellido", "email", "profesion"]


class CursoForm(forms.ModelForm):
    class Meta:
        model=Curso
        fields=["nombre", "camada"]



class UserEditForm(UserChangeForm):
    password1 = forms.CharField(label='Nueva contraseña', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password2