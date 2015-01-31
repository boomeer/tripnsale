# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0004_auto_20150119_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyoffer',
            name='createTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 1, 0, 25, 5, 527511)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='buyrecommendvisit',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 1, 0, 25, 5, 529511)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='saleoffer',
            name='createTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 1, 0, 25, 5, 527511)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='saleoffer',
            name='frTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 1, 0, 25, 5, 528511)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='saleoffer',
            name='toTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 1, 0, 25, 5, 528511)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='salerecommendvisit',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 1, 0, 25, 5, 529511)),
            preserve_default=True,
        ),
    ]
