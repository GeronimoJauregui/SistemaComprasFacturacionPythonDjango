from django.urls import path
from .views import ProveedorView, ProveedorNew, ProveedorEdit, ProveedorInactivar

urlpatterns = [
    #Rustas para el CRUD de proveedor.
    path('proveedor/',ProveedorView.as_view(), name='proveedor_list'),
    path('proveedor/new',ProveedorNew.as_view(), name='proveedor_new'),
    path('proveedor/edit/<int:pk>',ProveedorEdit.as_view(), name='proveedor_edit'),
    path('proveedor/inactivar/<int:id>',ProveedorInactivar, name='proveedor_inactivar'),
]