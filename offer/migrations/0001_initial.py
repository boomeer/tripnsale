# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyOffer',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.TextField(default='')),
                ('content', models.TextField(default='')),
                ('verified', models.BooleanField(default=True)),
                ('removed', models.BooleanField(default=False)),
                ('closed', models.BooleanField(default=False)),
                ('createTime', models.DateTimeField(default=datetime.datetime(2014, 12, 25, 1, 37, 11, 241030))),
                ('ititle', models.TextField(default='', blank=True)),
                ('costFrom', models.FloatField(default=None)),
                ('costTo', models.FloatField(default=None)),
                ('guarant', models.BooleanField(default=False)),
                ('frCity', models.TextField(default='', blank=True)),
                ('ifrCity', models.TextField(default='', blank=True)),
                ('toCity', models.TextField(default='', blank=True)),
                ('itoCity', models.TextField(default='', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OfferConnection',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SaleOffer',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.TextField(default='')),
                ('content', models.TextField(default='')),
                ('verified', models.BooleanField(default=True)),
                ('removed', models.BooleanField(default=False)),
                ('closed', models.BooleanField(default=False)),
                ('createTime', models.DateTimeField(default=datetime.datetime(2014, 12, 25, 1, 37, 11, 241030))),
                ('frCity', models.TextField(default='', blank=True)),
                ('ifrCity', models.TextField(default='', blank=True)),
                ('frTime', models.DateTimeField(default=datetime.datetime(2014, 12, 25, 1, 37, 11, 244115))),
                ('toCity', models.TextField(default='', blank=True)),
                ('itoCity', models.TextField(default='', blank=True)),
                ('toTime', models.DateTimeField(default=datetime.datetime(2014, 12, 25, 1, 37, 11, 244236))),
                ('deposit', models.FloatField(default=None)),
                ('guarant', models.BooleanField(default=False)),
                ('fr', models.ForeignKey(blank=True, null=True, to='place.Country', related_name='country_from')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
