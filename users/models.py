from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=150)
    categoria = models.CharField(max_length=50, null=True, blank=True)
    data_edition = models.DateField(auto_now=True)
    data_criacao = models.DateField(auto_now=True)

    def __str__(self):
        return self.nome
        
    