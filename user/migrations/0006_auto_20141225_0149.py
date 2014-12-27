# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20141225_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conferencemsg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 25, 1, 49, 55, 514178)),
        ),
        migrations.AlterField(
            model_name='msg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 25, 1, 49, 55, 509768)),
        ),
    ]
