# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0039_auto_20141211_2357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guarantpool',
            name='conf',
        ),
        migrations.DeleteModel(
            name='GuarantPool',
        ),
        migrations.AddField(
            model_name='conference',
            name='askGuarant',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='conference',
            name='withGuarant',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='conferencemsg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 13, 19, 22, 52, 43072)),
        ),
        migrations.AlterField(
            model_name='msg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 13, 19, 22, 52, 41397)),
        ),
    ]
