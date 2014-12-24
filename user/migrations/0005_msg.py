# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_user_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Msg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('content', models.TextField()),
                ('time', models.DateTimeField(default=datetime.datetime(2014, 11, 15, 17, 0, 35, 935858))),
                ('fr', models.ForeignKey(to='user.User', related_name='user_from')),
                ('to', models.ForeignKey(to='user.User', related_name='user_to')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
