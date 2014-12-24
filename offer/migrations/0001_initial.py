# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0058_auto_20141220_0134'),
        ('gallery', '0006_photo_thumbnail'),
        ('place', '0007_country_ititle'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyOffer',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.TextField(default='')),
                ('content', models.TextField(default='')),
                ('verified', models.BooleanField(default=True)),
                ('removed', models.BooleanField(default=False)),
                ('closed', models.BooleanField(default=False)),
                ('ititle', models.TextField(default='')),
                ('costFrom', models.FloatField(default=None)),
                ('costTo', models.FloatField(default=None)),
                ('guarant', models.BooleanField(default=False)),
                ('gallery', models.ForeignKey(to='gallery.Gallery')),
                ('owner', models.ForeignKey(to='user.User', default=None, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SaleOffer',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.TextField(default='')),
                ('content', models.TextField(default='')),
                ('verified', models.BooleanField(default=True)),
                ('removed', models.BooleanField(default=False)),
                ('closed', models.BooleanField(default=False)),
                ('frCity', models.TextField(default='')),
                ('ifrCity', models.TextField(default='')),
                ('frTime', models.DateTimeField(default=datetime.datetime(2014, 12, 20, 1, 34, 22, 423753))),
                ('toCity', models.TextField(default='')),
                ('itoCity', models.TextField(default='')),
                ('toTime', models.DateTimeField(default=datetime.datetime(2014, 12, 20, 1, 34, 22, 423845))),
                ('deposit', models.FloatField(default=None)),
                ('guarant', models.BooleanField(default=False)),
                ('fr', models.ForeignKey(to='place.Country', related_name='country_from', null=True, blank=True)),
                ('owner', models.ForeignKey(to='user.User', default=None, null=True, blank=True)),
                ('to', models.ForeignKey(to='place.Country', related_name='country_to', null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
