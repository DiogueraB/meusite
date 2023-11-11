from django.db import models

# Create your models here.
class Questao(models.Model):
    # Cria um campo de texto com no máximo 200 caracteres.
    texto_questao = models.CharField(max_length=200)

    # Cria um campo de data e hora.
    data_publicacao = models.DateTimeField('data de publicação')

class Escolha(models.Model):
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)

    texto_escolha = models.CharField(max_length=200)

    # Cria um campo de números inteiros
    votos = models.IntegerField(default=0)
