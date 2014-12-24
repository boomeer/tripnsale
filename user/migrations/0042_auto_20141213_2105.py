# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0041_auto_20141213_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conferencemsg',
            name='fr',
            field=models.ForeignKey(to='user.User', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='conferencemsg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 13, 21, 5, 58, 808061)),
        ),
        migrations.AlterField(
            model_name='msg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 13, 21, 5, 58, 806099)),
        ),
    ]
