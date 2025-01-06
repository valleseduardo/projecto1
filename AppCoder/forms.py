from django import forms
from .models import Estudiante, Profesor, Curso

class EstudianteForm(forms.ModelForm):
    class Meta:
        model= Estudiante
        fields= ["nombre", "apellido", "email"]


class ProfesorForm(forms.ModelForm):
    class meta:
        model=Profesor
        fields=["nombre", "apellido", "email", "profesion"]


class CursoForm(forms.ModelForm):
    class meta:
        model=Curso
        fields=["nombre", "camada"]