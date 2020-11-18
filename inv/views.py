from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Categoria, SubCategoria
from .forms import CategoriaForm, SubCategoriaForm
from django.urls import reverse_lazy

#CRUD DE CATEGORIA#
class CategoriaView(LoginRequiredMixin, generic.ListView):
    model = Categoria #Modelo a mostrar
    template_name = "inv/categoria_list.html"
    context_object_name = "obj"
    login_url = "bases/login"

class CategoriaNew(LoginRequiredMixin, generic.CreateView):
    model = Categoria
    template_name = 'inv/categoria_form.html'
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy("inv:categoria_list") #Lugar de redirección al dar summit
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user #agrega el id del usuario que esta logueado en uc.
        return super().form_valid(form)

class CategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Categoria
    template_name = 'inv/categoria_form.html'
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy("inv:categoria_list") #Lugar de redirección al dar summit
    login_url = "bases:login"

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