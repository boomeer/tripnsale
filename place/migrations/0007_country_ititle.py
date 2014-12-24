# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0006_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='ititle',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
    ]
