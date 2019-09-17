# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0005_dwhcountrystats_totalunaccompanied'),
    ]

    operations = [
        migrations.CreateModel(
            name='dwhStatsRegistered',
            fields=[
                ('statRegId', models.IntegerField(serialize=False, primary_key=True, db_column='arrival_stat_id')),
                ('regYear', models.IntegerField(db_column='i_arr_year')),
                ('regWeek', models.IntegerField(db_column='i_arr_week')),
                ('regTotalWeek', models.IntegerField(db_column='i_arr_total')),
                ('regDemsWeek', models.CharField(max_length=255, null=True, db_column='s_demographics', blank=True)),
                ('regAgeSexWeek', models.CharField(max_length=255, null=True, db_column='s_age_sex', blank=True)),
                ('regMale', models.IntegerField(verbose_name='Male Arrivals', db_column='i_arr_m')),
                ('regFemale', models.IntegerField(verbose_name='Female Arrivals', db_column='i_arr_f')),
                ('dtUpdated', models.DateTimeField(default=datetime.datetime.now, db_column='dt_updated')),
                ('dtCreated', models.DateTimeField(default=datetime.datetime.now, db_column='dt_created')),
            ],
            options={
                'verbose_name': 'Registration Trends',
                'db_table': 'dwh_c_registration_stats',
                'managed': True,
            },
        ),
        migrations.AlterModelOptions(
            name='dwhcountry',
            options={'managed': True, 'verbose_name': 'Countries'},
        ),
        migrations.AlterModelOptions(
            name='dwhcountrystats',
            options={'managed': True, 'verbose_name': 'Country Statistics'},
        ),
        migrations.AlterModelOptions(
            name='dwhstatsarrivals',
            options={'managed': True, 'verbose_name': 'Arrival Trends'},
        ),
        migrations.RemoveField(
            model_name='dwhstatsarrivals',
            name='dtUpdated',
        ),
        migrations.AddField(
            model_name='dwhstatsarrivals',
            name='dtCreated',
            field=models.DateTimeField(default=datetime.datetime.now, db_column='dt_created'),
        ),
        migrations.AlterField(
            model_name='dwhstatsarrivals',
            name='arrivalFemale',
            field=models.IntegerField(verbose_name='Female Arrivals', db_column='i_arr_f'),
        ),
        migrations.AlterField(
            model_name='dwhstatsarrivals',
            name='arrivalMale',
            field=models.IntegerField(verbose_name='Male Arrivals', db_column='i_arr_m'),
        ),
        migrations.AddField(
            model_name='dwhstatsregistered',
            name='StatId',
            field=models.ForeignKey(to='countries.dwhCountryStats'),
        ),
    ]
