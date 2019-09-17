# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0002_dwhcountrystats_dwhstatsarrivals'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dwhcountrystats',
            name='TotalFPop',
            field=models.IntegerField(db_column='i_tot_f_pop'),
        ),
        migrations.AlterField(
            model_name='dwhcountrystats',
            name='TotalMPop',
            field=models.IntegerField(db_column='i_tot_m_pop'),
        ),
        migrations.AlterField(
            model_name='dwhcountrystats',
            name='TotalPop',
            field=models.IntegerField(db_column='i_tot_pop'),
        ),
        migrations.AlterField(
            model_name='dwhcountrystats',
            name='dtUpdated',
            field=models.DateTimeField(default=datetime.datetime.now, db_column='dt_created'),
        ),
        migrations.AlterField(
            model_name='dwhcountrystats',
            name='statId',
            field=models.IntegerField(serialize=False, primary_key=True, db_column='stat_id'),
        ),
        migrations.AlterField(
            model_name='dwhstatsarrivals',
            name='arrivalTotalWeek',
            field=models.IntegerField(db_column='i_arr_total'),
        ),
        migrations.AlterField(
            model_name='dwhstatsarrivals',
            name='arrivalWeek',
            field=models.IntegerField(db_column='i_arr_week'),
        ),
        migrations.AlterField(
            model_name='dwhstatsarrivals',
            name='arrivalYear',
            field=models.IntegerField(db_column='i_arr_year'),
        ),
        migrations.AlterField(
            model_name='dwhstatsarrivals',
            name='dtUpdated',
            field=models.DateTimeField(default=datetime.datetime.now, db_column='dt_created'),
        ),
        migrations.AlterField(
            model_name='dwhstatsarrivals',
            name='statIdArrival',
            field=models.IntegerField(serialize=False, primary_key=True, db_column='arrival_stat_id'),
        ),
    ]
