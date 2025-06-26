from rest_framework import serializers
from .models import (
    Cliente,
    Funcionario,
    MateriaPrima,
    Produto,
    Pedido,
    ItemPedido,
    FuncionarioTemItemPedido,
    OrdemDeProducao
)

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'

class MateriaPrimaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MateriaPrima
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    materias_primas = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    funcionarios = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Produto
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPedido
        fields = '__all__'

class FuncionarioTemItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuncionarioTemItemPedido  
        fields = '__all__'

class OrdemDeProducaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdemDeProducao
        fields = '__all__'
