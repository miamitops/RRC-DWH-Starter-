from django.db import models

class situationsManager(models.Manager):
    def get_queryset(self):
        return super(situationsManager, self).get_queryset().filter(isActive=True)
    def get_by_id(self, id):
        return super(situationsManager, self).get(situationID='{}'.format(id), isActive=True)
class dwhSituations(models.Model):
    situationID = models.CharField(db_column='situationID', max_length=4, blank=True, null=False, primary_key=True)
    countryName = models.CharField(db_column='countryName', max_length=255, blank=True, null=True)
    countryBorder = models.CharField(db_column='kmlBorder', max_length=255, blank=True, null=True)
    isActive = models.BooleanField(db_column='active', default=False)
    situations = models.Manager()
    active = situationsManager()
    def __unicode__(self):
        return unicode(self.countryName)

    class Meta:
        managed = True
        db_table = 'c_situations'
        verbose_name = 'DWH Situations'
class situationOverview(models.Model):
    pkStatId = models.IntegerField(db_column='statID', primary_key=True)
    fksituationid = models.ForeignKey(dwhSituations)
    dtCreate = models.DateTimeField(db_column='dtCreate', auto_now_add=True, blank=True)
    dtUpdate = models.DateTimeField(db_column='dtUpdate', auto_now_add=True, blank=True)
    dtStatFrom = models.DateTimeField(db_column='dtStatFrom', blank=False)
    dtStatTo = models.DateTimeField(db_column='dtStatTo', blank=False)
    def __unicode__(self):
        return unicode(self.fksituationid)
    
    class Meta:
        managed = True
        db_table = 'c_situations_overview'
        verbose_name = 'DWH Situations overview'