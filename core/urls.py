from django.urls import path
from . import views

urlpatterns = [
    # Endpoints Clientes
    path('clientes/', views.ClienteListCreateView.as_view(), name='clientes-list-create'),
    path('clientes/<int:pk>/', views.ClienteDetailView.as_view(), name='clientes-detail'),

    # Endpoints Pedidos
    path('pedidos/', views.PedidoListCreateView.as_view(), name='pedidos-list-create'),
    path('pedidos/<int:pk>/', views.PedidoDetailView.as_view(), name='pedidos-detail'),
]