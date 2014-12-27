# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20141227_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conferencemsg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 27, 10, 41, 22, 78821)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='msg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 27, 10, 41, 22, 78821)),
            preserve_default=True,
        ),
    ]
