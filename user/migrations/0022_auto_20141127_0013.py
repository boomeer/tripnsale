# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0021_auto_20141127_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 27, 0, 13, 31, 566171)),
        ),
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.ForeignKey(to='place.Country'),
        ),
    ]
