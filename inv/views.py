from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin  #Mensajes para vistas basadas en clases
from django.views import generic
from .models import Categoria, SubCategoria, Marca, UnidadMedida, Producto
from .forms import CategoriaForm, SubCategoriaForm, MarcaForm, UnidadMedidaForm, ProductoForm
from django.urls import reverse_lazy
from django.contrib import messages #Mensajes para vistas basadas en funciones

#CRUD DE CATEGORIA#
class CategoriaView(LoginRequiredMixin, generic.ListView):
    model = Categoria #Modelo a mostrar
    template_name = "inv/categoria_list.html"
    context_object_name = "obj"
    login_url = "bases/login"

class CategoriaNew(SuccessMessageMixin,LoginRequiredMixin, generic.CreateView):
    model = Categoria
    template_name = 'inv/categoria_form.html'
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy("inv:categoria_list") #Lugar de redirección al dar summit
    login_url = "bases:login"
    success_message="Categoria creada exitosamente!"

    def form_valid(self, form):
        form.instance.uc = self.request.user #agrega el id del usuario que esta logueado en uc.
        return super().form_valid(form)

class CategoriaEdit(SuccessMessageMixin,LoginRequiredMixin, generic.UpdateView):
    model = Categoria
    template_name = 'inv/categoria_form.html'
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy("inv:categoria_list") #Lugar de redirección al dar summit
    login_url = "bases:login"
    success_message="Categoria editada exitosamente!"

    def form_valid(self, form):
        form.instance.um = self.request.user.id #agrega el id del usuario que esta logueado en uc.
        return super().form_valid(form)

class CategoriaDel(LoginRequiredMixin, generic.DeleteView):
    model=Categoria
    template_name = 'inv/catalogos_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy("inv:categoria_list")

#CRUD DE SUB CATEGORIA#
class SubCategoriaView(LoginRequiredMixin, generic.ListView):
    model = SubCategoria #Modelo a mostrar
    template_name = "inv/subcategoria_list.html"
    context_object_name = "obj"
    login_url = "bases/login"

class SubCategoriaNew(LoginRequiredMixin, generic.CreateView):
    model = SubCategoria
    template_name = 'inv/subcategoria_form.html'
    context_object_name = "obj"
    form_class = SubCategoriaForm
    success_url = reverse_lazy("inv:subcategoria_list") #Lugar de redirección al dar summit
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user #agrega el id del usuario que esta logueado en uc.
        return super().form_valid(form)

class SubCategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    model = SubCategoria
    template_name = 'inv/subcategoria_form.html'
    context_object_name = "obj"
    form_class = SubCategoriaForm
    success_url = reverse_lazy("inv:subcategoria_list") #Lugar de redirección al dar summit
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id #agrega el id del usuario que esta logueado en uc.
        return super().form_valid(form)

class SubCategoriaDel(LoginRequiredMixin, generic.DeleteView):
    model= SubCategoria
    template_name = 'inv/catalogos_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy("inv:subcategoria_list")

#CRUD DE MARCA#
class MarcaView(LoginRequiredMixin, generic.ListView):
    model = Marca #Modelo a mostrar
    template_name = "inv/marca_list.html"
    context_object_name = "obj"
    login_url = "bases/login"
    
class MarcaNew(LoginRequiredMixin, generic.CreateView):
    model = Marca
    template_name = 'inv/marca_form.html'
    context_object_name = "obj"
    form_class = MarcaForm
    success_url = reverse_lazy("inv:marca_list") #Lugar de redirección al dar summit
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user #agrega el id del usuario que esta logueado en uc.
        return super().form_valid(form)

class MarcaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Marca
    template_name = 'inv/marca_form.html'
    context_object_name = "obj"
    form_class = MarcaForm
    success_url = reverse_lazy("inv:marca_list") #Lugar de redirección al dar summit
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id #agrega el id del usuario que esta logueado en uc.
        return super().form_valid(form)

def Marca_Inactivar(request, id):
    marca= Marca.objects.filter(pk=id).first()
    contexto={}
    template_name = 'inv/catalogos_del.html'
    if not marca:
        return redirect("inv:marca_list")

    if request.method == "GET":
        contexto = {'obj': marca}
    
    if request.method== "POST":
        marca.estado = False
        marca.save()
        messages.success(request, 'Marca inactivada.')
        return redirect("inv:marca_list")

    return render(request,template_name,contexto)

#CRUD DE UNIDADES DE MEDIDA#
class UMView(LoginRequiredMixin, generic.ListView):
    model = UnidadMedida #Modelo a mostrar
    template_name = "inv/unidadmedida_list.html"
    context_object_name = "obj"
    login_url = "bases/login"

class UMNew(LoginRequiredMixin, generic.CreateView):
    model = UnidadMedida
    template_name = 'inv/unidadmedida_form.html'
    context_object_name = "obj"
    form_class = UnidadMedidaForm
    success_url = reverse_lazy("inv:unidadesmedida_list") #Lugar de redirección al dar summit
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user #agrega el id del usuario que esta logueado en uc.
        return super().form_valid(form)

class UMEdit(LoginRequiredMixin, generic.UpdateView):
    model = UnidadMedida
    template_name = 'inv/unidadmedida_form.html'
    context_object_name = "obj"
    form_class = UnidadMedidaForm
    success_url = reverse_lazy("inv:unidadesmedida_list") #Lugar de redirección al dar summit
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id #agrega el id del usuario que esta logueado en uc.
        return super().form_valid(form)

def UM_Inactivar(request, id):
    unidad= UnidadMedida.objects.filter(pk=id).first()
    contexto={}
    template_name = 'inv/catalogos_del.html'
    if not unidad:
        return redirect("inv:unidadesmedida_list")

    if request.method == "GET":
        contexto = {'obj': unidad}
    
    if request.method== "POST":
        unidad.estado = False
        unidad.save()
        return redirect("inv:unidadesmedida_list")

    return render(request,template_name,contexto)

#CRUD DE PRODUCTO
class ProductoView(LoginRequiredMixin, generic.ListView):
    model = Producto #Modelo a mostrar
    template_name = "inv/producto_list.html"
    context_object_name = "obj"
    login_url = "bases/login"

class ProductoNew(LoginRequiredMixin, generic.CreateView):
    model = Producto
    template_name = 'inv/producto_form.html'
    context_object_name = "obj"
    form_class = ProductoForm
    success_url = reverse_lazy("inv:producto_list") #Lugar de redirección al dar summit
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user #agrega el id del usuario que esta logueado en uc.
        return super().form_valid(form)

class ProductoEdit(LoginRequiredMixin, generic.UpdateView):
    model = Producto
    template_name = 'inv/producto_form.html'
    context_object_name = "obj"
    form_class = ProductoForm
    success_url = reverse_lazy("inv:producto_list") #Lugar de redirección al dar summit
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id #agrega el id del usuario que esta logueado en uc.
        return super().form_valid(form)

def Producto_Inactivar(request, id):
    produc= Producto.objects.filter(pk=id).first()
    contexto={}
    template_name = 'inv/catalogos_del.html'
    if not produc:
        return redirect("inv:producto_list")

    if request.method == "GET":
        contexto = {'obj': produc}
    
    if request.method== "POST":
        produc.estado = False
        produc.save()
        return redirect("inv:producto_list")

    return render(request,template_name,contexto)