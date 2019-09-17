# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report_builder', '0004_auto_20160705_1226'),
        ('dwh_reports', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dwhreport',
            name='reportId',
        ),
        migrations.AddField(
            model_name='dwhreport',
            name='dateOperation',
            field=models.CharField(default=b'MN', max_length=2, db_column=b'operation', choices=[(b'MN', b'MONTH'), (b'YR', b'YEAR')]),
        ),
        migrations.AddField(
            model_name='dwhreport',
            name='report_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=1, serialize=False, to='report_builder.Report'),
            preserve_default=False,
        ),
    ]
