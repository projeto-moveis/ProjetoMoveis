from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14, primary_key=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    cep = models.CharField(max_length=9, default='00000-000')

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    data_pedido = models.DateTimeField()
    status_pedido = models.CharField(max_length=45)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"Pedido {self.id_pedido}"

class ItemPedido(models.Model):
    id_item = models.AutoField(primary_key=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey("Produto", on_delete=models.CASCADE)
    quantidade_item = models.IntegerField()

    def __str__(self):
        return f"Item {self.id_item} - {self.produto}"

class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome_produto = models.CharField(max_length=45)
    descricao_produto = models.CharField(max_length=200)
    preco_produto = models.DecimalField(max_digits=10, decimal_places=2)
    estoque_produto = models.IntegerField()
    materias_primas = models.ManyToManyField("MateriaPrima", related_name="produtos")
    funcionarios = models.ManyToManyField("Funcionario", related_name="produtos")

    def __str__(self):
        return self.nome_produto

class OrdemDeProducao(models.Model):
    id_ordem = models.AutoField(primary_key=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    quantidade_produzida = models.IntegerField()
    funcionario = models.ForeignKey("Funcionario", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Ordem {self.id_ordem}"

class Funcionario(models.Model):
    id_funcionario = models.AutoField(primary_key=True)
    nome_funcionario = models.CharField(max_length=100)
    cargo_funcionario = models.CharField(max_length=45)

    def __str__(self):
        return self.nome_funcionario

class MateriaPrima(models.Model):
    id_materia = models.AutoField(primary_key=True)
    nome_materia = models.CharField(max_length=100)
    descricao_materia = models.CharField(max_length=200)
    estoque_materia = models.IntegerField()
    medida_materia = models.CharField(max_length=45)

    def __str__(self):
        return self.nome_materia

class FuncionarioTemItemPedido(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    item_pedido = models.ForeignKey(ItemPedido, on_delete=models.CASCADE)
    data_acao = models.DateTimeField(auto_now_add=True)
    observacao = models.TextField(blank=True)

    def __str__(self):
        return f"{self.funcionario} → {self.item_pedido}"



# Create your models here.
