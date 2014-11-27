from django.db import models

class Country(models.Model):
    title = models.TextField(default="")
    name = models.TextField(default="")
