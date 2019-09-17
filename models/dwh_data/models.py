# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class BaseData(models.Model):
    individualid = models.CharField(db_column='IndividualID', max_length=255, blank=True, null=True, primary_key=True)  # Field name made lowercase.
    individualguid = models.CharField(db_column='Individualguid', max_length=255, blank=True, null=True)  # Field name made lowercase.
    familyname = models.CharField(db_column='FamilyName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    givenname = models.CharField(db_column='GivenName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concatenatedname = models.CharField(db_column='ConcatenatedName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    registrationdate = models.CharField(db_column='RegistrationDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dateofbirth = models.CharField(db_column='DateofBirth', max_length=255, blank=True, null=True)  # Field name made lowercase.
    countryoforigin = models.CharField(db_column='CountryOfOrigin', max_length=255, blank=True, null=True)  # Field name made lowercase.
    asylumcountrycode = models.CharField(db_column='AsylumCountryCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    arrivaldate = models.CharField(db_column='ArrivalDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(max_length=255, blank=True, null=True)
    age = models.CharField(db_column='Age', max_length=255, blank=True, null=True)  # Field name made lowercase.
    individualagecohortcode = models.CharField(db_column='IndividualAgeCohortCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nationalitycode = models.CharField(db_column='NationalityCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rsdstatuscode = models.CharField(db_column='RSDStatusCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    resettlementstatuscode = models.CharField(db_column='ResettlementStatusCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    volrepstatuscode = models.CharField(db_column='VolRepStatusCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    marriagestatuscode = models.CharField(db_column='MarriageStatusCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ethnicitycode = models.CharField(db_column='EthnicityCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    educationlevelcode = models.CharField(db_column='EducationLevelCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    occupationcode = models.CharField(db_column='OccupationCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    processstatuscode = models.CharField(db_column='ProcessStatusCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refugeestatuscode = models.CharField(db_column='RefugeeStatusCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fathername = models.CharField(db_column='FatherName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mothername = models.CharField(db_column='MotherName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    siteidowner = models.CharField(db_column='SiteIDOwner', max_length=255, blank=True, null=True)  # Field name made lowercase.
    siteidcreate = models.CharField(db_column='SiteIDCreate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isanygroupprincipalrepresentative = models.CharField(db_column='IsAnyGroupPrincipalRepresentative', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hasspneed = models.CharField(db_column='HasSPNeed', max_length=255, blank=True, null=True)  # Field name made lowercase.
    processinggrouptypecode = models.CharField(db_column='ProcessingGroupTypeCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    processinggroupnumber = models.CharField(db_column='ProcessingGroupNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    currentrationcardnumber = models.CharField(db_column='CurrentRationCardNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    processinggroupfilenumber = models.CharField(db_column='ProcessingGroupFileNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    processinggroupsize = models.CharField(db_column='ProcessingGroupSize', max_length=255, blank=True, null=True)  # Field name made lowercase.
    processinggroupstatuscode = models.CharField(db_column='ProcessingGroupStatusCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    processgroupstatusdate = models.CharField(db_column='ProcessGroupStatusDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    processinggroupregistrationdate = models.CharField(db_column='ProcessingGroupRegistrationDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    individualsequencenumber = models.CharField(db_column='IndividualSequenceNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    principalrepresentative = models.CharField(db_column='PrincipalRepresentative', max_length=255, blank=True, null=True)  # Field name made lowercase.
    relationshiptoprincipalrepresentative = models.CharField(db_column='RelationshipToPrincipalRepresentative', max_length=255, blank=True, null=True)  # Field name made lowercase.
    relationshiptext = models.CharField(db_column='RelationshipText', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coalocationlevel1id = models.CharField(db_column='COALocationLevel1ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coalocationlevel2id = models.CharField(db_column='COALocationLevel2ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coalocationlevel3id = models.CharField(db_column='COALocationLevel3ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coalocationlevel4id = models.CharField(db_column='COALocationLevel4ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coalocationlevel5id = models.CharField(db_column='COALocationLevel5ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coolocationlevel1id = models.CharField(db_column='COOLocationLevel1ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coolocationlevel2id = models.CharField(db_column='COOLocationLevel2ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coolocationlevel3id = models.CharField(db_column='COOLocationLevel3ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coolocationlevel4id = models.CharField(db_column='COOLocationLevel4ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coolocationlevel5id = models.CharField(db_column='COOLocationLevel5ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vulnerabilitycode = models.CharField(db_column='VulnerabilityCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vulnerabilitydetailscode = models.CharField(db_column='VulnerabilityDetailsCode', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'base_data'
