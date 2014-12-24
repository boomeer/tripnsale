# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0070_auto_20141225_0115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Backmsg',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(default='')),
                ('email', models.TextField(default='')),
                ('is_red', models.BooleanField(default=False)),
                ('user', models.ForeignKey(null=True, default=None, to='user.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
