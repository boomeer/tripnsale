# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0009_auto_20141220_0225'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='verified',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gallery',
            name='createTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 20, 2, 25, 30, 382333)),
        ),
    ]
