from rest_framework import viewsets
from .models import ( Cliente, Funcionario, MateriaPrima, Produto, Pedido, ItemPedido, FuncionarioTemItemPedido, OrdemDeProducao)
from .serializers import ( ClienteSerializer, FuncionarioSerializer, MateriaPrimaSerializer, ProdutoSerializer, PedidoSerializer, ItemPedidoSerializer,  FuncionarioTemItemPedidoSerializer,   OrdemDeProducaoSerializer)

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class MateriaPrimaViewSet(viewsets.ModelViewSet):
    queryset = MateriaPrima.objects.all()
    serializer_class = MateriaPrimaSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class ItemPedidoViewSet(viewsets.ModelViewSet):
    queryset = ItemPedido.objects.all()
    serializer_class = ItemPedidoSerializer

class FuncionarioTemItemPedidoViewSet(viewsets.ModelViewSet):
    queryset = FuncionarioTemItemPedido.objects.all()
    serializer_class = FuncionarioTemItemPedidoSerializer

class OrdemDeProducaoViewSet(viewsets.ModelViewSet):
    queryset = OrdemDeProducao.objects.all()
    serializer_class = OrdemDeProducaoSerializer

# Create your views here.
