# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('offer', '0001_initial'),
        ('place', '0001_initial'),
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='saleoffer',
            name='owner',
            field=models.ForeignKey(to='user.User', default=None, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='saleoffer',
            name='to',
            field=models.ForeignKey(related_name='country_to', to='place.Country', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='offerconnection',
            name='buy',
            field=models.ForeignKey(to='offer.BuyOffer', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='offerconnection',
            name='sale',
            field=models.ForeignKey(to='offer.SaleOffer', null=True, blank=True),
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
            field=models.ForeignKey(related_name='buy_country_from', to='place.Country', null=True, blank=True),
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
            field=models.ForeignKey(to='user.User', default=None, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='buyoffer',
            name='to',
            field=models.ForeignKey(related_name='buy_country_to', to='place.Country', null=True, blank=True),
            preserve_default=True,
        ),
    ]
