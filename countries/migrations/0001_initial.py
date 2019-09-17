# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dwhCountry',
            fields=[
                ('countryID', models.CharField(max_length=4, serialize=False, primary_key=True, db_column='countryID', blank=True)),
                ('countryName', models.CharField(max_length=255, null=True, db_column='countryName', blank=True)),
                ('countryBorder', models.CharField(max_length=255, null=True, db_column='kmlBorder', blank=True)),
                ('isEnabled', models.BooleanField(default=False, db_column='enabled')),
            ],
            options={
                'verbose_name': 'DWH Countries',
                'db_table': 'conf_countries',
                'managed': True,
            },
        ),
    ]
