# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dwh_data', '0005_auto_20160627_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basedata',
            name='age',
            field=models.CharField(max_length=255, null=True, verbose_name='Age', db_column='Age', blank=True),
        ),
        migrations.AlterField(
            model_name='basedata',
            name='arrivaldate',
            field=models.CharField(max_length=255, null=True, verbose_name='Arrival Date', db_column='ArrivalDate', blank=True),
        ),
        migrations.AlterField(
            model_name='basedata',
            name='asylumcountrycode',
            field=models.CharField(max_length=255, null=True, verbose_name='Country of Asylum', db_column='AsylumCountryCode', blank=True),
        ),
        migrations.AlterField(
            model_name='basedata',
            name='concatenatedname',
            field=models.CharField(max_length=255, null=True, verbose_name='Full Name', db_column='ConcatenatedName', blank=True),
        ),
        migrations.AlterField(
            model_name='basedata',
            name='countryoforigin',
            field=models.CharField(max_length=255, null=True, verbose_name='Country of Origin', db_column='CountryOfOrigin', blank=True),
        ),
        migrations.AlterField(
            model_name='basedata',
            name='createdate',
            field=models.CharField(max_length=255, null=True, verbose_name='Date created', db_column='CreateDate', blank=True),
        ),
        migrations.AlterField(
            model_name='basedata',
            name='dateofbirth',
            field=models.CharField(max_length=255, null=True, verbose_name='Date of Birth', db_column='DateofBirth', blank=True),
        ),
        migrations.AlterField(
            model_name='basedata',
            name='educationlevelcode',
            field=models.CharField(max_length=255, null=True, verbose_name='Education Level', db_column='EducationLevelCode', blank=True),
        ),
        migrations.AlterField(
            model_name='basedata',
            name='ethnicitycode',
            field=models.CharField(max_length=255, null=True, verbose_name='Ethnicity', db_column='EthnicityCode', blank=True),
        ),
        migrations.AlterField(
            model_name='basedata',
            name='familyname',
            field=models.CharField(max_length=255, null=True, verbose_name='Family Name', db_column='FamilyName', blank=True),
        ),
        migrations.AlterField(
            model_name='basedata',
            name='fathername',
            field=models.CharField(max_length=255, null=True, verbose_name='Fathers Name', db_column='FatherName', blank=True),
        ),
        migrations.AlterField(
            model_name='basedata',
            name='gender',
            field=models.CharField(max_length=255, null=True, verbose_name='Gender', blank=True),
        ),
        migrations.AlterField(
            model_name='basedata',
            name='givenname',
            field=models.CharField(max_length=255, null=True, verbose_name='Given Name', db_column='GivenName', blank=True),
        ),
        migrations.AlterField(
            model_name='basedata',
            name='hasspneed',
            field=models.CharField(max_length=255, null=True, verbose_name='Has special need', db_column='HasSPNeed', blank=True),
        ),
        migrations.AlterField(
            model_name='basedata',
            name='individualagecohortcode',
            field=models.CharField(max_length=255, null=True, verbose_name='Age Group', db_column='IndividualAgeCohortCode', blank=True),
        ),
        migrations.AlterField(
            model_name='basedata',
            name='individualguid',
            field=models.CharField(max_length=255, serialize=False, verbose_name='ID', primary_key=True, db_column='Individualguid'),
        ),
        migrations.AlterField(
            model_name='basedata',
            name='marriagestatuscode',
            field=models.CharField(max_length=255, null=True, verbose_name='Marriage status Code', db_column='MarriageStatusCode', blank=True),
        ),
        migrations.AlterField(
            model_name='basedata',
            name='mothername',
            field=models.CharField(max_length=255, null=True, verbose_name='Mothers Name', db_column='MotherName', blank=True),
        ),
        migrations.AlterField(
            model_name='basedata',
            name='nationalitycode',
            field=models.CharField(max_length=255, null=True, verbose_name='Nationality', db_column='NationalityCode', blank=True),
        ),
        migrations.AlterField(
            model_name='basedata',
            name='occupationcode',
            field=models.CharField(max_length=255, null=True, verbose_name='Occupation', db_column='OccupationCode', blank=True),
        ),
        migrations.AlterField(
            model_name='basedata',
            name='processstatuscode',
            field=models.CharField(max_length=255, null=True, verbose_name='Process Status', db_column='ProcessStatusCode', blank=True),
        ),
        migrations.AlterField(
            model_name='basedata',
            name='refugeestatuscode',
            field=models.CharField(max_length=255, null=True, verbose_name='Refugee Status', db_column='RefugeeStatusCode', blank=True),
        ),
        migrations.AlterField(
            model_name='basedata',
            name='registrationdate',
            field=models.CharField(max_length=255, null=True, verbose_name='Registration Date', db_column='RegistrationDate', blank=True),
        ),
        migrations.AlterField(
            model_name='basedata',
            name='resettlementstatuscode',
            field=models.CharField(max_length=255, null=True, verbose_name='Resettlement Status Code', db_column='ResettlementStatusCode', blank=True),
        ),
        migrations.AlterField(
            model_name='basedata',
            name='rsdstatuscode',
            field=models.CharField(max_length=255, null=True, verbose_name='RSD Status', db_column='RSDStatusCode', blank=True),
        ),
        migrations.AlterField(
            model_name='basedata',
            name='siteidcreate',
            field=models.CharField(max_length=255, null=True, verbose_name='Site created', db_column='SiteIDCreate', blank=True),
        ),
        migrations.AlterField(
            model_name='basedata',
            name='siteidowner',
            field=models.CharField(max_length=255, null=True, verbose_name='Site Owner', db_column='SiteIDOwner', blank=True),
        ),
        migrations.AlterField(
            model_name='basedata',
            name='volrepstatuscode',
            field=models.CharField(max_length=255, null=True, verbose_name='Voluntary repatriation status', db_column='VolRepStatusCode', blank=True),
        ),
    ]
