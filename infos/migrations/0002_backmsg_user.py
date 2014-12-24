# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('infos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='backmsg',
            name='user',
            field=models.ForeignKey(default=None, null=True, to='user.User'),
            preserve_default=True,
        ),
    ]
