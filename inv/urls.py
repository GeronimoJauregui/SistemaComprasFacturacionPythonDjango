from django.urls import path
from .views import CategoriaView, CategoriaNew, CategoriaEdit, CategoriaDel, \
    SubCategoriaView, SubCategoriaNew, SubCategoriaEdit, SubCategoriaDel, \
    MarcaView, MarcaNew, MarcaEdit, Marca_Inactivar, \
    UMView, UMNew, UMEdit, UM_Inactivar,\
    ProductoView, ProductoNew, ProductoEdit, Producto_Inactivar

urlpatterns = [
    #Rustas para el CRUD de categoria.
    path('categorias/',CategoriaView.as_view(), name='categoria_list'),
    path('categorias/new',CategoriaNew.as_view(), name='categoria_new'),
    path('categorias/edit/<int:pk>',CategoriaEdit.as_view(), name='categoria_edit'),
    path('categorias/delete/<int:pk>',CategoriaDel.as_view(), name='categoria_del'),
    
    #Rutas para el CRUD de sub categoria.
    path('subcategorias/',SubCategoriaView.as_view(), name='subcategoria_list'),
    path('subcategorias/new',SubCategoriaNew.as_view(), name='subcategoria_new'),
    path('subcategorias/edit/<int:pk>',SubCategoriaEdit.as_view(), name='subcategoria_edit'),
    path('subcategorias/delete/<int:pk>',SubCategoriaDel.as_view(), name='subcategoria_del'),

    #Rutas para el CRUD de marca.
    path('marcas/',MarcaView.as_view(), name='marca_list'),
    path('marcas/new',MarcaNew.as_view(), name='marca_new'),
    path('marcas/edit/<int:pk>',MarcaEdit.as_view(), name='marca_edit'),
    path('marcas/inactivar/<int:id>',Marca_Inactivar, name='marca_inactivar'),

    #Rutas para el CRUD de unidades de medida.
    path('unidadesmedida/',UMView.as_view(), name='unidadesmedida_list'),
    path('unidadesmedida/new',UMNew.as_view(), name='unidadesmedida_new'),
    path('unidadesmedida/edit/<int:pk>',UMEdit.as_view(), name='unidadesmedida_edit'),
    path('unidadesmedida/inactivar/<int:id>',UM_Inactivar, name='unidadesmedida_inactivar'),

    #Rutas para el CRUD de producto.
    path('producto/',ProductoView.as_view(), name='producto_list'),
    path('producto/new',ProductoNew.as_view(), name='producto_new'),
    path('producto/edit/<int:pk>',ProductoEdit.as_view(), name='producto_edit'),
    path('producto/inactivar/<int:id>',Producto_Inactivar, name='producto_inactivar'),
]