from django.shortcuts import render
from django.views import generic #Acceso a los vistas genericas.
from django.contrib.auth.mixins import LoginRequiredMixin 

#Los mixin siempre a la izquierda, para darle prioridad y se ejecuten primero.
class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'bases/home.html'
    login_url='bases:login'  #Lugar de redirección si el usuario no esta autenticado.