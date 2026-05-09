from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    # Endpoints Clientes
    path('api/clientes/', views.ClienteListCreateView.as_view(), name='clientes-list-create'),
    path('api/clientes/<int:pk>/', views.ClienteDetailView.as_view(), name='clientes-detail'),

    # Endpoints Pedidos
    path('api/pedidos/', views.PedidoListCreateView.as_view(), name='pedidos-list-create'),
    path('api/pedidos/<int:pk>/', views.PedidoDetailView.as_view(), name='pedidos-detail'),

    path('admin/', admin.site.urls),
]