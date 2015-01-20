# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20150119_2217'),
        ('offer', '0003_auto_20141228_0359'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyRecommendVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.TextField(default='')),
                ('content', models.TextField(default='')),
                ('verified', models.BooleanField(default=True)),
                ('visType', models.CharField(choices=[('M', 'email'), ('V', 'visited')], default='V', max_length=1)),
                ('time', models.DateTimeField(default=datetime.datetime(2015, 1, 19, 22, 17, 7, 938694))),
                ('baseOffer', models.ForeignKey(to='offer.BuyOffer')),
                ('recOffer', models.ForeignKey(to='offer.SaleOffer')),
                ('user', models.ForeignKey(to='user.User')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SaleRecommendVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.TextField(default='')),
                ('content', models.TextField(default='')),
                ('verified', models.BooleanField(default=True)),
                ('visType', models.CharField(choices=[('M', 'email'), ('V', 'visited')], default='V', max_length=1)),
                ('time', models.DateTimeField(default=datetime.datetime(2015, 1, 19, 22, 17, 7, 938694))),
                ('baseOffer', models.ForeignKey(to='offer.SaleOffer')),
                ('recOffer', models.ForeignKey(to='offer.BuyOffer')),
                ('user', models.ForeignKey(to='user.User')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='buyoffer',
            name='createTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 19, 22, 17, 7, 938694)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='saleoffer',
            name='createTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 19, 22, 17, 7, 938694)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='saleoffer',
            name='frTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 19, 22, 17, 7, 938694)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='saleoffer',
            name='toTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 19, 22, 17, 7, 938694)),
            preserve_default=True,
        ),
    ]
