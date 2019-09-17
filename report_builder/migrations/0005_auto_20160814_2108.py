# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report_builder', '0004_auto_20160705_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filterfield',
            name='filter_type',
            field=models.CharField(default=b'contains', max_length=20, blank=True, choices=[(b'exact', b'Equals'), (b'contains', b'Contains'), (b'in', b'Is one of (Multiple Values)'), (b'gt', b'Greater than'), (b'gte', b'Greater than equals'), (b'lt', b'Less than'), (b'lte', b'Less than equals'), (b'startswith', b'Starts with'), (b'endswith', b'Ends with'), (b'range', b'range'), (b'week_day', b'Week day')]),
        ),
    ]
