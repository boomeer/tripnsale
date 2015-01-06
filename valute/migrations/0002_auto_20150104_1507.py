# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valute', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='valute',
            options={'ordering': ['-updTime']},
        ),
        migrations.AlterField(
            model_name='valute',
            name='toName',
            field=models.TextField(default='Российский рубль'),
            preserve_default=True,
        ),
    ]
