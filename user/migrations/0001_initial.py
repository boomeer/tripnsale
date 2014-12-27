# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('place', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.TextField(default='')),
                ('askGuarant', models.BooleanField(default=False)),
                ('withGuarant', models.BooleanField(default=False)),
                ('plusGuarant', models.ForeignKey(to='user.Conference', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ConferenceMsg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('content', models.TextField(default='')),
                ('time', models.DateTimeField(default=datetime.datetime(2014, 12, 28, 0, 54, 25, 868467))),
                ('new', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Msg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('content', models.TextField()),
                ('time', models.DateTimeField(default=datetime.datetime(2014, 12, 28, 0, 54, 25, 865985))),
                ('new', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SystemMsg',
            fields=[
                ('conferencemsg_ptr', models.OneToOneField(auto_created=True, serialize=False, primary_key=True, parent_link=True, to='user.ConferenceMsg')),
            ],
            options={
            },
            bases=('user.conferencemsg',),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, serialize=False, primary_key=True, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('remoteAddr', models.TextField(default='')),
                ('regRemoteAddr', models.TextField(default='')),
                ('city', models.TextField(blank=True, default='')),
                ('avatar', models.ImageField(null=True, upload_to='avatars', blank=True)),
                ('avatarThumb', models.ImageField(null=True, upload_to='avatars/thumbs', blank=True)),
                ('activated', models.BooleanField(default=True)),
                ('activateCode', models.TextField(default='')),
                ('guarant', models.BooleanField(default=False)),
                ('birthday', models.DateField(null=True, default=None)),
                ('about', models.TextField(blank=True, default='')),
                ('hidden', models.BooleanField(default=False)),
                ('country', models.ForeignKey(to='place.Country')),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
        ),
        migrations.AddField(
            model_name='msg',
            name='fr',
            field=models.ForeignKey(related_name='user_from', to='user.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='msg',
            name='to',
            field=models.ForeignKey(related_name='user_to', to='user.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='conferencemsg',
            name='conf',
            field=models.ForeignKey(related_name='msgs', to='user.Conference'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='conferencemsg',
            name='fr',
            field=models.ForeignKey(to='user.User', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='conference',
            name='users',
            field=models.ManyToManyField(to='user.User'),
            preserve_default=True,
        ),
    ]
