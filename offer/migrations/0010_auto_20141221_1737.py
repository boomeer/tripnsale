# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0009_auto_20141221_1734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyoffer',
            name='frTime',
        ),
        migrations.AddField(
            model_name='buyoffer',
            name='itoCity',
            field=models.TextField(default='', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='buyoffer',
            name='createTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 21, 17, 37, 33, 248426)),
        ),
        migrations.AlterField(
            model_name='buyoffer',
            name='frCity',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='buyoffer',
            name='ifrCity',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='buyoffer',
            name='ititle',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='buyoffer',
            name='toCity',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='saleoffer',
            name='createTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 21, 17, 37, 33, 248426)),
        ),
        migrations.AlterField(
            model_name='saleoffer',
            name='frCity',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='saleoffer',
            name='frTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 21, 17, 37, 33, 250085)),
        ),
        migrations.AlterField(
            model_name='saleoffer',
            name='ifrCity',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='saleoffer',
            name='itoCity',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='saleoffer',
            name='toCity',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='saleoffer',
            name='toTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 21, 17, 37, 33, 250171)),
        ),
    ]
