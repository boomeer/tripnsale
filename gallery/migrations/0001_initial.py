# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('createTime', models.DateTimeField(default=datetime.datetime(2014, 12, 28, 0, 54, 25, 875539))),
                ('token', models.TextField(default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('img', models.ImageField(null=True, upload_to='gallery_img', blank=True)),
                ('thumbnail', models.ImageField(null=True, upload_to='gallery_img', blank=True)),
                ('token', models.TextField(default='')),
                ('verified', models.BooleanField(default=True)),
                ('gallery', models.ForeignKey(related_name='photos', to='gallery.Gallery', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='gallery',
            name='head',
            field=models.ForeignKey(related_name='heads', to='gallery.Photo', null=True, blank=True),
            preserve_default=True,
        ),
    ]
