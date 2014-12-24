# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0013_auto_20141221_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='createTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 21, 17, 37, 33, 246717)),
        ),
    ]
