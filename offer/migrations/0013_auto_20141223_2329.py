# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0069_auto_20141223_2329'),
        ('offer', '0012_auto_20141223_0241'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfferConnection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('buy', models.ForeignKey(null=True, blank=True, to='offer.BuyOffer')),
                ('sale', models.ForeignKey(null=True, blank=True, to='offer.SaleOffer')),
                ('user', models.ForeignKey(to='user.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='buyoffer',
            name='createTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 23, 23, 29, 6, 664163)),
        ),
        migrations.AlterField(
            model_name='saleoffer',
            name='createTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 23, 23, 29, 6, 664163)),
        ),
        migrations.AlterField(
            model_name='saleoffer',
            name='frTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 23, 23, 29, 6, 665818)),
        ),
        migrations.AlterField(
            model_name='saleoffer',
            name='toTime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 23, 23, 29, 6, 665904)),
        ),
    ]
