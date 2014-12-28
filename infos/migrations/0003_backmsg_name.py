# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infos', '0002_backmsg_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='backmsg',
            name='name',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
    ]
