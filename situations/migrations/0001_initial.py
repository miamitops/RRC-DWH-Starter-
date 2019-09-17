# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dwhSituations',
            fields=[
                ('situationID', models.CharField(max_length=4, serialize=False, primary_key=True, db_column=b'situationID', blank=True)),
                ('countryName', models.CharField(max_length=255, null=True, db_column=b'countryName', blank=True)),
                ('countryBorder', models.CharField(max_length=255, null=True, db_column=b'kmlBorder', blank=True)),
                ('isActive', models.BooleanField(default=False, db_column=b'active')),
            ],
            options={
                'verbose_name': 'DWH Situations',
                'db_table': 'c_situations',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='situationOverview',
            fields=[
                ('pkStatId', models.IntegerField(serialize=False, primary_key=True, db_column=b'statID')),
                ('dtCreate', models.DateTimeField(auto_now_add=True, db_column=b'dtCreate')),
                ('dtUpdate', models.DateTimeField(auto_now_add=True, db_column=b'dtUpdate')),
                ('dtStatFrom', models.DateTimeField(db_column=b'dtStatFrom')),
                ('dtStatTo', models.DateTimeField(db_column=b'dtStatTo')),
                ('fksituationid', models.ForeignKey(to='situations.dwhSituations')),
            ],
            options={
                'verbose_name': 'DWH Situations overview',
                'db_table': 'c_situations_overview',
                'managed': True,
            },
        ),
    ]
