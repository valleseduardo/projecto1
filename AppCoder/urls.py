from django.urls import path
from .views import *
from .views import cargar_estudiante, lista_estudiantes, cargar_profesor, lista_profesores, index, buscar, register, editarPerfil
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", index, name="index"),
    path('cargar_estudiante/', cargar_estudiante, name='cargar_estudiante'),
    path('estudiantes/', lista_estudiantes, name='lista_estudiantes'),
    path("cargar_profesor/", cargar_profesor, name = "cargar_profesor"),
    path("profesores/", lista_profesores, name= "lista_profesores"),
    path("cargar_curso/", cargar_curso, name= "cargar_curso"),
    path("cursos/", lista_cursos, name= "lista_cursos"),
    path('buscar/', buscar, name='buscar'),
    path('login/', LoginView.as_view(template_name="AppCoder/login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(template_name='AppCoder/login.html'), name='login'),
    path('register/', register, name='register'),
    path('editarperfil/', editarPerfil, name='editarperfil'),
    path('about_me/', about_me, name='about_me'),
]

