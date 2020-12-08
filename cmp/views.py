from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic
from .models import Proveedor
from .forms import ProveedorForm
from django.urls import reverse_lazy
#Para ocupar ajax en la vista.
from django.http import HttpResponse
import json
from bases.views import SinPrivilegios
#CRUD DE PROVEEDORES#
class ProveedorView(LoginRequiredMixin, SinPrivilegios, generic.ListView):
    permission_required = "cmp.view_proveedor"
    model = Proveedor #Modelo a mostrar
    template_name = "cmp/proveedor_list.html"
    context_object_name = "obj"
    login_url = "bases:login"

class ProveedorNew(LoginRequiredMixin, SinPrivilegios, generic.CreateView):
    permission_required = "cmp.add_proveedor"
    model = Proveedor
    template_name = 'cmp/proveedor_form.html'
    context_object_name = "obj"
    form_class = ProveedorForm
    success_url = reverse_lazy("cmp:proveedor_list") #Lugar de redirección al dar summit
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user #agrega el id del usuario que esta logueado en uc.
        print(self.request.user.id)
        return super().form_valid(form)

class ProveedorEdit(LoginRequiredMixin, SinPrivilegios, generic.UpdateView):
    permission_required = "cmp.change_proveedor"
    model = Proveedor
    template_name = 'cmp/proveedor_form.html'
    context_object_name = "obj"
    form_class = ProveedorForm
    success_url = reverse_lazy("cmp:proveedor_list") #Lugar de redirección al dar summit
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id #agrega el id del usuario que esta logueado en uc.
        print(self.request.user.id)
        return super().form_valid(form)

def ProveedorInactivar(request,id):
    template_name= 'cmp/inactivar.html'
    contexto={}
    prv = Proveedor.objects.filter(pk=id).first()

    if not prv:
        return HttpResponse('Proveedor no existe' + str(id))
    
    if request.method=='GET':
        contexto={'obj':prv}
    
    if request.method=='POST':
        prv.estado = False
        prv.save()
        contexto={'obj':'OK'}
        return HttpResponse('Proveedor inactivado')
    return render(request,template_name,contexto)
