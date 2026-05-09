from rest_framework import generics
from .models import Cliente, Pedido
from .serializers import ClienteSerializer, PedidoSerializer

# Clientes
class ClienteListCreateView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all().order_by('id')
    serializer_class = ClienteSerializer


class ClienteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all().order_by('id')
    serializer_class = ClienteSerializer


# Pedidos
class PedidoListCreateView(generics.ListCreateAPIView):
    queryset = Pedido.objects.all().order_by('id')
    serializer_class = PedidoSerializer


class PedidoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pedido.objects.all().order_by('id')
    serializer_class = PedidoSerializer