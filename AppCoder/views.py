from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
from django.shortcuts import render, get_object_or_404

from .models import Estudiante, Profesor, Curso
from django.db.models import Q

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
#----------------------------INDEX-------------------------------------------
def index(request):
    return render(request, "AppCoder/index.html")


#----------------------------ESTUDIANTE-------------------------------------------
def cargar_estudiante(request):
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_estudiantes")
    else:
        form= EstudianteForm()
    return render(request, "AppCoder/estudiante_form.html", {"form" : form})

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, "AppCoder/lista_estudiantes.html", {"estudiantes": estudiantes})



#----------------------------PROFESOR-------------------------------------------

def cargar_profesor(request):
    if request.method == "POST":
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_profesores")
            
    else:
        form= ProfesorForm()
    return render(request, "AppCoder/profesor_form.html", {"form" : form})

def lista_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, "AppCoder/lista_profesores.html", {"profesores": profesores})


    #----------------------------CURSO-------------------------------------------

def cargar_curso(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_cursos")
    else:
        form= CursoForm()
    return render(request, "AppCoder/curso_form.html", {"form" : form})

def lista_cursos(request):
    curso = Curso.objects.all()
    return render(request, "AppCoder/lista_cursos.html", {"cursos": curso})



    #----------------------------BUSQUEDA-------------------------------------------

def buscar(request):
    query = request.GET.get('q', '')
    resultados = []

    if query:
        estudiantes = Estudiante.objects.filter(
            Q(nombre__icontains=query) | Q(apellido__icontains=query) | Q(email__icontains=query)
        )
        profesores = Profesor.objects.filter(
            Q(nombre__icontains=query) | Q(apellido__icontains=query) | Q(email__icontains=query) | Q(profesion__icontains=query)
        )

        for estudiante in estudiantes:
            resultados.append({
                'tipo': 'Estudiante',
                'nombre': estudiante.nombre,
                'apellido': estudiante.apellido,
                'email': estudiante.email,
                'extra': '-',
            })

        for profesor in profesores:
            resultados.append({
                'tipo': 'Profesor',
                'nombre': profesor.nombre,
                'apellido': profesor.apellido,
                'email': profesor.email,
                'extra': f'{profesor.profesion}',
            })

    return render(request, 'AppCoder/index.html', {'resultados': resultados})



 #----------------------------REGISTRO DE USUARIOS-------------------------------------------

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado exitosamente. ¡Ahora puedes iniciar sesión!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'AppCoder/register.html', {'form': form})



 #----------------------------EDICION DE USUARIOS-------------------------------------------


@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=usuario)
        if profile_form.is_valid():
            informacion= profile_form.cleaned_data

            usuario.email= informacion["email"]
            usuario.first_name= informacion["first_name"]
            usuario.last_name= informacion["last_name"]

            if informacion.get("password1") and informacion["password1"]== informacion["password2"]:
                usuario.set_password(informacion["password1"])

            usuario.save()

            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('index')
    else:
        user_form = UserEditForm(instance=usuario)

    return render(request, "AppCoder/editarPerfil.html", {
        "user_form": user_form,
        "usuario": usuario
    })
