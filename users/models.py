from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=80)
    data_nascimento = models.DateField
    nascionalidade = models.CharField(max_length=50)


class Livro(models.Model):
    titulo = models.CharField(max_length=150)
    autor_livro = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=50, null=True, blank=True)
    data_edition = models.DateField(auto_now=True)
    data_criacao = models.DateField(auto_now=True)

    def __str__(self):
        return self.nome    
        
    