from rest_framework import serializers
from .models import Cliente, Pedido

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'direccion']


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ['id', 'fecha', 'monto_total', 'estado', 'cliente']