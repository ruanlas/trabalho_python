# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class dadosVeicular(models.Model):
    veiculo_id=models.IntegerField()
    modelo=models.CharField(max_length=50)
    velocidade=models.IntegerField()
    temperaturaAr=models.IntegerField()

    def __str__(self):
        return self.modelo