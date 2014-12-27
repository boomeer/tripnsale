# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0009_auto_20141227_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='createTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 27, 22, 29, 18, 695160)),
            preserve_default=True,
        ),
    ]
