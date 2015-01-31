# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='createTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 1, 0, 25, 5, 525510)),
            preserve_default=True,
        ),
    ]
