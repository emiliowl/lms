from django.db  import models
from datetime   import date

class Pessoa(models.Model):
    nome = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    celular = models.TextField(max_length=20)
    dt_expiracao = models.DateField(default=date(year=1900, month=1, day=1))
    login = models.TextField(max_length=20, unique=True)
    senha = models.TextField(max_length=20)