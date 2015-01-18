# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20150117_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='emailNotify',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='conferencemsg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 18, 23, 21, 19, 973542)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='msg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 18, 23, 21, 19, 970695)),
            preserve_default=True,
        ),
    ]
