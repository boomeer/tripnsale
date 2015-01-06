# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valute', '0002_auto_20150104_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valute',
            name='toId',
            field=models.TextField(default='RUB'),
            preserve_default=True,
        ),
    ]
