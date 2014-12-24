# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='img',
            field=models.ImageField(upload_to='gallery_img', null=True, blank=True),
            preserve_default=True,
        ),
    ]
