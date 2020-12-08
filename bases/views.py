from django.shortcuts import render
from django.views import generic #Acceso a los vistas genericas.
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

#Los mixin siempre a la izquierda, para darle prioridad y se ejecuten primero.
class SinPrivilegios(PermissionRequiredMixin):
    raise_exception=False
    redirect_field_name="redirecto_to"

    def handle_no_permission(self):
        from django.contrib.auth.models import AnonymousUser
        if not self.request.user==AnonymousUser():
            self.login_url = 'bases:sin_privilegios'
        return HttpResponseRedirect(reverse_lazy(self.login_url))

class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'bases/home.html'
    login_url='bases:login'  #Lugar de redirección si el usuario no esta autenticado.

class HomeSinPrivilegios(generic.TemplateView):
    template_name = "bases/sin_privilegios.html"