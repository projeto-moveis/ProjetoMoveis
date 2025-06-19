from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14, primary_key=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    cep = models.CharField(max_length=9, default='00000-000')

    def __str__(self):
        return self.nome




# Create your models here.
