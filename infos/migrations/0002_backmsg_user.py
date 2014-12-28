# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infos', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='backmsg',
            name='user',
            field=models.ForeignKey(to='user.User', default=None, null=True),
            preserve_default=True,
        ),
    ]
