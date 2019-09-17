# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dwh_data', '0007_auto_20160707_1441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bdcoaaddress',
            name='id',
        ),
        migrations.RemoveField(
            model_name='bdcooaddress',
            name='id',
        ),
        migrations.RemoveField(
            model_name='bdgroup',
            name='id',
        ),
        migrations.AddField(
            model_name='basedata',
            name='d_arrival',
            field=models.DateTimeField(null=True, verbose_name='Arrival Date', db_column='n_ArrivalDate'),
        ),
        migrations.AddField(
            model_name='basedata',
            name='d_dob',
            field=models.DateTimeField(null=True, verbose_name='Birth Date', db_column='n_DateOfBirth'),
        ),
        migrations.AddField(
            model_name='basedata',
            name='d_registration',
            field=models.DateTimeField(null=True, verbose_name='Registration Date', db_column='n_RegistrationDate'),
        ),
        migrations.AlterField(
            model_name='bdcoaaddress',
            name='fkindividualguid',
            field=models.OneToOneField(primary_key=True, serialize=False, to='dwh_data.BaseData'),
        ),
        migrations.AlterField(
            model_name='bdcooaddress',
            name='coolocationlevel1id',
            field=models.CharField(max_length=255, null=True, verbose_name='Country of origin1', db_column='COOLocationLevel1ID', blank=True),
        ),
        migrations.AlterField(
            model_name='bdcooaddress',
            name='coolocationlevel2id',
            field=models.CharField(max_length=255, null=True, verbose_name='Country of origin2', db_column='COOLocationLevel2ID', blank=True),
        ),
        migrations.AlterField(
            model_name='bdcooaddress',
            name='coolocationlevel3id',
            field=models.CharField(max_length=255, null=True, verbose_name='Country of origin3', db_column='COOLocationLevel3ID', blank=True),
        ),
        migrations.AlterField(
            model_name='bdcooaddress',
            name='coolocationlevel4id',
            field=models.CharField(max_length=255, null=True, verbose_name='Country of origin4', db_column='COOLocationLevel4ID', blank=True),
        ),
        migrations.AlterField(
            model_name='bdcooaddress',
            name='coolocationlevel5id',
            field=models.CharField(max_length=255, null=True, verbose_name='Country of origin5', db_column='COOLocationLevel5ID', blank=True),
        ),
        migrations.AlterField(
            model_name='bdcooaddress',
            name='fkindividualguid',
            field=models.OneToOneField(primary_key=True, serialize=False, to='dwh_data.BaseData'),
        ),
        migrations.AlterField(
            model_name='bdgroup',
            name='fkindividualguid',
            field=models.OneToOneField(primary_key=True, serialize=False, to='dwh_data.BaseData'),
        ),
    ]
