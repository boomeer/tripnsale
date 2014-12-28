# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0002_auto_20141228_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyoffer',
            name='createTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 28, 3, 59, 33, 489007)),
        ),
        migrations.AlterField(
            model_name='saleoffer',
            name='createTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 28, 3, 59, 33, 489007)),
        ),
        migrations.AlterField(
            model_name='saleoffer',
            name='frTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 28, 3, 59, 33, 491145)),
        ),
        migrations.AlterField(
            model_name='saleoffer',
            name='toTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 28, 3, 59, 33, 491303)),
        ),
    ]
