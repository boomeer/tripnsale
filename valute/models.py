#-*- coding:utf-8 -*-

from django.db import models

class Valute(models.Model):
    class Meta:
        ordering = [ "-updTime" ]
    date = models.DateField()
    updTime = models.DateTimeField()
    fromVal = models.FloatField(default=1.0)
    fromName = models.TextField()
    fromId = models.TextField()
    toVal = models.FloatField(default=1.0)
    toName = models.TextField(default="Российский рубль")
    toId = models.TextField(default="RUR")
