# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0007_country_ititle'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='order',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
