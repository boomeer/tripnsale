# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0005_auto_20141225_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyoffer',
            name='createTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 25, 1, 41, 10, 181566)),
        ),
        migrations.AlterField(
            model_name='saleoffer',
            name='createTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 25, 1, 41, 10, 181566)),
        ),
        migrations.AlterField(
            model_name='saleoffer',
            name='frTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 25, 1, 41, 10, 183066)),
        ),
        migrations.AlterField(
            model_name='saleoffer',
            name='toTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 25, 1, 41, 10, 183151)),
        ),
    ]
