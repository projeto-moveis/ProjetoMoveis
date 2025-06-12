from django.db import models

class Id_cliente(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True) # ID sequencial

    def __str__(self):
            return self.id

class nome_cliente(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome



# Create your models here.
