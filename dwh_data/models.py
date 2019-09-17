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
from django.forms import ModelForm
from countries.models import dwhCountry

class IndividualsManager(models.Manager):
    def with_counts(self):
        from django.db import connections
        cursor = connections['dwh_data'].cursor()
        cursor.execute("""SELECT CountryOfOrigin, COUNT(CountryOfOrigin) as TT
        FROM t_individuals
        WHERE AsylumCountryCode = 'BDI'
        AND ProcessStatusCode = 'A'
        GROUP BY CountryOfOrigin
        ORDER BY TT DESC
        """)
        result_list = []
        total_list = []
        for row in cursor.fetchall():
            country = row[0]
            total = row[1]
            result_list.append(country)
            total_list.append(total)
        return result_list, total_list

    def get_queryset(self):
        return super(IndividualsManager, self).get_queryset().filter()
    ''''''
class BaseDataBdi(models.Model):
    individualid = models.CharField(db_column='IndividualID', max_length=255, blank=True, null=False, primary_key=True)  # Field name made lowercase.
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
    
    def __unicode__(self):
        return unicode(self.concatenatedname)
    def retreiveByIndividualID(self, indiviDualId):
        return self.individuals.get(individualid=indiviDualId)

    class Meta:
        managed = True
        db_table = 'base_data'
class BaseDataManager(models.Manager):
    def with_counts(self):
        from django.db import connection
        cursor = connection['dwh_data'].cursor()
        cursor.execute("""
            SELECT individualid, COUNT(*)
            FROM base_data_bdi
            GROUP BY individualid
            ORDER BY individualid DESC
            LIMIT 5""")
        result_list = []
        for row in cursor.fetchall():
            p = self.model(individualid=row[0])
            p.num_responses = row[1]
            result_list.append(p)
        return result_list
    def get_queryset(self):
        return super(BaseDataManager, self).get_queryset().filter()

class BaseData(models.Model):
    individualguid = models.CharField(db_column='Individualguid', max_length=255, blank=False, null=False, primary_key=True, verbose_name = 'ID')  # Field name made lowercase.
    individualid = models.CharField(db_column='IndividualID', max_length=255)  # Field name made lowercase.
    familyname = models.CharField(db_column='FamilyName', max_length=255, blank=True, null=True, verbose_name='Family Name')  # Field name made lowercase.
    givenname = models.CharField(db_column='GivenName', max_length=255, blank=True, null=True, verbose_name = 'Given Name')  # Field name made lowercase.
    concatenatedname = models.CharField(db_column='ConcatenatedName', max_length=255, blank=True, null=True, verbose_name='Full Names')  # Field name made lowercase.
    registrationdate = models.CharField(db_column='RegistrationDate', max_length=255, blank=True, null=True, verbose_name='Registration Date')  # Field name made lowercase.
    dateofbirth = models.CharField(db_column='DateofBirth', max_length=255, blank=True, null=True, verbose_name='Date of Birth')  # Field name made lowercase.
    countryoforigin = models.CharField(db_column='CountryOfOrigin', max_length=255, blank=True, null=True, verbose_name='Country of Origin')  # Field name made lowercase.
    asylumcountrycode = models.CharField(db_column='AsylumCountryCode', max_length=255, blank=True, null=True, verbose_name='Country of Asylum')  # Field name made lowercase.
    arrivaldate = models.CharField(db_column='ArrivalDate', max_length=255, blank=True, null=True, verbose_name = 'Arrival Date')  # Field name made lowercase.
    gender = models.CharField(max_length=255, blank=True, null=True, verbose_name = 'Gender')
    age = models.CharField(db_column='Age', max_length=255, blank=True, null=True, verbose_name = 'Age')  # Field name made lowercase.
    individualagecohortcode = models.CharField(db_column='IndividualAgeCohortCode', max_length=255, blank=True, null=True, verbose_name = 'Age Group')  # Field name made lowercase.
    nationalitycode = models.CharField(db_column='NationalityCode', max_length=255, blank=True, null=True, verbose_name = 'Nationality')  # Field name made lowercase.
    rsdstatuscode = models.CharField(db_column='RSDStatusCode', max_length=255, blank=True, null=True, verbose_name = 'RSD Status')  # Field name made lowercase.
    resettlementstatuscode = models.CharField(db_column='ResettlementStatusCode', max_length=255, blank=True, null=True, verbose_name = 'Resettlement Status Code')  # Field name made lowercase.
    volrepstatuscode = models.CharField(db_column='VolRepStatusCode', max_length=255, blank=True, null=True, verbose_name = 'Voluntary repatriation status')  # Field name made lowercase.
    marriagestatuscode = models.CharField(db_column='MarriageStatusCode', max_length=255, blank=True, null=True, verbose_name = 'Marriage status Code')  # Field name made lowercase.
    ethnicitycode = models.CharField(db_column='EthnicityCode', max_length=255, blank=True, null=True, verbose_name = 'Ethnicity')  # Field name made lowercase.
    educationlevelcode = models.CharField(db_column='EducationLevelCode', max_length=255, blank=True, null=True, verbose_name = 'Education Level')  # Field name made lowercase.
    occupationcode = models.CharField(db_column='OccupationCode', max_length=255, blank=True, null=True, verbose_name = 'Occupation')  # Field name made lowercase.
    processstatuscode = models.CharField(db_column='ProcessStatusCode', max_length=255, blank=True, null=True, verbose_name = 'Process Status')  # Field name made lowercase.
    refugeestatuscode = models.CharField(db_column='RefugeeStatusCode', max_length=255, blank=True, null=True, verbose_name = 'Refugee Status')  # Field name made lowercase.
    fathername = models.CharField(db_column='FatherName', max_length=255, blank=True, null=True, verbose_name = 'Fathers Name')  # Field name made lowercase.
    mothername = models.CharField(db_column='MotherName', max_length=255, blank=True, null=True, verbose_name = 'Mothers Name')  # Field name made lowercase.
    siteidowner = models.CharField(db_column='SiteIDOwner', max_length=255, blank=True, null=True, verbose_name = 'Site Owner')  # Field name made lowercase.
    siteidcreate = models.CharField(db_column='SiteIDCreate', max_length=255, blank=True, null=True, verbose_name = 'Site created')  # Field name made lowercase.
    createdate = models.CharField(db_column='CreateDate', max_length=255, blank=True, null=True, verbose_name = 'Date created')  # Field name made lowercase.
    hasspneed = models.CharField(db_column='HasSPNeed', max_length=255, blank=True, null=True, verbose_name = 'Has special need')  # Field name made lowercase.
    d_arrival = models.DateTimeField(db_column='n_ArrivalDate',null=True, verbose_name = 'Arrival Date')
    d_registration = models.DateTimeField(db_column='n_RegistrationDate', null=True,verbose_name = 'Registration Date')
    d_dob = models.DateTimeField(db_column='n_DateOfBirth', null=True,verbose_name = 'Birth Date')
    objects = BaseDataManager

    def __unicode__(self):
        return unicode(self.concatenatedname)
    class ReportBuilder:
        exclude =()  # Lists or tuple of excluded fields
        fields = ['countryoforigin','nationalitycode', 'asylumcountrycode', 'arrivaldate', 'registrationdate', 'processstatuscode', 'individualguid','refugeestatuscode', 'gender',  'individualagecohortcode']   # Explicitly allowed fields
        extra = ('arrivaldate', )    # List extra fields (useful for methods)
    class Meta:
        managed = True
        db_table = 't_individuals'
        verbose_name = "Individual Information"
        
class BDGroup(models.Model):
    processinggrouptypecode = models.CharField(db_column='ProcessingGroupTypeCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    processinggroupnumber = models.CharField(db_column='ProcessingGroupNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    currentrationcardnumber = models.CharField(db_column='CurrentRationCardNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    processinggroupfilenumber = models.CharField(db_column='ProcessingGroupFileNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    processinggroupsize = models.CharField(db_column='ProcessingGroupSize', max_length=255, blank=True, null=True)  # Field name made lowercase.
    processinggroupstatuscode = models.CharField(db_column='ProcessingGroupStatusCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    processgroupstatusdate = models.CharField(db_column='ProcessGroupStatusDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    processinggroupregistrationdate = models.CharField(db_column='ProcessingGroupRegistrationDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    individualsequencenumber = models.CharField(db_column='IndividualSequenceNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fkindividualguid = models.OneToOneField(BaseData, primary_key=True)
    isanygroupprincipalrepresentative = models.CharField(db_column='IsAnyGroupPrincipalRepresentative', max_length=2, blank=True, null=True)  # Field name made lowercase.
    principalrepresentative = models.CharField(db_column='PrincipalRepresentative', max_length=10, blank=True, null=True)  # Field name made lowercase.
    relationshiptoprincipalrepresentative = models.CharField(db_column='RelationshipToPrincipalRepresentative', max_length=20, blank=True, null=True)  # Field name made lowercase.
    relationshiptext = models.CharField(db_column='RelationshipText', max_length=100, blank=True, null=True)  # Field name made lowercase.
    
    def __unicode__(self):
        return unicode(self.fkindividualguid)
    class ReportBuilder:
        exclude =()  # Lists or tuple of excluded fields
        fields = ['']
        extra = ()
    class Meta:
        managed = True
        db_table = 't_group'
        verbose_name = 'Group Address'
        
class BDCOOAddress(models.Model):
    fkindividualguid = models.OneToOneField(BaseData, primary_key=True)
    coolocationlevel1id = models.CharField(db_column='COOLocationLevel1ID', max_length=255, blank=True, null=True, verbose_name ="Country of origin1")  # Field name made lowercase.
    coolocationlevel2id = models.CharField(db_column='COOLocationLevel2ID', max_length=255, blank=True, null=True, verbose_name ="Country of origin2")  # Field name made lowercase.
    coolocationlevel3id = models.CharField(db_column='COOLocationLevel3ID', max_length=255, blank=True, null=True, verbose_name ="Country of origin3")  # Field name made lowercase.
    coolocationlevel4id = models.CharField(db_column='COOLocationLevel4ID', max_length=255, blank=True, null=True, verbose_name ="Country of origin4")  # Field name made lowercase.
    coolocationlevel5id = models.CharField(db_column='COOLocationLevel5ID', max_length=255, blank=True, null=True, verbose_name ="Country of origin5")  # Field name made lowercase.
    
    def __unicode__(self):
        return unicode(self.fkindividualguid, self.coolocationlevel1id)
    class ReportBuilder:
        exclude =()  # Lists or tuple of excluded fields
        fields = ['coolocationlevel1id', 'coolocationlevel2id', 'coolocationlevel3id', 'coolocationlevel4id', 'coolocationlevel5id']
        extra = ('')
    class Meta:
        managed = True
        db_table = 't_coo_address'
        verbose_name = 'Country Of Origin Address'
        
class BDCOAAddress(models.Model):
    coalocationlevel1id = models.CharField(db_column='COALocationLevel1ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coalocationlevel2id = models.CharField(db_column='COALocationLevel2ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coalocationlevel3id = models.CharField(db_column='COALocationLevel3ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coalocationlevel4id = models.CharField(db_column='COALocationLevel4ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coalocationlevel5id = models.CharField(db_column='COALocationLevel5ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fkindividualguid = models.OneToOneField(BaseData, primary_key=True)
    
    def __unicode__(self):
        return unicode(self.fkindividualguid)
    class Meta:
        managed = True
        db_table = 't_coa_address'
        verbose_name = 'Country of Asylum Address'

class BDVulnerability(models.Model):
    vulnerabilitycode = models.CharField(db_column='VulnerabilityCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    vulnerabilitydetailscode = models.CharField(db_column='VulnerabilityDetailsCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fkindividualguid = models.ForeignKey(BaseData)
    dt_update = models.CharField(max_length=255, blank=True, null=True)
    def __unicode__(self):
        return unicode(self.fkindividualguid)
    class Meta:
        managed = True
        db_table = 't_vuln_status'
        verbose_name = 'Vulnerability Status'

     
class FormVulnerability(ModelForm):
    class Meta:
        model = BDVulnerability
        fields = ['vulnerabilitycode', 'vulnerabilitydetailscode', 'dt_update']
class allDataModels():
    COAAddress = BDCOAAddress
        



