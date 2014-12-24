# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0040_auto_20141213_1922'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemMsg',
            fields=[
                ('conferencemsg_ptr', models.OneToOneField(serialize=False, parent_link=True, auto_created=True, primary_key=True, to='user.ConferenceMsg')),
            ],
            options={
            },
            bases=('user.conferencemsg',),
        ),
        migrations.AlterField(
            model_name='conferencemsg',
            name='fr',
            field=models.ForeignKey(blank=True, to='user.User'),
        ),
        migrations.AlterField(
            model_name='conferencemsg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 13, 21, 2, 35, 270483)),
        ),
        migrations.AlterField(
            model_name='msg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 13, 21, 2, 35, 268784)),
        ),
    ]
