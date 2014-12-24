# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20141225_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conferencemsg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 25, 1, 43, 11, 447626)),
        ),
        migrations.AlterField(
            model_name='msg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 25, 1, 43, 11, 444173)),
        ),
    ]
