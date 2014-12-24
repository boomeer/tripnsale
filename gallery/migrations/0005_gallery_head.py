# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20141204_0012'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='head',
            field=models.ForeignKey(related_name='heads', blank=True, to='gallery.Photo', null=True),
            preserve_default=True,
        ),
    ]
