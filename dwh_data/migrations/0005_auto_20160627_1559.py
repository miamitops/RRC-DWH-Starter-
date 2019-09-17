# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dwh_data', '0004_auto_20160603_1246'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basedata',
            options={'managed': True, 'verbose_name': 'Individual Information'},
        ),
    ]
