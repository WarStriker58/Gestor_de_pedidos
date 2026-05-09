from rest_framework import serializers
from .models import Cliente, Pedido

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'direccion']


class PedidoSerializer(serializers.ModelSerializer):
    # NUEVO → Datos completos del cliente en la respuesta
    cliente_info = ClienteSerializer(source='cliente', read_only=True)

    class Meta:
        model = Pedido
        fields = [
            'id',
            'fecha',
            'monto_total',
            'estado',
            'cliente',       # ID del cliente para crear/actualizar
            'cliente_info',  # NUEVO → Datos del cliente en la respuesta
        ]