# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0004_auto_20160608_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='dwhcountrystats',
            name='TotalUnaccompanied',
            field=models.IntegerField(default=0, db_column='i_tot_um_pop'),
            preserve_default=False,
        ),
    ]
