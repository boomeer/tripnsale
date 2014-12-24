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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('createTime', models.DateTimeField(default=datetime.datetime(2014, 12, 25, 1, 37, 11, 237333))),
                ('token', models.TextField(default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='gallery_img')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='gallery_img')),
                ('token', models.TextField(default='')),
                ('verified', models.BooleanField(default=True)),
                ('gallery', models.ForeignKey(blank=True, null=True, to='gallery.Gallery', related_name='photos')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='gallery',
            name='head',
            field=models.ForeignKey(blank=True, null=True, to='gallery.Photo', related_name='heads'),
            preserve_default=True,
        ),
    ]
