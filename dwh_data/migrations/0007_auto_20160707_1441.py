# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dwh_data', '0006_auto_20160629_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basedata',
            name='concatenatedname',
            field=models.CharField(max_length=255, null=True, verbose_name='Full Names', db_column='ConcatenatedName', blank=True),
        ),
    ]
