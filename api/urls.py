from django.urls import path, include
from .views import ProductoList, ProductoDetalle
urlpatterns = [
    path('v1/productos/',ProductoList.as_view(),name='producto_list'),
    path('v1/productos/<str:codigo>',ProductoDetalle.as_view(),name='producto_detalle')
]

# 127.0.0.1:8000/api/v1/productos/