from django.contrib import admin
from .models import Cliente, Pedido, ItemPedido, Produto, OrdemDeProducao, Funcionario, MateriaPrima, FuncionarioTemItemPedido

admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(ItemPedido)
admin.site.register(Produto)
admin.site.register(OrdemDeProducao)
admin.site.register(Funcionario)
admin.site.register(MateriaPrima)
admin.site.register(FuncionarioTemItemPedido)



# Register your models here.
