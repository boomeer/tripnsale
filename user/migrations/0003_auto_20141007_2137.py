# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20141007_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='regRemoteAddr',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='remoteAddr',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
    ]
