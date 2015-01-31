# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='connectionNotify',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='recommendNotify',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='unreadNotify',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='conferencemsg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 1, 0, 25, 5, 501817)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='msg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 1, 0, 25, 5, 501817)),
            preserve_default=True,
        ),
    ]
