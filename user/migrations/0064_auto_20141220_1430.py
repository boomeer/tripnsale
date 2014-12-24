# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0063_auto_20141220_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatarThumb',
            field=models.ImageField(upload_to='avatars/thumbs', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='conferencemsg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 20, 14, 30, 18, 402391)),
        ),
        migrations.AlterField(
            model_name='msg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 20, 14, 30, 18, 400633)),
        ),
    ]
