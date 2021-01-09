from django.shortcuts import render, redirect
from django.views import generic

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from datetime import datetime
from django.contrib import messages

from .models import Cliente, FacturaEnc, FacturaDet
from .forms import ClienteForm

from bases.views import SinPrivilegios

import inv.views as inv
from inv.models import Producto

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

class FacturaView(SinPrivilegios, generic.ListView):
    model = FacturaEnc
    template_name = "fac/factura_list.html"
    context_object_name = "obj"
    permission_required = "fac.view_facturaenc"
    

@login_required(login_url='/login/')
@permission_required("fac.change_facturasenc", login_url='bases:sin_privilegios')
def facturas(request,id=None):
    template_name = 'fac/facturas.html'
    
    detalle = {}
    clientes = Cliente.objects.filter(estado=True)

    if request.method == "GET":
        enc = FacturaEnc.objects.filter(pk=id).first()
        if not enc: 
            encabezado = {
                'id': 0,
                'fecha': datetime.today(),
                'cliente': 0,
                'sub_total': 0.00,
                'descuento': 0.00,
                'total': 0.00
            }
            detalle = None
        else:
            encabezado = {
                'id': enc.id,
                'fecha': enc.fecha,
                'cliente': enc.cliente,
                'sub_total': enc.sub_total,
                'descuento': enc.descuento,
                'total': enc.total
            }
            detalle = FacturaDet.objects.filter(factura=enc)

        contexto={"enc":encabezado,"det":detalle,"clientes":clientes}
    if request.method == "POST":
        cliente = request.POST.get("enc_cliente")
        fecha = request.POST.get("fecha")
        cli = Cliente.objects.get(pk=cliente)

        if not id:
            enc = FacturaEnc(
                cliente = cli,
                fecha = fecha
            )
            if enc:
                enc.save()
                id = enc.id
        else:
            enc = FacturaEnc.objects.filter(pk=id).first()
            if enc:
                enc.cliente = cli
                enc.save()
        
        if not id:
            messages.error(request, 'No puedo continuar, no pude detectar No. de factura')
            return redirect("fac:factura_list")
        
        codigo = request.POST.get("codigo")
        cantidad = request.POST.get("cantidad")
        precio = request.POST.get("precio")
        s_total = request.POST.get("sub_total_detalle")
        descuento = request.POST.get("descuento_detalle")
        total = request.POST.get("total_detalle")

        prod = Producto.objects.get(codigo=codigo)
        det = FacturaDet(
            factura = enc,
            producto = prod,
            cantidad = cantidad,
            precio = precio,
            sub_total = s_total,
            descuento = descuento,
            total = total
        )
        if det:
            det.save()

        return redirect("fac:factura_edit",id=id)

    return render(request,template_name,contexto)


class ProductoView(inv.ProductoView):
    template_name="fac/buscar_producto.html"