from django.db import models

# Create your models here.

class CadastroMediuns(models.Model):
    nome = models.CharField(max_length=60)
    endereco = models.CharField(max_length=60)
    email = models.CharField(max_length=70, blank=True, null=True)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length=15, blank=True, null=True)
    fixo = models.CharField(max_length=14, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cadastroMediuns'

    def __str__(self):
        return self.nome + ' ' + self.celular
