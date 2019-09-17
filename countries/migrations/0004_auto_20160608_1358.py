# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0003_auto_20160608_0959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dwhstatsarrivals',
            name='arrivalGenderWeek',
        ),
        migrations.AddField(
            model_name='dwhstatsarrivals',
            name='arrivalFemale',
            field=models.IntegerField(default=0, db_column='i_arr_f'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dwhstatsarrivals',
            name='arrivalMale',
            field=models.IntegerField(default=0, db_column='i_arr_m'),
            preserve_default=False,
        ),
    ]
