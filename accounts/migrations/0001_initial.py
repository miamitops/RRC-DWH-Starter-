# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import easy_thumbnails.fields
import userena.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organizations',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'i_id')),
                ('orgName', models.CharField(unique=True, max_length=255, db_column=b'name')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mugshot', easy_thumbnails.fields.ThumbnailerImageField(help_text='A personal image displayed in your profile.', upload_to=userena.models.upload_to_mugshot, verbose_name='mugshot', blank=True)),
                ('privacy', models.CharField(default=b'registered', help_text='Designates who can view your profile.', max_length=15, verbose_name='privacy', choices=[(b'open', 'Open'), (b'registered', 'Registered'), (b'closed', 'Closed')])),
                ('country', models.CharField(max_length=255, null=True, verbose_name=b'Country', db_column=b'country')),
                ('city', models.CharField(max_length=255, null=True, verbose_name=b'City', db_column=b'city')),
                ('dutyStation', models.CharField(max_length=255, verbose_name=b'Duty Station', db_column=b'duty_station')),
                ('department', models.CharField(max_length=255, verbose_name=b'Department or Unit', db_column=b'department')),
                ('organization', models.ForeignKey(db_column=b'fk_org', verbose_name=b'Organization', to='accounts.Organizations')),
                ('user', models.OneToOneField(related_name='my_profile', verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'accounts_profile2',
                'managed': True,
            },
        ),
    ]
