# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0007_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyoffer',
            name='createTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 27, 10, 34, 6, 952039)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='saleoffer',
            name='createTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 27, 10, 34, 6, 952039)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='saleoffer',
            name='frTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 27, 10, 34, 6, 952039)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='saleoffer',
            name='toTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 27, 10, 34, 6, 952039)),
            preserve_default=True,
        ),
    ]
