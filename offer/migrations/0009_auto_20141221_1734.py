# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0007_country_ititle'),
        ('offer', '0008_auto_20141220_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyoffer',
            name='fr',
            field=models.ForeignKey(null=True, to='place.Country', blank=True, related_name='buy_country_from'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='buyoffer',
            name='frCity',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='buyoffer',
            name='frTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 21, 17, 34, 0, 985137)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='buyoffer',
            name='ifrCity',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='buyoffer',
            name='to',
            field=models.ForeignKey(null=True, to='place.Country', blank=True, related_name='buy_country_to'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='buyoffer',
            name='toCity',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='buyoffer',
            name='createTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 21, 17, 34, 0, 984665)),
        ),
        migrations.AlterField(
            model_name='saleoffer',
            name='createTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 21, 17, 34, 0, 984665)),
        ),
        migrations.AlterField(
            model_name='saleoffer',
            name='frTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 21, 17, 34, 0, 986386)),
        ),
        migrations.AlterField(
            model_name='saleoffer',
            name='toTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 21, 17, 34, 0, 986470)),
        ),
    ]
