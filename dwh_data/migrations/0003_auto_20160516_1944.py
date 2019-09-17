# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwh_data', '0002_auto_20160516_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='bdcoaaddress',
            name='fkindividualguid',
            field=models.ForeignKey(default=3, to='dwh_data.BaseData'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bdcooaddress',
            name='fkindividualguid',
            field=models.ForeignKey(default=0, to='dwh_data.BaseData'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bdgroup',
            name='fkindividualguid',
            field=models.ForeignKey(default=0, to='dwh_data.BaseData'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bdvulnerability',
            name='fkindividualguid',
            field=models.ForeignKey(default=0, to='dwh_data.BaseData'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='basedata',
            name='individualguid',
            field=models.CharField(max_length=255, serialize=False, primary_key=True, db_column='Individualguid'),
        ),
        migrations.AlterField(
            model_name='basedata',
            name='individualid',
            field=models.CharField(max_length=255, db_column='IndividualID', blank=True),
        ),
    ]
