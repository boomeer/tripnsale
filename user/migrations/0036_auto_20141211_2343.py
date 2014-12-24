# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0035_auto_20141211_2332'),
    ]

    operations = [
        migrations.AddField(
            model_name='conferencemsg',
            name='fr',
            field=models.ForeignKey(default=1, to='user.User'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='conferencemsg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 11, 23, 43, 30, 719959)),
        ),
        migrations.AlterField(
            model_name='msg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 11, 23, 43, 30, 718285)),
        ),
    ]
