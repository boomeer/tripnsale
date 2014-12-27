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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.TextField(default='')),
                ('content', models.TextField(default='')),
                ('verified', models.BooleanField(default=True)),
                ('removed', models.BooleanField(default=False)),
                ('closed', models.BooleanField(default=False)),
                ('createTime', models.DateTimeField(default=datetime.datetime(2014, 12, 28, 0, 54, 25, 879722))),
                ('ititle', models.TextField(blank=True, default='')),
                ('costFrom', models.FloatField(default=None)),
                ('costTo', models.FloatField(default=None)),
                ('guarant', models.BooleanField(default=False)),
                ('frCity', models.TextField(blank=True, default='')),
                ('ifrCity', models.TextField(blank=True, default='')),
                ('toCity', models.TextField(blank=True, default='')),
                ('itoCity', models.TextField(blank=True, default='')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OfferConnection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SaleOffer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.TextField(default='')),
                ('content', models.TextField(default='')),
                ('verified', models.BooleanField(default=True)),
                ('removed', models.BooleanField(default=False)),
                ('closed', models.BooleanField(default=False)),
                ('createTime', models.DateTimeField(default=datetime.datetime(2014, 12, 28, 0, 54, 25, 879722))),
                ('frCity', models.TextField(blank=True, default='')),
                ('ifrCity', models.TextField(blank=True, default='')),
                ('frTime', models.DateTimeField(default=datetime.datetime(2014, 12, 28, 0, 54, 25, 882548))),
                ('toCity', models.TextField(blank=True, default='')),
                ('itoCity', models.TextField(blank=True, default='')),
                ('toTime', models.DateTimeField(default=datetime.datetime(2014, 12, 28, 0, 54, 25, 882825))),
                ('deposit', models.FloatField(default=None)),
                ('guarant', models.BooleanField(default=False)),
                ('fr', models.ForeignKey(related_name='country_from', to='place.Country', null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
