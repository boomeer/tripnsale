# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20141227_1041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='bday',
        ),
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(null=True, default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='conferencemsg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 27, 10, 54, 29, 728731)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='msg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 27, 10, 54, 29, 728731)),
            preserve_default=True,
        ),
    ]
