# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwh_data', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bdcoaaddress',
            name='fkindividualguid',
        ),
        migrations.RemoveField(
            model_name='bdcooaddress',
            name='fkindividualguid',
        ),
        migrations.RemoveField(
            model_name='bdgroup',
            name='fkindividualguid',
        ),
        migrations.RemoveField(
            model_name='bdvulnerability',
            name='fkindividualguid',
        ),
        migrations.AlterField(
            model_name='basedata',
            name='individualguid',
            field=models.CharField(max_length=255, null=True, db_column='Individualguid', blank=True),
        ),
        migrations.AlterField(
            model_name='basedata',
            name='individualid',
            field=models.CharField(max_length=255, serialize=False, primary_key=True, db_column='IndividualID', blank=True),
        ),
    ]
