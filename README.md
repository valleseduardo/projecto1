1. Configuración Inicial
1.1 Crear un nuevo proyecto Django:

Bash

django-admin startproject MiProyecto1
1.2 Crear las aplicaciones:

Bash

cd MiProyecto1
python manage.py startapp AppCoder
python manage.py startapp AppNuevo
python manage.py startapp AppBlog
2. Configuración de settings.py
Agregar aplicaciones: En MiProyecto1/settings.py, agrega las nuevas aplicaciones a la lista INSTALLED_APPS:
<!-- end list -->

Python

INSTALLED_APPS = [
    # ...
    'AppCoder',
    'AppNuevo',
    'AppBlog',
]
3. Creación de Modelos
3.1 Definir modelos en models.py:

Cada aplicación tendrá su propio archivo models.py. Por ejemplo, en AppCoder/models.py:

Python

from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
3.2 Realizar migraciones:

Bash

python manage.py makemigrations
python manage.py migrate
4. Creación de Vistas
4.1 Definir vistas en views.py:

Python

from django.shortcuts import render
from .models import Estudiante

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'AppCoder/estudiantes.html', {'estudiantes': estudiantes})
4.2 Configurar URLs en urls.py:

Python

from django.urls import path
from . import views

urlpatterns = [
    path('estudiantes/', views.lista_estudiantes, name='lista_estudiantes'),
]
5. Creación de Plantillas
Crear las plantillas HTML en la carpeta templates/AppCoder. Por ejemplo, estudiantes.html para mostrar la lista de estudiantes.
6. Subir a GitHub
6.1 Inicializar repositorio:

Bash

cd MiProyecto1
git init
git add .
git commit -m "Primer commit"
6.2 Crear un repositorio remoto en GitHub:

Sigue las instrucciones de GitHub para crear un nuevo repositorio.

6.3 Conectar el repositorio local con el remoto:

Bash

git remote add origin https://github.com/tu_usuario/MiProyecto1.git
6.4 Subir los cambios:

Bash

git push -u origin main
Explicación de las Transacciones
makemigrations: Genera un archivo de migración que describe los cambios realizados en los modelos.
migrate: Aplica los cambios descritos en las migraciones a la base de datos.
Consideraciones Adicionales:


Autor
Eduardo Valles