# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0008_auto_20141220_0217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='verified',
        ),
        migrations.AlterField(
            model_name='gallery',
            name='createTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 20, 2, 25, 16, 571416)),
        ),
    ]
