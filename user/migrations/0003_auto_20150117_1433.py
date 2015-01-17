# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20141228_0359'),
    ]

    operations = [
        migrations.AddField(
            model_name='conferencemsg',
            name='notified',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='conferencemsg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 17, 14, 33, 1, 634311)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='msg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 17, 14, 33, 1, 631416)),
            preserve_default=True,
        ),
    ]
