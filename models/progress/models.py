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


class Allmatchesaug(models.Model):
    cpims_code = models.CharField(db_column='CPIMS Code', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    childfirstname = models.CharField(db_column='ChildFirstName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    childlastname = models.CharField(db_column='ChildLastName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    totrace = models.CharField(db_column='ToTrace', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rel = models.CharField(max_length=255, blank=True, null=True)
    agency = models.CharField(max_length=255, blank=True, null=True)
    country_field = models.CharField(db_column='Country ', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    individualid = models.CharField(db_column='individualID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    country_asc = models.CharField(db_column='Country_ASC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=255, blank=True, null=True)  # Field name made lowercase.
    firstnamelastname = models.CharField(db_column='FirstNameLastName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastnamefirtsname = models.CharField(db_column='LastNameFirtsName', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AllMatchesAug'


class Basedata20151016(models.Model):
    individualid = models.CharField(db_column='IndividualID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    individualguid = models.CharField(db_column='Individualguid', max_length=50, blank=True, null=True)  # Field name made lowercase.
    familyname = models.CharField(db_column='FamilyName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    givenname = models.CharField(db_column='GivenName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    concatenatedname = models.CharField(db_column='ConcatenatedName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    registrationdate = models.CharField(db_column='RegistrationDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dateofbirth = models.CharField(db_column='DateofBirth', max_length=50, blank=True, null=True)  # Field name made lowercase.
    countryoforigin = models.CharField(db_column='CountryOfOrigin', max_length=50, blank=True, null=True)  # Field name made lowercase.
    asylumcountrycode = models.CharField(db_column='AsylumCountryCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    arrivaldate = models.CharField(db_column='ArrivalDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(max_length=50, blank=True, null=True)
    age = models.CharField(db_column='Age', max_length=50, blank=True, null=True)  # Field name made lowercase.
    individualagecohortcode = models.CharField(db_column='IndividualAgeCohortCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nationalitycode = models.CharField(db_column='NationalityCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rsdstatuscode = models.CharField(db_column='RSDStatusCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    resettlementstatuscode = models.CharField(db_column='ResettlementStatusCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    volrepstatuscode = models.CharField(db_column='VolRepStatusCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    marriagestatuscode = models.CharField(db_column='MarriageStatusCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ethnicitycode = models.CharField(db_column='EthnicityCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    educationlevelcode = models.CharField(db_column='EducationLevelCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    occupationcode = models.CharField(db_column='OccupationCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    processstatuscode = models.CharField(db_column='ProcessStatusCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    refugeestatuscode = models.CharField(db_column='RefugeeStatusCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fathername = models.CharField(db_column='FatherName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    mothername = models.CharField(db_column='MotherName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    siteidowner = models.CharField(db_column='SiteIDOwner', max_length=50, blank=True, null=True)  # Field name made lowercase.
    siteidcreate = models.CharField(db_column='SiteIDCreate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isanygroupprincipalrepresentative = models.CharField(db_column='IsAnyGroupPrincipalRepresentative', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hasspneed = models.CharField(db_column='HasSPNeed', max_length=50, blank=True, null=True)  # Field name made lowercase.
    processinggrouptypecode = models.CharField(db_column='ProcessingGroupTypeCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    processinggroupnumber = models.CharField(db_column='ProcessingGroupNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    currentrationcardnumber = models.CharField(db_column='CurrentRationCardNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    processinggroupfilenumber = models.CharField(db_column='ProcessingGroupFileNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    processinggroupsize = models.CharField(db_column='ProcessingGroupSize', max_length=50, blank=True, null=True)  # Field name made lowercase.
    processinggroupstatuscode = models.CharField(db_column='ProcessingGroupStatusCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    processgroupstatusdate = models.CharField(db_column='ProcessGroupStatusDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    processinggroupregistrationdate = models.CharField(db_column='ProcessingGroupRegistrationDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    individualsequencenumber = models.CharField(db_column='IndividualSequenceNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    principalrepresentative = models.CharField(db_column='PrincipalRepresentative', max_length=50, blank=True, null=True)  # Field name made lowercase.
    relationshiptoprincipalrepresentative = models.CharField(db_column='RelationshipToPrincipalRepresentative', max_length=50, blank=True, null=True)  # Field name made lowercase.
    relationshiptext = models.CharField(db_column='RelationshipText', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coalocationlevel1id = models.CharField(db_column='COALocationLevel1ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coalocationlevel2id = models.CharField(db_column='COALocationLevel2ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coalocationlevel3id = models.CharField(db_column='COALocationLevel3ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coalocationlevel4id = models.CharField(db_column='COALocationLevel4ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coalocationlevel5id = models.CharField(db_column='COALocationLevel5ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coolocationlevel1id = models.CharField(db_column='COOLocationLevel1ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coolocationlevel2id = models.CharField(db_column='COOLocationLevel2ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coolocationlevel3id = models.CharField(db_column='COOLocationLevel3ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coolocationlevel4id = models.CharField(db_column='COOLocationLevel4ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coolocationlevel5id = models.CharField(db_column='COOLocationLevel5ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vulnerabilitycode = models.CharField(db_column='VulnerabilityCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vulnerabilitydetailscode = models.CharField(db_column='VulnerabilityDetailsCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cpimsname = models.TextField(db_column='CPIMSNAme', blank=True, null=True)  # Field name made lowercase.
    ll2 = models.CharField(db_column='LL2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    asy2 = models.CharField(db_column='ASY2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    arrmonth = models.IntegerField(db_column='ARRMonth', blank=True, null=True)  # Field name made lowercase.
    arrday = models.IntegerField(db_column='ARRDay', blank=True, null=True)  # Field name made lowercase.
    arryear = models.IntegerField(db_column='ARRYear', blank=True, null=True)  # Field name made lowercase.
    regmonth = models.IntegerField(db_column='REGMonth', blank=True, null=True)  # Field name made lowercase.
    regday = models.IntegerField(db_column='REGDay', blank=True, null=True)  # Field name made lowercase.
    regyear = models.IntegerField(db_column='REGYear', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BaseData_20151016'


class CpimsData105Matches(models.Model):
    tracking_tracing_or_tracking_and_tracing_field = models.CharField(db_column='Tracking, Tracing or Tracking and Tracing ', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    cpims_code = models.CharField(db_column='CPIMS Code', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unhcr_id = models.CharField(db_column='UNHCR ID', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    protection_status_field = models.CharField(db_column='Protection Status ', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    first_name = models.CharField(db_column='First name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    column2 = models.CharField(db_column='Column2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    middle_name = models.CharField(db_column='Middle Name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_name = models.CharField(db_column='Last Name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    column1 = models.CharField(db_column='Column1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date_of_birth = models.DateTimeField(db_column='Date of Birth', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    age = models.FloatField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    nationality = models.CharField(db_column='Nationality', max_length=255, blank=True, null=True)  # Field name made lowercase.
    location_of_origin_1 = models.CharField(db_column='Location of Origin 1', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_of_origin_2 = models.CharField(db_column='Location of Origin 2', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_of_origin_3 = models.CharField(db_column='Location of Origin 3', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    registering_agency = models.CharField(db_column='Registering Agency', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_of_registration = models.DateTimeField(db_column='Date of Registration', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    father_s_first_name = models.CharField(db_column=u"Father's First Name", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    father_s_second_name = models.CharField(db_column=u"Father's Second Name", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    father_s_third_name = models.CharField(db_column=u"Father's Third Name", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    is_father_alive_field = models.CharField(db_column='Is Father Alive?', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    mother_s_first_name = models.CharField(db_column=u"Mother's First  Name", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mother_s_second_name = models.CharField(db_column=u"Mother's Second Name", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mother_s_third_name = models.CharField(db_column=u"Mother's Third  Name", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    is_mother_alive_field = models.CharField(db_column='Is mother alive?', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name_of_current_caregiver = models.CharField(db_column='Name of current caregiver', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_where_child_is_currently_living_1 = models.CharField(db_column='Location where child is currently living 1', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_where_child_is_currently_living_2 = models.CharField(db_column='Location where child is currently living 2', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_where_child_is_currently_living_3 = models.CharField(db_column='Location where child is currently living 3', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    relationship_of_caregiver_to_child = models.CharField(db_column='Relationship of caregiver to child', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_of_separation = models.DateTimeField(db_column='Date of separation', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    does_the_child_want_family_reunification_field = models.CharField(db_column='Does the child want family reunification?', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name_of_person_to_trace = models.CharField(db_column='Name of person to trace', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    relationship_of_person_to_trace_with_child = models.CharField(db_column='Relationship of person to trace with child', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_of_separation_1 = models.CharField(db_column='Location of Separation 1', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_of_separation_2 = models.CharField(db_column='Location of Separation 2', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_of_separation_3 = models.CharField(db_column='Location of Separation 3', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    country_field = models.CharField(db_column='Country ', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    agency = models.CharField(max_length=255, blank=True, null=True)
    s_no_sorting_field = models.FloatField(db_column='S#No (Sorting)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'CPIMS Data_105 Matches'


class ChildVerified(models.Model):
    unhcr_id = models.CharField(db_column='UNHCR ID', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cpims_field = models.DateTimeField(db_column='CPIMS #', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    rftr_code = models.DateTimeField(db_column='RFTR Code', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_of_registration = models.DateTimeField(db_column='Date of registration', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_of_referral = models.CharField(db_column='Date of referral', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    registering_agency_of_enquirer = models.CharField(db_column='Registering Agency of Enquirer', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    receiving_agency_for_verification = models.CharField(db_column='Receiving agency for verification', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    has_the_verification_form_been_completed_by_ftr_partner_field = models.CharField(db_column='Has the Verification Form been completed by FTR Partner?', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    date_verification_completed = models.CharField(db_column='Date verification completed', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    comments = models.CharField(db_column='Comments', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Child Verified'


class Dataaddress(models.Model):
    individualguid = models.CharField(db_column='Individualguid', max_length=50, blank=True, null=True)  # Field name made lowercase.
    individualidadress = models.CharField(db_column='IndividualIDADRESS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coalocationlevel1id = models.CharField(db_column='COALocationLevel1ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coalocationlevel2id = models.CharField(db_column='COALocationLevel2ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coalocationlevel3id = models.CharField(db_column='COALocationLevel3ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coalocationlevel4id = models.CharField(db_column='COALocationLevel4ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coalocationlevel5id = models.CharField(db_column='COALocationLevel5ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coolocationlevel1id = models.CharField(db_column='COOLocationLevel1ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coolocationlevel2id = models.CharField(db_column='COOLocationLevel2ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coolocationlevel3id = models.CharField(db_column='COOLocationLevel3ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coolocationlevel4id = models.CharField(db_column='COOLocationLevel4ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coolocationlevel5id = models.CharField(db_column='COOLocationLevel5ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dup = models.BigIntegerField(db_column='Dup', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DataAddress'


class Databid(models.Model):
    individualguid = models.CharField(db_column='Individualguid', max_length=50, blank=True, null=True)  # Field name made lowercase.
    individualidbid = models.CharField(db_column='IndividualIDBID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bidevent = models.CharField(db_column='BIDevent', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bidresultevent = models.CharField(db_column='BIDResultEvent', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dup = models.BigIntegerField(db_column='Dup', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DataBID'


class Dataindividual(models.Model):
    individualid = models.CharField(db_column='IndividualID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    individualguid = models.CharField(db_column='Individualguid', max_length=50, blank=True, null=True)  # Field name made lowercase.
    familyname = models.CharField(db_column='FamilyName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    givenname = models.CharField(db_column='GivenName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    registrationdate = models.CharField(db_column='RegistrationDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dateofbirth = models.CharField(db_column='DateofBirth', max_length=50, blank=True, null=True)  # Field name made lowercase.
    countryoforigin = models.CharField(db_column='CountryOfOrigin', max_length=50, blank=True, null=True)  # Field name made lowercase.
    asylumcountrycode = models.CharField(db_column='AsylumCountryCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    arrivaldate = models.CharField(db_column='ArrivalDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=50, blank=True, null=True)  # Field name made lowercase.
    individualagecohortcode = models.CharField(db_column='IndividualAgeCohortCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nationalitycode = models.CharField(db_column='NationalityCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rsdstatuscode = models.CharField(db_column='RSDStatusCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    resettlementstatuscode = models.CharField(db_column='ResettlementStatusCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    volrepstatuscode = models.CharField(db_column='VolRepStatusCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    marriagestatuscode = models.CharField(db_column='MarriageStatusCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ethnicitycode = models.CharField(db_column='EthnicityCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    educationlevelcode = models.CharField(db_column='EducationLevelCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    occupationcode = models.CharField(db_column='OccupationCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    processstatuscode = models.CharField(db_column='ProcessStatusCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    refugeestatuscode = models.CharField(db_column='RefugeeStatusCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fathername = models.CharField(db_column='FatherName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    mothername = models.CharField(db_column='MotherName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    siteidowner = models.CharField(db_column='SiteIDOwner', max_length=50, blank=True, null=True)  # Field name made lowercase.
    siteidcreate = models.CharField(db_column='SiteIDCreate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isanygroupprincipalrepresentative = models.CharField(db_column='IsAnyGroupPrincipalRepresentative', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hasspneed = models.CharField(db_column='HasSPNeed', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vulnerabilitycode = models.CharField(db_column='VulnerabilityCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vulnerabilitydetailscode = models.CharField(db_column='VulnerabilityDetailsCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sitecountry = models.CharField(db_column='SiteCountry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    marriagetext = models.CharField(max_length=50, blank=True, null=True)
    ethnictytext = models.CharField(db_column='EthnictyText', max_length=50, blank=True, null=True)  # Field name made lowercase.
    educationtext = models.CharField(db_column='EducationText', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vulnerabilitytext = models.CharField(db_column='VulnerabilityText', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vulnerabilitydetailstext = models.CharField(max_length=50, blank=True, null=True)
    dup = models.BigIntegerField(db_column='Dup', blank=True, null=True)  # Field name made lowercase.
    acountrytext = models.CharField(db_column='ACountrytext', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ocountrytext = models.CharField(db_column='OCountrytext', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nationalitytext = models.CharField(db_column='Nationalitytext', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dob = models.DateTimeField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    ard = models.DateTimeField(db_column='ARD', blank=True, null=True)  # Field name made lowercase.
    rgd = models.DateTimeField(db_column='RGD', blank=True, null=True)  # Field name made lowercase.
    ctd = models.DateTimeField(db_column='CTD', blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DataIndividual'


class EnqAugust(models.Model):
    adult_first_name_field = models.CharField(db_column='Adult First Name ', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    adult_second_name_field = models.CharField(db_column='Adult Second Name ', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    adult_last_name_field = models.CharField(db_column='Adult Last Name ', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    sex = models.CharField(db_column='Sex', max_length=255, blank=True, null=True)  # Field name made lowercase.
    relationship_to_child_being_sought = models.CharField(db_column='Relationship to child being sought', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    current_living_location_1 = models.CharField(db_column='Current Living Location 1', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    current_living_location_2 = models.CharField(db_column='Current Living Location 2', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    current_living_location_3 = models.CharField(db_column='Current Living Location 3', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_of_registration = models.DateTimeField(db_column='Date of Registration', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    first_name = models.CharField(db_column='First name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    middle_name = models.CharField(db_column='Middle Name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_name = models.CharField(db_column='Last Name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    f13 = models.CharField(db_column='F13', max_length=255, blank=True, null=True)  # Field name made lowercase.
    f14 = models.CharField(db_column='F14', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sex1 = models.CharField(db_column='Sex1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date_of_birth = models.DateTimeField(db_column='Date of Birth', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    age = models.FloatField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    possible_location = models.CharField(db_column='Possible location', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_of_separation_1 = models.CharField(db_column='Location of Separation 1', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_of_separation_2 = models.CharField(db_column='Location of Separation 2', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_of_separation_3 = models.CharField(db_column='Location of Separation 3', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    father_s_first_name = models.CharField(db_column=u"Father's First Name", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    father_s_second_name = models.CharField(db_column=u"Father's Second Name", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    father_s_third_name = models.CharField(db_column=u"Father's Third Name", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    is_father_alive_field = models.CharField(db_column='Is Father Alive?', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    mother_s_first_name = models.CharField(db_column=u"Mother's First  Name", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mother_s_second_name = models.CharField(db_column=u"Mother's Second Name", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mother_s_third_name = models.CharField(db_column=u"Mother's Third  Name", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    is_mother_alive_field = models.CharField(db_column='Is mother alive?', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'Enq_August'


class Fisrtroundmatch(models.Model):
    individualid = models.CharField(db_column='IndividualID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    asy2 = models.CharField(db_column='ASY2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    age1 = models.BigIntegerField(db_column='Age1', blank=True, null=True)  # Field name made lowercase.
    individualagecohortcode = models.CharField(db_column='IndividualAgeCohortCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    first_name = models.TextField(db_column='First name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    middle_name = models.TextField(db_column='Middle Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_name = models.TextField(db_column='Last Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sex = models.TextField(db_column='Sex', blank=True, null=True)  # Field name made lowercase.
    age = models.TextField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    givenname = models.CharField(db_column='GivenName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    familyname = models.CharField(db_column='FamilyName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    concatenatedname = models.CharField(db_column='ConcatenatedName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(max_length=50, blank=True, null=True)
    fathername = models.CharField(db_column='FatherName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    mothername = models.CharField(db_column='MotherName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    fatherfullname = models.CharField(max_length=100, blank=True, null=True)
    motherfullname = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FisrtRoundMatch'


class KakumaA(models.Model):
    first_name = models.TextField(db_column='First name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    middle_name = models.TextField(db_column='Middle Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_name = models.TextField(db_column='Last Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sex = models.TextField(db_column='Sex', blank=True, null=True)  # Field name made lowercase.
    location_of_origin_2 = models.TextField(db_column='Location of Origin 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    father_first_name = models.TextField(db_column='Father First Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    father_second_name = models.TextField(db_column='Father  Second Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    father_third_name = models.TextField(db_column='Father Third Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    is_father_alive = models.TextField(db_column='Is Father Alive', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mothers_first_name = models.TextField(db_column='Mothers First  Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mothers_second_name = models.TextField(db_column='Mothers Second Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mothers_third_name = models.TextField(db_column='Mothers Third  Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    totrace = models.TextField(db_column='ToTrace', blank=True, null=True)  # Field name made lowercase.
    reltotrace = models.TextField(db_column='RelToTrace', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Kakuma_A'


class Matches3(models.Model):
    unhcr_id = models.TextField(db_column='UNHCR ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    protection_status_field = models.TextField(db_column='Protection Status ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    first_name = models.TextField(db_column='First name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    middle_name = models.TextField(db_column='Middle Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_name = models.TextField(db_column='Last Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sex = models.TextField(db_column='Sex', blank=True, null=True)  # Field name made lowercase.
    date_of_birth = models.TextField(db_column='Date of Birth', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    age = models.TextField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    nationality = models.TextField(db_column='Nationality', blank=True, null=True)  # Field name made lowercase.
    location_of_origin_2 = models.TextField(db_column='Location of Origin 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_of_origin_3 = models.TextField(db_column='Location of Origin 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    father_s_first_name = models.TextField(db_column=u"Father's First Name", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    father_s_second_name = models.TextField(db_column=u"Father's Second Name", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    father_s_third_name = models.TextField(db_column=u"Father's Third Name", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fa = models.TextField(db_column='FA', blank=True, null=True)  # Field name made lowercase.
    mother_s_first_name = models.TextField(db_column=u"Mother's First  Name", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mother_s_second_name = models.TextField(db_column=u"Mother's Second Name", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mother_s_third_name = models.TextField(db_column=u"Mother's Third  Name", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ma = models.TextField(db_column='MA', blank=True, null=True)  # Field name made lowercase.
    name_of_current_caregiver = models.TextField(db_column='Name of current caregiver', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_where_child_is_currently_living_1 = models.TextField(db_column='Location where child is currently living 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_where_child_is_currently_living_2 = models.TextField(db_column='Location where child is currently living 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_where_child_is_currently_living_3 = models.TextField(db_column='Location where child is currently living 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    relationship_of_caregiver_to_child = models.TextField(db_column='Relationship of caregiver to child', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_of_separation = models.TextField(db_column='Date of separation', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    does_the_child_want_family_reunification_field = models.TextField(db_column='Does the child want family reunification?', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name_of_person_to_trace = models.TextField(db_column='Name of person to trace', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    relationship_of_person_to_trace_with_child = models.TextField(db_column='Relationship of person to trace with child', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_of_separation_1 = models.TextField(db_column='Location of Separation 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_of_separation_2 = models.TextField(db_column='Location of Separation 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_of_separation_3 = models.TextField(db_column='Location of Separation 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    country_field = models.TextField(db_column='Country ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    column_32 = models.TextField(db_column='Column 32')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    column_33 = models.TextField(db_column='Column 33')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    column_34 = models.TextField(db_column='Column 34')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    column_35 = models.TextField(db_column='Column 35')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    column_36 = models.TextField(db_column='Column 36')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    column_37 = models.TextField(db_column='Column 37')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    column_38 = models.TextField(db_column='Column 38')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    column_39 = models.TextField(db_column='Column 39')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    column_40 = models.TextField(db_column='Column 40')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Matches3'


class SsdData(models.Model):
    individualid = models.CharField(db_column='IndividualID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    individualguid = models.CharField(db_column='Individualguid', max_length=50, blank=True, null=True)  # Field name made lowercase.
    familyname = models.CharField(db_column='FamilyName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    givenname = models.CharField(db_column='GivenName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    concatenatedname = models.CharField(db_column='ConcatenatedName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    registrationdate = models.CharField(db_column='RegistrationDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dateofbirth = models.CharField(db_column='DateofBirth', max_length=50, blank=True, null=True)  # Field name made lowercase.
    countryoforigin = models.CharField(db_column='CountryOfOrigin', max_length=50, blank=True, null=True)  # Field name made lowercase.
    asylumcountrycode = models.CharField(db_column='AsylumCountryCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    arrivaldate = models.CharField(db_column='ArrivalDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(max_length=50, blank=True, null=True)
    age = models.CharField(db_column='Age', max_length=50, blank=True, null=True)  # Field name made lowercase.
    individualagecohortcode = models.CharField(db_column='IndividualAgeCohortCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nationalitycode = models.CharField(db_column='NationalityCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rsdstatuscode = models.CharField(db_column='RSDStatusCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    resettlementstatuscode = models.CharField(db_column='ResettlementStatusCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    volrepstatuscode = models.CharField(db_column='VolRepStatusCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    marriagestatuscode = models.CharField(db_column='MarriageStatusCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ethnicitycode = models.CharField(db_column='EthnicityCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    educationlevelcode = models.CharField(db_column='EducationLevelCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    occupationcode = models.CharField(db_column='OccupationCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    processstatuscode = models.CharField(db_column='ProcessStatusCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    refugeestatuscode = models.CharField(db_column='RefugeeStatusCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fathername = models.CharField(db_column='FatherName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    mothername = models.CharField(db_column='MotherName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    siteidowner = models.CharField(db_column='SiteIDOwner', max_length=50, blank=True, null=True)  # Field name made lowercase.
    siteidcreate = models.CharField(db_column='SiteIDCreate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isanygroupprincipalrepresentative = models.CharField(db_column='IsAnyGroupPrincipalRepresentative', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hasspneed = models.CharField(db_column='HasSPNeed', max_length=50, blank=True, null=True)  # Field name made lowercase.
    processinggrouptypecode = models.CharField(db_column='ProcessingGroupTypeCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    processinggroupnumber = models.CharField(db_column='ProcessingGroupNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    currentrationcardnumber = models.CharField(db_column='CurrentRationCardNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    processinggroupfilenumber = models.CharField(db_column='ProcessingGroupFileNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    processinggroupsize = models.CharField(db_column='ProcessingGroupSize', max_length=50, blank=True, null=True)  # Field name made lowercase.
    processinggroupstatuscode = models.CharField(db_column='ProcessingGroupStatusCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    processgroupstatusdate = models.CharField(db_column='ProcessGroupStatusDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    processinggroupregistrationdate = models.CharField(db_column='ProcessingGroupRegistrationDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    individualsequencenumber = models.CharField(db_column='IndividualSequenceNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    principalrepresentative = models.CharField(db_column='PrincipalRepresentative', max_length=50, blank=True, null=True)  # Field name made lowercase.
    relationshiptoprincipalrepresentative = models.CharField(db_column='RelationshipToPrincipalRepresentative', max_length=50, blank=True, null=True)  # Field name made lowercase.
    relationshiptext = models.CharField(db_column='RelationshipText', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coalocationlevel1id = models.CharField(db_column='COALocationLevel1ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coalocationlevel2id = models.CharField(db_column='COALocationLevel2ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coalocationlevel3id = models.CharField(db_column='COALocationLevel3ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coalocationlevel4id = models.CharField(db_column='COALocationLevel4ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coalocationlevel5id = models.CharField(db_column='COALocationLevel5ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coolocationlevel1id = models.CharField(db_column='COOLocationLevel1ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coolocationlevel2id = models.CharField(db_column='COOLocationLevel2ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coolocationlevel3id = models.CharField(db_column='COOLocationLevel3ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coolocationlevel4id = models.CharField(db_column='COOLocationLevel4ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coolocationlevel5id = models.CharField(db_column='COOLocationLevel5ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vulnerabilitycode = models.CharField(db_column='VulnerabilityCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vulnerabilitydetailscode = models.CharField(db_column='VulnerabilityDetailsCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fnamelname = models.CharField(db_column='FNameLName', max_length=101, blank=True, null=True)  # Field name made lowercase.
    lnamefname = models.CharField(db_column='LNameFName', max_length=101, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SSD_Data'


class Secondroundmatch(models.Model):
    individualid = models.CharField(db_column='IndividualID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    asy2 = models.CharField(db_column='ASY2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    age1 = models.BigIntegerField(db_column='Age1', blank=True, null=True)  # Field name made lowercase.
    individualagecohortcode = models.CharField(db_column='IndividualAgeCohortCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    first_name = models.TextField(db_column='First name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    middle_name = models.TextField(db_column='Middle Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_name = models.TextField(db_column='Last Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sex = models.TextField(db_column='Sex', blank=True, null=True)  # Field name made lowercase.
    age = models.TextField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    givenname = models.CharField(db_column='GivenName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    familyname = models.CharField(db_column='FamilyName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    concatenatedname = models.CharField(db_column='ConcatenatedName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(max_length=50, blank=True, null=True)
    fathername = models.CharField(db_column='FatherName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    mothername = models.CharField(db_column='MotherName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    fatherfullname = models.CharField(max_length=100, blank=True, null=True)
    motherfullname = models.CharField(max_length=100, blank=True, null=True)
    coalocationlevel1id = models.CharField(db_column='COALocationLevel1ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coalocationlevel2id = models.CharField(db_column='COALocationLevel2ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coalocationlevel3id = models.CharField(db_column='COALocationLevel3ID', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SecondRoundMatch'


class SsddataWithaddress(models.Model):
    individualid = models.CharField(db_column='IndividualID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    registrationdate = models.CharField(db_column='RegistrationDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    concatenatedname = models.CharField(db_column='ConcatenatedName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(max_length=50, blank=True, null=True)
    dateofbirth = models.CharField(db_column='DateofBirth', max_length=50, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='Age', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nationalitycode = models.CharField(db_column='NationalityCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    countryoforigin = models.CharField(db_column='CountryOfOrigin', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fnln_lnfn = models.CharField(db_column='FNLN_LNFN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coolevel1 = models.CharField(db_column='COOLevel1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coolevel2 = models.CharField(db_column='COOLevel2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coolevel3 = models.CharField(db_column='COOLevel3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coolevel4 = models.CharField(db_column='COOLevel4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coolevel5 = models.CharField(db_column='COOLevel5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    asylumcountrycode = models.CharField(db_column='AsylumCountryCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coalevel1 = models.CharField(db_column='COALevel1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coalevel2 = models.CharField(db_column='COALevel2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coalevel3 = models.CharField(db_column='COALevel3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coalevel4 = models.CharField(db_column='COALevel4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coalevel5 = models.CharField(db_column='COALevel5', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SsdData_WithAddress'


class Uasc(models.Model):
    tracking_tracing_or_tracking_and_tracing_field = models.CharField(db_column='Tracking, Tracing or Tracking and Tracing ', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    cpims_code = models.CharField(db_column='CPIMS Code', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unhcr_id = models.CharField(db_column='UNHCR ID', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    protection_status_field = models.CharField(db_column='Protection Status ', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    first_name = models.CharField(db_column='First name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    middle_name = models.CharField(db_column='Middle Name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_name = models.CharField(db_column='Last Name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sex = models.CharField(db_column='Sex', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date_of_birth = models.DateTimeField(db_column='Date of Birth', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    age = models.FloatField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    nationality = models.CharField(db_column='Nationality', max_length=255, blank=True, null=True)  # Field name made lowercase.
    location_of_origin_1 = models.CharField(db_column='Location of Origin 1', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_of_origin_2 = models.CharField(db_column='Location of Origin 2', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_of_origin_3 = models.CharField(db_column='Location of Origin 3', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    registering_agency = models.CharField(db_column='Registering Agency', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_of_registration = models.DateTimeField(db_column='Date of Registration', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    father_s_first_name = models.CharField(db_column=u"Father's First Name", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    father_s_second_name = models.CharField(db_column=u"Father's Second Name", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    father_s_third_name = models.CharField(db_column=u"Father's Third Name", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    is_father_alive_field = models.CharField(db_column='Is Father Alive?', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    mother_s_first_name = models.CharField(db_column=u"Mother's First  Name", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mother_s_second_name = models.CharField(db_column=u"Mother's Second Name", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mother_s_third_name = models.CharField(db_column=u"Mother's Third  Name", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    is_mother_alive_field = models.CharField(db_column='Is mother alive?', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name_of_current_caregiver = models.CharField(db_column='Name of current caregiver', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_where_child_is_currently_living_1 = models.CharField(db_column='Location where child is currently living 1', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_where_child_is_currently_living_2 = models.CharField(db_column='Location where child is currently living 2', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_where_child_is_currently_living_3 = models.CharField(db_column='Location where child is currently living 3', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    relationship_of_caregiver_to_child = models.CharField(db_column='Relationship of caregiver to child', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_of_separation = models.DateTimeField(db_column='Date of separation', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    does_the_child_want_family_reunification_field = models.CharField(db_column='Does the child want family reunification?', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name_of_person_to_trace = models.CharField(db_column='Name of person to trace', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    relationship_of_person_to_trace_with_child = models.CharField(db_column='Relationship of person to trace with child', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_of_separation_1 = models.CharField(db_column='Location of Separation 1', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_of_separation_2 = models.CharField(db_column='Location of Separation 2', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_of_separation_3 = models.CharField(db_column='Location of Separation 3', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    country_field = models.CharField(db_column='Country ', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    agency = models.CharField(max_length=255, blank=True, null=True)
    copy_of_tracking_tracing_or_tracking_and_tracing = models.CharField(db_column='Copy of Tracking, Tracing or Tracking and Tracing', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    copy_of_cpims_code = models.CharField(db_column='Copy of CPIMS Code', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    copy_of_unhcr_id = models.CharField(db_column='Copy of UNHCR ID', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    copy_of_protection_status = models.CharField(db_column='Copy of Protection Status', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    copy_of_first_name = models.CharField(db_column='Copy of First name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    copy_of_middle_name = models.CharField(db_column='Copy of Middle Name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    copy_of_last_name = models.CharField(db_column='Copy of Last Name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    copy_of_sex = models.CharField(db_column='Copy of Sex', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    copy_of_date_of_birth = models.DateTimeField(db_column='Copy of Date of Birth', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    copy_of_age = models.FloatField(db_column='Copy of Age', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    copy_of_nationality = models.CharField(db_column='Copy of Nationality', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    copy_of_location_of_origin_1 = models.CharField(db_column='Copy of Location of Origin 1', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    copy_of_location_of_origin_2 = models.CharField(db_column='Copy of Location of Origin 2', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    copy_of_location_of_origin_3 = models.CharField(db_column='Copy of Location of Origin 3', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    copy_of_registering_agency = models.CharField(db_column='Copy of Registering Agency', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    copy_of_date_of_registration = models.DateTimeField(db_column='Copy of Date of Registration', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    copy_of_father_s_first_name = models.CharField(db_column=u"Copy of Father's First Name", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    copy_of_father_s_second_name = models.CharField(db_column=u"Copy of Father's Second Name", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    copy_of_father_s_third_name = models.CharField(db_column=u"Copy of Father's Third Name", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    copy_of_is_father_alive_field = models.CharField(db_column='Copy of Is Father Alive?', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    copy_of_mother_s_first_name = models.CharField(db_column=u"Copy of Mother's First  Name", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    copy_of_mother_s_second_name = models.CharField(db_column=u"Copy of Mother's Second Name", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    copy_of_mother_s_third_name = models.CharField(db_column=u"Copy of Mother's Third  Name", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    copy_of_is_mother_alive_field = models.CharField(db_column='Copy of Is mother alive?', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    copy_of_name_of_current_caregiver = models.CharField(db_column='Copy of Name of current caregiver', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    copy_of_location_where_child_is_currently_living_1 = models.CharField(db_column='Copy of Location where child is currently living 1', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    copy_of_location_where_child_is_currently_living_2 = models.CharField(db_column='Copy of Location where child is currently living 2', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    copy_of_location_where_child_is_currently_living_3 = models.CharField(db_column='Copy of Location where child is currently living 3', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    copy_of_relationship_of_caregiver_to_child = models.CharField(db_column='Copy of Relationship of caregiver to child', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    copy_of_date_of_separation = models.DateTimeField(db_column='Copy of Date of separation', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    copy_of_does_the_child_want_family_reunification_field = models.CharField(db_column='Copy of Does the child want family reunification?', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    copy_of_name_of_person_to_trace = models.CharField(db_column='Copy of Name of person to trace', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    copy_of_relationship_of_person_to_trace_with_child = models.CharField(db_column='Copy of Relationship of person to trace with child', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    copy_of_location_of_separation_1 = models.CharField(db_column='Copy of Location of Separation 1', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    copy_of_location_of_separation_2 = models.CharField(db_column='Copy of Location of Separation 2', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    copy_of_location_of_separation_3 = models.CharField(db_column='Copy of Location of Separation 3', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    copy_of_country = models.CharField(db_column='Copy of Country', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    copy_of_agency = models.CharField(db_column='Copy of agency', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'UASC'


class UascAugust(models.Model):
    tracking_tracing_or_tracking_and_tracing_field = models.CharField(db_column='Tracking, Tracing or Tracking and Tracing ', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    cpims_code = models.CharField(db_column='CPIMS Code', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unhcr_id = models.CharField(db_column='UNHCR ID', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    protection_status_field = models.CharField(db_column='Protection Status ', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    first_name = models.CharField(db_column='First name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    middle_name = models.CharField(db_column='Middle Name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_name = models.CharField(db_column='Last Name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sex = models.CharField(db_column='Sex', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date_of_birth = models.DateTimeField(db_column='Date of Birth', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    age = models.FloatField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    nationality = models.CharField(db_column='Nationality', max_length=255, blank=True, null=True)  # Field name made lowercase.
    location_of_origin_1 = models.CharField(db_column='Location of Origin 1', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_of_origin_2 = models.CharField(db_column='Location of Origin 2', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_of_origin_3 = models.CharField(db_column='Location of Origin 3', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    registering_agency = models.CharField(db_column='Registering Agency', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_of_registration = models.DateTimeField(db_column='Date of Registration', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    father_s_first_name = models.CharField(db_column=u"Father's First Name", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    father_s_second_name = models.CharField(db_column=u"Father's Second Name", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    father_s_third_name = models.CharField(db_column=u"Father's Third Name", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    is_father_alive_field = models.CharField(db_column='Is Father Alive?', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    mother_s_first_name = models.CharField(db_column=u"Mother's First  Name", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mother_s_second_name = models.CharField(db_column=u"Mother's Second Name", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mother_s_third_name = models.CharField(db_column=u"Mother's Third  Name", max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    is_mother_alive_field = models.CharField(db_column='Is mother alive?', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name_of_current_caregiver = models.CharField(db_column='Name of current caregiver', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_where_child_is_currently_living_1 = models.CharField(db_column='Location where child is currently living 1', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_where_child_is_currently_living_2 = models.CharField(db_column='Location where child is currently living 2', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_where_child_is_currently_living_3 = models.CharField(db_column='Location where child is currently living 3', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    relationship_of_caregiver_to_child = models.CharField(db_column='Relationship of caregiver to child', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_of_separation = models.DateTimeField(db_column='Date of separation', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    does_the_child_want_family_reunification_field = models.CharField(db_column='Does the child want family reunification?', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name_of_person_to_trace = models.CharField(db_column='Name of person to trace', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    relationship_of_person_to_trace_with_child = models.CharField(db_column='Relationship of person to trace with child', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_of_separation_1 = models.CharField(db_column='Location of Separation 1', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_of_separation_2 = models.CharField(db_column='Location of Separation 2', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_of_separation_3 = models.CharField(db_column='Location of Separation 3', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    country_field = models.CharField(db_column='Country ', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    agency = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UASC_August'


class Configlocationlevel(models.Model):
    locationlevelid = models.CharField(db_column='LocationLevelID', primary_key=True, max_length=30)  # Field name made lowercase.
    siteid = models.CharField(db_column='SiteID', max_length=10)  # Field name made lowercase.
    locationleveldescription = models.CharField(db_column='LocationLevelDescription', max_length=100)  # Field name made lowercase.
    locationlevelactive = models.BooleanField(db_column='LocationLevelActive')  # Field name made lowercase.
    iscamp = models.BooleanField(db_column='IsCamp')  # Field name made lowercase.
    countrycode = models.CharField(db_column='CountryCode', max_length=5, blank=True, null=True)  # Field name made lowercase.
    parentid = models.CharField(db_column='ParentID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    useridcreate = models.CharField(db_column='UserIDCreate', max_length=10)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    useridupdate = models.CharField(db_column='UserIDUpdate', max_length=10)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.
    siteidcreate = models.CharField(db_column='SiteIDCreate', max_length=10)  # Field name made lowercase.
    siteidupdate = models.CharField(db_column='SiteIDUpdate', max_length=10)  # Field name made lowercase.
    siteidowner = models.CharField(db_column='SiteIDOwner', max_length=10)  # Field name made lowercase.
    ownerdate = models.DateTimeField(db_column='OwnerDate')  # Field name made lowercase.
    siteidreplicate = models.CharField(db_column='SiteIDReplicate', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'configLocationLevel'


class Enquerier(models.Model):
    adult_first_name_field = models.TextField(db_column='Adult First Name ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    adult_second_name_field = models.TextField(db_column='Adult Second Name ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    adult_last_name_field = models.TextField(db_column='Adult Last Name ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    sex = models.TextField(db_column='Sex', blank=True, null=True)  # Field name made lowercase.
    relationship_to_child_being_sought = models.TextField(db_column='Relationship to child being sought', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    current_living_location_1 = models.TextField(db_column='Current Living Location 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    current_living_location_2 = models.TextField(db_column='Current Living Location 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    current_living_location_3 = models.TextField(db_column='Current Living Location 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_of_registration = models.TextField(db_column='Date of Registration', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    first_name = models.TextField(db_column='First name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    middle_name = models.TextField(db_column='Middle Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_name = models.TextField(db_column='Last Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sexchild = models.TextField(db_column='SexChild', blank=True, null=True)  # Field name made lowercase.
    date_of_birth = models.TextField(db_column='Date of Birth', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    age = models.TextField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    possible_location = models.TextField(db_column='Possible location', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_of_separation_1 = models.TextField(db_column='Location of Separation 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_of_separation_2 = models.TextField(db_column='Location of Separation 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_of_separation_3 = models.TextField(db_column='Location of Separation 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fathers_first_name = models.TextField(db_column='Fathers First Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fathers_second_name = models.TextField(db_column='Fathers Second Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fathers_third_name = models.TextField(db_column='Fathers Third Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    is_father_alive = models.TextField(db_column='Is Father Alive', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mothers_first_name = models.TextField(db_column='Mothers First  Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mothers_second_name = models.TextField(db_column='Mothers Second Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mothers_third_name = models.TextField(db_column='Mothers Third  Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    is_mother_alive = models.TextField(db_column='Is mother alive', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fullname = models.CharField(max_length=500, blank=True, null=True)
    fatherfullname = models.CharField(max_length=100, blank=True, null=True)
    motherfullname = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enquerier'


class Tempkak(models.Model):
    individualid = models.CharField(db_column='IndividualID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    childfn = models.TextField(db_column='ChildFN', blank=True, null=True)  # Field name made lowercase.
    childmn = models.TextField(db_column='ChildMN', blank=True, null=True)  # Field name made lowercase.
    childln = models.TextField(db_column='ChildLN', blank=True, null=True)  # Field name made lowercase.
    cpimsname = models.TextField(db_column='CPIMSNAme', blank=True, null=True)  # Field name made lowercase.
    concatenatedname = models.CharField(db_column='ConcatenatedName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ll2 = models.CharField(max_length=50, blank=True, null=True)
    location_of_origin_2 = models.TextField(db_column='Location of Origin 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    totrace = models.TextField(db_column='ToTrace', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(max_length=50, blank=True, null=True)
    coolocationlevel1id = models.CharField(db_column='COOLocationLevel1ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    t = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tempkak'


class Tempkak1(models.Model):
    individualid = models.CharField(db_column='IndividualID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    childfn = models.TextField(db_column='ChildFN', blank=True, null=True)  # Field name made lowercase.
    childmn = models.TextField(db_column='ChildMN', blank=True, null=True)  # Field name made lowercase.
    childln = models.TextField(db_column='ChildLN', blank=True, null=True)  # Field name made lowercase.
    cpimsname = models.TextField(db_column='CPIMSNAme', blank=True, null=True)  # Field name made lowercase.
    concatenatedname = models.CharField(db_column='ConcatenatedName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ll2 = models.CharField(max_length=50, blank=True, null=True)
    location_of_origin_2 = models.TextField(db_column='Location of Origin 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    totrace = models.TextField(db_column='ToTrace', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(max_length=50, blank=True, null=True)
    coolocationlevel1id = models.CharField(db_column='COOLocationLevel1ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coalocationlevel3id = models.CharField(db_column='COALocationLevel3ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(max_length=3, blank=True, null=True)
    t = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tempkak1'


class Tempkak3(models.Model):
    individualid = models.CharField(db_column='IndividualID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    unhcr_id = models.TextField(db_column='UNHCR ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    childfn = models.TextField(db_column='ChildFN', blank=True, null=True)  # Field name made lowercase.
    childmn = models.TextField(db_column='ChildMN', blank=True, null=True)  # Field name made lowercase.
    childln = models.TextField(db_column='ChildLN', blank=True, null=True)  # Field name made lowercase.
    cpimsname = models.TextField(db_column='CPIMSNAme', blank=True, null=True)  # Field name made lowercase.
    concatenatedname = models.CharField(db_column='ConcatenatedName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ll2 = models.CharField(max_length=50, blank=True, null=True)
    location_of_origin_2 = models.TextField(db_column='Location of Origin 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    name_of_person_to_trace = models.TextField(db_column='Name of person to trace', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gender = models.CharField(max_length=50, blank=True, null=True)
    coolocationlevel1id = models.CharField(db_column='COOLocationLevel1ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coalocationlevel3id = models.CharField(db_column='COALocationLevel3ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(max_length=3, blank=True, null=True)
    t = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tempkak3'


class Temporarykak(models.Model):
    individualid = models.CharField(db_column='IndividualID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cpimsname = models.TextField(db_column='CPIMSNAme', blank=True, null=True)  # Field name made lowercase.
    concatenatedname = models.CharField(db_column='ConcatenatedName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    totrace = models.TextField(db_column='ToTrace', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(max_length=50, blank=True, null=True)
    coolocationlevel1id = models.CharField(db_column='COOLocationLevel1ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    t = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temporarykak'
