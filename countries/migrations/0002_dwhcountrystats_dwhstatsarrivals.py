# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='dwhCountryStats',
            fields=[
                ('statId', models.IntegerField(max_length=100, serialize=False, primary_key=True, db_column='stat_id')),
                ('TotalPop', models.IntegerField(max_length=10, db_column='i_tot_pop')),
                ('TotalMPop', models.IntegerField(max_length=10, db_column='i_tot_m_pop')),
                ('TotalFPop', models.IntegerField(max_length=10, db_column='i_tot_f_pop')),
                ('demographics', models.CharField(max_length=255, null=True, db_column='s_demographics', blank=True)),
                ('ageSex', models.CharField(max_length=255, null=True, db_column='s_age_sex', blank=True)),
                ('popGender', models.CharField(max_length=255, null=True, db_column='s_gender', blank=True)),
                ('dtUpdated', models.DateTimeField(default=datetime.datetime.now, db_column='dt_updated')),
                ('fkCountryId', models.ForeignKey(to='countries.dwhCountry')),
            ],
            options={
                'verbose_name': 'DWH Country Statistics',
                'db_table': 'dwh_country_stats',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='dwhStatsArrivals',
            fields=[
                ('statIdArrival', models.IntegerField(max_length=100, serialize=False, primary_key=True, db_column='arrival_stat_id')),
                ('arrivalYear', models.IntegerField(max_length=5, db_column='i_arr_year')),
                ('arrivalWeek', models.IntegerField(max_length=2, db_column='i_arr_week')),
                ('arrivalTotalWeek', models.IntegerField(max_length=8, db_column='i_arr_total')),
                ('arrivalDemsWeek', models.CharField(max_length=255, null=True, db_column='s_demographics', blank=True)),
                ('arrivalAgeSexWeek', models.CharField(max_length=255, null=True, db_column='s_age_sex', blank=True)),
                ('arrivalGenderWeek', models.CharField(max_length=255, null=True, db_column='s_gender', blank=True)),
                ('dtUpdated', models.DateTimeField(default=datetime.datetime.now, db_column='dt_updated')),
                ('fkStatId', models.ForeignKey(to='countries.dwhCountryStats')),
            ],
            options={
                'verbose_name': 'DWH Refugee Arrival Trends',
                'db_table': 'dwh_c_arrival_stats',
                'managed': True,
            },
        ),
    ]
