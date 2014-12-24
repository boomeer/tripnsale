# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('place', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.TextField(default='')),
                ('askGuarant', models.BooleanField(default=False)),
                ('withGuarant', models.BooleanField(default=False)),
                ('plusGuarant', models.ForeignKey(blank=True, null=True, to='user.Conference')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ConferenceMsg',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('content', models.TextField(default='')),
                ('time', models.DateTimeField(default=datetime.datetime(2014, 12, 25, 1, 37, 11, 229253))),
                ('new', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Msg',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('content', models.TextField()),
                ('time', models.DateTimeField(default=datetime.datetime(2014, 12, 25, 1, 37, 11, 225756))),
                ('new', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SystemMsg',
            fields=[
                ('conferencemsg_ptr', models.OneToOneField(auto_created=True, parent_link=True, to='user.ConferenceMsg', serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=('user.conferencemsg',),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, parent_link=True, to=settings.AUTH_USER_MODEL, serialize=False, primary_key=True)),
                ('remoteAddr', models.TextField(default='')),
                ('regRemoteAddr', models.TextField(default='')),
                ('city', models.TextField(default='', blank=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars')),
                ('avatarThumb', models.ImageField(blank=True, null=True, upload_to='avatars/thumbs')),
                ('activated', models.BooleanField(default=True)),
                ('activateCode', models.TextField(default='')),
                ('guarant', models.BooleanField(default=False)),
                ('bday', models.TextField(default='01.01.1970')),
                ('about', models.TextField(default='', blank=True)),
                ('hidden', models.BooleanField(default=False)),
                ('country', models.ForeignKey(to='place.Country')),
            ],
            options={
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
                'abstract': False,
            },
            bases=('auth.user',),
        ),
        migrations.AddField(
            model_name='msg',
            name='fr',
            field=models.ForeignKey(to='user.User', related_name='user_from'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='msg',
            name='to',
            field=models.ForeignKey(to='user.User', related_name='user_to'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='conferencemsg',
            name='conf',
            field=models.ForeignKey(to='user.Conference', related_name='msgs'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='conferencemsg',
            name='fr',
            field=models.ForeignKey(blank=True, null=True, to='user.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='conference',
            name='users',
            field=models.ManyToManyField(to='user.User'),
            preserve_default=True,
        ),
    ]
