from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin  #Mensajes para vistas basadas en clases
from django.views import generic
from .models import Categoria, SubCategoria, Marca, UnidadMedida, Producto
from .forms import CategoriaForm, SubCategoriaForm, MarcaForm, UnidadMedidaForm, ProductoForm
from django.urls import reverse_lazy
from django.contrib import messages #Mensajes para vistas basadas en funciones
from bases.views import SinPrivilegios #clase general para los privilegios(permisos) de todas las clases 
from django.contrib.auth.decorators import login_required, permission_required #Para poder poner privilegios (permisos) a funciones


#CRUD DE CATEGORIA#
class CategoriaView(SinPrivilegios, generic.ListView):
    permission_required = "inv.view_categoria"
    model = Categoria #Modelo a mostrar
    template_name = "inv/categoria_list.html"
    context_object_name = "obj"

class CategoriaNew(SuccessMessageMixin, SinPrivilegios, generic.CreateView):
    permission_required = "inv.add_categoria"
    model = Categoria
    template_name = 'inv/categoria_form.html'
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy("inv:categoria_list") #Lugar de redirección al dar summit
    success_message="Categoria creada exitosamente!"

    def form_valid(self, form):
        form.instance.uc = self.request.user #agrega el id del usuario que esta logueado en uc.
        return super().form_valid(form)

class CategoriaEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
    permission_required = "inv.change_categoria"
    model = Categoria
    template_name = 'inv/categoria_form.html'
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy("inv:categoria_list") #Lugar de redirección al dar summit
    success_message="Categoria editada exitosamente!"

    def form_valid(self, form):
        form.instance.um = self.request.user.id #agrega el id del usuario que esta logueado en uc.
        return super().form_valid(form)

class CategoriaDel(SinPrivilegios, generic.DeleteView):
    permission_required = "inv.delete_categoria"
    model=Categoria
    template_name = 'inv/catalogos_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy("inv:categoria_list")

#CRUD DE SUB CATEGORIA#
class SubCategoriaView(SinPrivilegios, generic.ListView):
    permission_required = "inv.view_subcategoria"
    model = SubCategoria #Modelo a mostrar
    template_name = "inv/subcategoria_list.html"
    context_object_name = "obj"

class SubCategoriaNew(SinPrivilegios, generic.CreateView):
    permission_required = "inv.add_subcategoria"
    model = SubCategoria
    template_name = 'inv/subcategoria_form.html'
    context_object_name = "obj"
    form_class = SubCategoriaForm
    success_url = reverse_lazy("inv:subcategoria_list") #Lugar de redirección al dar summit

    def form_valid(self, form):
        form.instance.uc = self.request.user #agrega el id del usuario que esta logueado en uc.
        return super().form_valid(form)

class SubCategoriaEdit(SinPrivilegios, generic.UpdateView):
    permission_required = "inv.change_subcategoria"
    model = SubCategoria
    template_name = 'inv/subcategoria_form.html'
    context_object_name = "obj"
    form_class = SubCategoriaForm
    success_url = reverse_lazy("inv:subcategoria_list") #Lugar de redirección al dar summit

    def form_valid(self, form):
        form.instance.um = self.request.user.id #agrega el id del usuario que esta logueado en uc.
        return super().form_valid(form)

class SubCategoriaDel(SinPrivilegios, generic.DeleteView):
    permission_required = "inv.delete_subcategoria"
    model= SubCategoria
    template_name = 'inv/catalogos_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy("inv:subcategoria_list")

#CRUD DE MARCA#
class MarcaView(SinPrivilegios, generic.ListView):
    permission_required = "inv.view_marca"
    model = Marca #Modelo a mostrar
    template_name = "inv/marca_list.html"
    context_object_name = "obj"
    
class MarcaNew(SinPrivilegios, generic.CreateView):
    permission_required = "inv.add_marca"
    model = Marca
    template_name = 'inv/marca_form.html'
    context_object_name = "obj"
    form_class = MarcaForm
    success_url = reverse_lazy("inv:marca_list") #Lugar de redirección al dar summit

    def form_valid(self, form):
        form.instance.uc = self.request.user #agrega el id del usuario que esta logueado en uc.
        return super().form_valid(form)

class MarcaEdit(SinPrivilegios, generic.UpdateView):
    permission_required = "inv.change_marca"
    model = Marca
    template_name = 'inv/marca_form.html'
    context_object_name = "obj"
    form_class = MarcaForm
    success_url = reverse_lazy("inv:marca_list") #Lugar de redirección al dar summit

    def form_valid(self, form):
        form.instance.um = self.request.user.id #agrega el id del usuario que esta logueado en uc.
        return super().form_valid(form)

@login_required(login_url='/login/')
@permission_required("inv.change_marca", login_url='bases:sin_privilegios')
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
class UMView(SinPrivilegios, generic.ListView):
    permission_required = "inv.view_unidadmedida"
    model = UnidadMedida #Modelo a mostrar
    template_name = "inv/unidadmedida_list.html"
    context_object_name = "obj"

class UMNew(SinPrivilegios, generic.CreateView):
    permission_required = "inv.add_unidadmedida"
    model = UnidadMedida
    template_name = 'inv/unidadmedida_form.html'
    context_object_name = "obj"
    form_class = UnidadMedidaForm
    success_url = reverse_lazy("inv:unidadesmedida_list") #Lugar de redirección al dar summit

    def form_valid(self, form):
        form.instance.uc = self.request.user #agrega el id del usuario que esta logueado en uc.
        return super().form_valid(form)

class UMEdit(SinPrivilegios, generic.UpdateView):
    permission_required = "inv.change_unidadmedida"
    model = UnidadMedida
    template_name = 'inv/unidadmedida_form.html'
    context_object_name = "obj"
    form_class = UnidadMedidaForm
    success_url = reverse_lazy("inv:unidadesmedida_list") #Lugar de redirección al dar summit

    def form_valid(self, form):
        form.instance.um = self.request.user.id #agrega el id del usuario que esta logueado en uc.
        return super().form_valid(form)

@login_required(login_url='/login/')
@permission_required("inv.change_unidadmedida", login_url='bases:sin_privilegios')
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
class ProductoView(SinPrivilegios, generic.ListView):
    permission_required = "inv.view_producto"
    model = Producto #Modelo a mostrar
    template_name = "inv/producto_list.html"
    context_object_name = "obj"

class ProductoNew(SinPrivilegios, generic.CreateView):
    permission_required = "inv.add_producto"
    model = Producto
    template_name = 'inv/producto_form.html'
    context_object_name = "obj"
    form_class = ProductoForm
    success_url = reverse_lazy("inv:producto_list") #Lugar de redirección al dar summit
    

    def form_valid(self, form):
        form.instance.uc = self.request.user #agrega el id del usuario que esta logueado en uc.
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ProductoNew, self).get_context_data(**kwargs)
        context["categorias"] = Categoria.objects.all()
        context["subcategorias"] = SubCategoria.objects.all()
        return context

class ProductoEdit(SinPrivilegios, generic.UpdateView):
    permission_required = "inv.change_producto"
    model = Producto
    template_name = 'inv/producto_form.html'
    context_object_name = "obj"
    form_class = ProductoForm
    success_url = reverse_lazy("inv:producto_list") #Lugar de redirección al dar summit
    

    def form_valid(self, form):
        form.instance.um = self.request.user.id #agrega el id del usuario que esta logueado en uc.
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        context = super(ProductoEdit, self).get_context_data(**kwargs)
        context["categorias"] = Categoria.objects.all()
        context["subcategorias"] = SubCategoria.objects.all()

        context["obj"] = Producto.objects.filter(pk=pk).first()
        return context

@login_required(login_url='/login/')
@permission_required("inv.change_producto", login_url='bases:sin_privilegios')
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