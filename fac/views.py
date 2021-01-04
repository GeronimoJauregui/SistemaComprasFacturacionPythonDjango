from django.shortcuts import render
from django.views import generic

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse

from .models import Cliente
from .forms import ClienteForm

from bases.views import SinPrivilegios

#CRUD DE CLIENTES#
class ClienteView(SinPrivilegios, generic.ListView):
    permission_required = "fac.view_cliente"
    model = Cliente #Modelo a mostrar
    template_name = "cmp/cliente_list.html"
    context_object_name = "obj"

class VistaBaseCreate(SuccessMessageMixin,SinPrivilegios, generic.CreateView):
    context_object_name = "obj"
    success_message= "Registro agregado satisfactoriamente!"

    def form_valid(self, form):
        form.instance.uc = self.request.user #agrega el id del usuario que esta logueado en uc.
        return super().form_valid(form)

class VistaBaseEdit(SuccessMessageMixin,SinPrivilegios, generic.UpdateView):
    context_object_name = "obj"
    success_message= "Registro actualizado satisfactoriamente!"

    def form_valid(self, form):
        form.instance.um = self.request.user.id #agrega el id del usuario que esta logueado en uc.
        return super().form_valid(form)

class ClienteNew(VistaBaseCreate):
    model = Cliente
    template_name = "fac/cliente_form.html"
    form_class = ClienteForm
    success_url = reverse_lazy("fac:cliente_list")
    permission_required="fac.add_cliente"

class ClienteEdit(VistaBaseEdit):
    model = Cliente
    template_name = "fac/cliente_form.html"
    form_class = ClienteForm
    success_url = reverse_lazy("fac:cliente_list")
    permission_required="fac.change_cliente"

@login_required(login_url='/login/')
@permission_required("fac.change_cliente", login_url='/login/')
def ClienteInactivar(request,id):
    cliente = Cliente.objects.filter(pk=id).first()

    if request.method=='POST':
        if cliente: 
            cliente.estado = not cliente.estado
            cliente.save()
            return HttpResponse('ok')
        return HttpResponse("FAIL")
    return render("FAIL")
