from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ClienteViewSet,
    FuncionarioViewSet,
    MateriaPrimaViewSet,
    ProdutoViewSet,
    PedidoViewSet,
    ItemPedidoViewSet,
    FuncionarioTemItemPedidoViewSet,
    OrdemDeProducaoViewSet
)

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'funcionarios', FuncionarioViewSet)
router.register(r'materias-primas', MateriaPrimaViewSet)
router.register(r'produtos', ProdutoViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'itens-pedido', ItemPedidoViewSet)
router.register(r'funcionarios-itens', FuncionarioTemItemPedidoViewSet)
router.register(r'ordens-producao', OrdemDeProducaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
