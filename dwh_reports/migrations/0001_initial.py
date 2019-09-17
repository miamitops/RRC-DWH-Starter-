# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report_builder', '0003_auto_20150720_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='dwhFormat',
            fields=[
                ('tid', models.AutoField(serialize=False, primary_key=True, db_column=b'i_id')),
                ('fName', models.CharField(max_length=254, db_column=b's_name')),
                ('fDescription', models.CharField(max_length=254, db_column=b's_desc')),
            ],
            options={
                'verbose_name': 'Format Type',
                'db_table': 't_dwh_report_format',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='dwhReport',
            fields=[
                ('reportId', models.OneToOneField(primary_key=True, serialize=False, to='report_builder.Report')),
                ('raw_data', models.CharField(max_length=254, null=True, db_column=b'raw_data', blank=True)),
            ],
            options={
                'verbose_name': 'DWH Report',
                'db_table': 't_dwh_reports',
                'managed': True,
            },
            bases=('report_builder.report',),
        ),
        migrations.CreateModel(
            name='dwhReportView',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'Report Views',
                'db_table': 't_dwh_report_view',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='reportTypes',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'id')),
                ('name', models.CharField(max_length=254, db_column=b's_name')),
                ('description', models.CharField(max_length=254, db_column=b's_desc')),
            ],
            options={
                'verbose_name': 'DWH Report Types',
                'db_table': 't_report_types',
                'managed': True,
            },
        ),
    ]
