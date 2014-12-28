# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Valute',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('updTime', models.DateTimeField()),
                ('fromVal', models.FloatField(default=1.0)),
                ('fromName', models.TextField()),
                ('fromId', models.TextField()),
                ('toVal', models.FloatField(default=1.0)),
                ('toName', models.TextField(default='Российские рубли')),
                ('toId', models.TextField(default='RUR')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
