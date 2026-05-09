from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Cliente, Pedido
from .serializers import ClienteSerializer, PedidoSerializer


# -------------------
# CRUD Clientes
# -------------------
class ClienteListCreateView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all().order_by('id')
    serializer_class = ClienteSerializer


class ClienteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all().order_by('id')
    serializer_class = ClienteSerializer


# -------------------
# CRUD Pedidos
# -------------------
class PedidoListCreateView(generics.ListCreateAPIView):
    queryset = Pedido.objects.all().order_by('id')
    serializer_class = PedidoSerializer

    # NUEVO
    filter_backends = [SearchFilter, OrderingFilter]

    # NUEVO — Campos que se podrán buscar
    search_fields = [
        'estado',
        'monto_total',
        'fecha',
        'cliente__nombre',     # IMPORTANTE: búsqueda por nombre del cliente
    ]

    # NUEVO — Filtros exactos
    def get_queryset(self):
        queryset = Pedido.objects.all().order_by('id')

        fecha = self.request.query_params.get('fecha')
        estado = self.request.query_params.get('estado')
        monto = self.request.query_params.get('monto_total')

        # FILTROS OPCIONALES
        if fecha:
            queryset = queryset.filter(fecha=fecha)

        if estado:
            queryset = queryset.filter(estado__icontains=estado)

        if monto:
            queryset = queryset.filter(monto_total=monto)

        return queryset


class PedidoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pedido.objects.all().order_by('id')
    serializer_class = PedidoSerializer