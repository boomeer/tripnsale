# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0062_auto_20141220_0225'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='bday',
            field=models.TextField(default='01.01.1970'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='conferencemsg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 20, 14, 7, 29, 246109)),
        ),
        migrations.AlterField(
            model_name='msg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 20, 14, 7, 29, 244291)),
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.TextField(default='', blank=True),
        ),
    ]
