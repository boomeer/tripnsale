#-*- coding:utf-8 -*-

from django.db import models

class Valute(models.Model):
    date = models.DateField()
    updTime = models.DateTimeField()
    fromVal = models.FloatField(default=1.0)
    fromName = models.TextField()
    fromId = models.TextField()
    toVal = models.FloatField(default=1.0)
    toName = models.TextField(default="Российские рубли")
    toId = models.TextField(default="RUR")
