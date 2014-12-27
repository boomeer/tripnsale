# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0008_auto_20141227_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='createTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 27, 10, 54, 29, 744358)),
            preserve_default=True,
        ),
    ]
