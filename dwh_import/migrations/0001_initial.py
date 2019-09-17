# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0006_auto_20160814_2119'),
        ('report_builder', '0005_auto_20160814_2108'),
    ]

    operations = [
        migrations.CreateModel(
            name='DWHImportFile',
            fields=[
                ('fileid', models.AutoField(serialize=False, primary_key=True, db_column=b'i_file_id')),
                ('progressinstance', models.CharField(max_length=254, verbose_name=b'Progress Instance', db_column=b's_progress_instance')),
                ('dategenerated', models.DateTimeField(verbose_name=b'Date Generated', db_column=b'd_generated')),
                ('dateimport', models.DateTimeField(verbose_name=b'Date Imported', db_column=b'd_imported')),
                ('importstatus', models.CharField(blank=True, max_length=5, choices=[(b'succs', b'Successfull'), (b'faile', b'Failed'), (b'succe', b'Successfull but with errors')])),
                ('fcountry', models.ForeignKey(db_column=b'fk_country_id', verbose_name=b'Country', to='countries.dwhCountry')),
            ],
            options={
                'verbose_name': 'CSV Import History',
                'db_table': 't_dwh_import_files',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DWHImportLog',
            fields=[
                ('report_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='report_builder.Report')),
                ('logid', models.AutoField(serialize=False, primary_key=True, db_column=b'log_id')),
                ('loglevel', models.CharField(blank=True, max_length=5, db_column=b'log_level', choices=[(b'f', b'File'), (b'r', b'Row')])),
                ('logmessage', models.CharField(max_length=1200, db_column=b'log_message', blank=True)),
                ('fileid', models.ForeignKey(to='dwh_import.DWHImportFile', db_column=b'file_id')),
            ],
            options={
                'verbose_name': 'DWH Import Log',
                'db_table': 't_dwh_import_logs',
                'managed': True,
            },
            bases=('report_builder.report',),
        ),
        migrations.CreateModel(
            name='importTypes',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'id')),
                ('name', models.CharField(max_length=254, db_column=b's_name')),
                ('description', models.CharField(max_length=254, db_column=b's_desc')),
            ],
            options={
                'verbose_name': 'DWH Import Types',
                'db_table': 't_dwh_import_types',
                'managed': True,
            },
        ),
    ]
