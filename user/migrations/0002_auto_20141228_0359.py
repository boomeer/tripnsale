# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conferencemsg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 28, 3, 59, 33, 478518)),
        ),
        migrations.AlterField(
            model_name='msg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 28, 3, 59, 33, 475095)),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(null=True, blank=True, default=None),
        ),
    ]
