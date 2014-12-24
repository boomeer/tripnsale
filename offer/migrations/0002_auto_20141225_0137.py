# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0001_initial'),
        ('user', '0001_initial'),
        ('gallery', '0001_initial'),
        ('place', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='saleoffer',
            name='owner',
            field=models.ForeignKey(default=None, null=True, to='user.User', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='saleoffer',
            name='to',
            field=models.ForeignKey(blank=True, null=True, to='place.Country', related_name='country_to'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='offerconnection',
            name='buy',
            field=models.ForeignKey(blank=True, null=True, to='offer.BuyOffer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='offerconnection',
            name='sale',
            field=models.ForeignKey(blank=True, null=True, to='offer.SaleOffer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='offerconnection',
            name='user',
            field=models.ForeignKey(to='user.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='buyoffer',
            name='fr',
            field=models.ForeignKey(blank=True, null=True, to='place.Country', related_name='buy_country_from'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='buyoffer',
            name='gallery',
            field=models.ForeignKey(to='gallery.Gallery'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='buyoffer',
            name='owner',
            field=models.ForeignKey(default=None, null=True, to='user.User', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='buyoffer',
            name='to',
            field=models.ForeignKey(blank=True, null=True, to='place.Country', related_name='buy_country_to'),
            preserve_default=True,
        ),
    ]
