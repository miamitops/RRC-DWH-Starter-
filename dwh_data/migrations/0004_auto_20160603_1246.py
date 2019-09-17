# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwh_data', '0003_auto_20160516_1944'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basedata',
            options={'managed': True, 'verbose_name': 'Personal Information'},
        ),
        migrations.AlterModelOptions(
            name='bdcoaaddress',
            options={'managed': True, 'verbose_name': 'Country of Asylum Address'},
        ),
        migrations.AlterModelOptions(
            name='bdcooaddress',
            options={'managed': True, 'verbose_name': 'Country Of Origin Address'},
        ),
        migrations.AlterModelOptions(
            name='bdgroup',
            options={'managed': True, 'verbose_name': 'Group Address'},
        ),
        migrations.AlterModelOptions(
            name='bdvulnerability',
            options={'managed': True, 'verbose_name': 'Vulnerability Status'},
        ),
        migrations.RemoveField(
            model_name='basedata',
            name='isanygroupprincipalrepresentative',
        ),
        migrations.RemoveField(
            model_name='basedata',
            name='principalrepresentative',
        ),
        migrations.RemoveField(
            model_name='basedata',
            name='relationshiptext',
        ),
        migrations.RemoveField(
            model_name='basedata',
            name='relationshiptoprincipalrepresentative',
        ),
        migrations.AddField(
            model_name='bdgroup',
            name='isanygroupprincipalrepresentative',
            field=models.CharField(max_length=2, null=True, db_column='IsAnyGroupPrincipalRepresentative', blank=True),
        ),
        migrations.AddField(
            model_name='bdgroup',
            name='principalrepresentative',
            field=models.CharField(max_length=10, null=True, db_column='PrincipalRepresentative', blank=True),
        ),
        migrations.AddField(
            model_name='bdgroup',
            name='relationshiptext',
            field=models.CharField(max_length=100, null=True, db_column='RelationshipText', blank=True),
        ),
        migrations.AddField(
            model_name='bdgroup',
            name='relationshiptoprincipalrepresentative',
            field=models.CharField(max_length=20, null=True, db_column='RelationshipToPrincipalRepresentative', blank=True),
        ),
        migrations.AddField(
            model_name='bdvulnerability',
            name='dt_update',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='basedata',
            name='individualid',
            field=models.CharField(max_length=255, db_column='IndividualID'),
        ),
        migrations.AlterField(
            model_name='bdvulnerability',
            name='vulnerabilitycode',
            field=models.CharField(max_length=10, null=True, db_column='VulnerabilityCode', blank=True),
        ),
        migrations.AlterField(
            model_name='bdvulnerability',
            name='vulnerabilitydetailscode',
            field=models.CharField(max_length=10, null=True, db_column='VulnerabilityDetailsCode', blank=True),
        ),
    ]
