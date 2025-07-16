from django.db import models

# Create your models here.

class Fotografia(models.Model):

    OPCOES_CATEGORIA = [
        ("NEBULOSA", "Imperatriz"),
        ("GALAXIA", "Rainha"),
        ("ESTRELA", "Princesa"),
        ("PLANETA", "Condessa"),
    ]

    nome = models.CharField(max_length= 100, null= False, blank= False)
    legenda = models.CharField(max_length= 200, null= False, blank= False)
    categoria = models.CharField(max_length=50, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length= 200, null= False, blank= False)
    publicada = models.BooleanField(default=False)

    def __str__(self):
        return f"Fotografia[nome= {self.nome}]"