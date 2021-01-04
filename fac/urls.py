from django.urls import path
from .views import ClienteView, ClienteNew, ClienteEdit, ClienteInactivar, \
    FacturaView, facturas

urlpatterns = [
    path('clientes/', ClienteView.as_view(), name="cliente_list"),
    path('clientes/new', ClienteNew.as_view(), name="cliente_new"),
    path('clientes/<int:pk>', ClienteEdit.as_view(), name="cliente_edit"),
    path('clientes/estado/<int:id>', ClienteInactivar, name="cliente_inactivar"),

    path('facturas/', FacturaView.as_view(), name="factura_list"),
    path('facturas/new', facturas, name="factura_new"),
]