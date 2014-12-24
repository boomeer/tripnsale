# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0066_auto_20141221_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='conference',
            name='plusGuarant',
            field=models.ForeignKey(to='user.Conference', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='conferencemsg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 23, 1, 35, 36, 517121)),
        ),
        migrations.AlterField(
            model_name='msg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 23, 1, 35, 36, 515177)),
        ),
    ]
