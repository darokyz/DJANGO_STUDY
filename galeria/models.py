from django.db import models
from datetime import datetime

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
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default= datetime.now, blank=False)

    def __str__(self):
        return self.nome