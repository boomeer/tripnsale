# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_photo_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='createTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 20, 2, 3, 20, 580906)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gallery',
            name='token',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photo',
            name='token',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
    ]
