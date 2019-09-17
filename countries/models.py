from __future__ import unicode_literals
from django.db import models
from datetime import datetime, date
import dateutil.relativedelta

class countriesManager(models.Manager):
    def get_queryset(self):
        return super(countriesManager, self).get_queryset().filter(isEnabled=True)
class countryStatsManager(models.Manager):
    def get_queryset(self):
        return super(countriesManager, self).get_queryset()
    def get_reportId(self, countryId):
        ''''''
        stats= super(countryStatsManager, self).get_queryset().get(fkCountryId = countryId)
    def get_countryStatWithArr(self, sid):
        arrivals = self.get_arrivalStats(sid)
        threeMonthsStats = self.get_arrivalStatsLastThreeMonths(sid)
        return arrivals, threeMonthsStats
    def get_arrivalStats(self, sid):
        arrStats = dwhStatsArrivals.arrivals.filter(fkStatId = sid)
        return arrStats
    def get_arrivalStatsLastThreeMonths(self, sid):
        d = datetime.strptime("{}".format(date.today()), "%Y-%m-%d")
        d2 = d - dateutil.relativedelta.relativedelta(months=3)
        threeMonthsWeekNum = d2.isocalendar()[1]
        '''Change this to Pick year Automatically also include calculation for previous years for date that are less than three months
        from the start of the year'''
        arrStats = dwhStatsArrivals.arrivals.filter(fkStatId = sid, arrivalWeek__gte = threeMonthsWeekNum, arrivalYear = 2016)
        return arrStats
    def get_arrivalStatsThisYear(self, sid, aYear):
        arrStats = dwhStatsArrivals.arrivals.filter(fkStatId = sid, arrivalYear = aYear)
        return arrStats
    
class dwhCountry(models.Model):
    countryID = models.CharField(db_column='countryID', max_length=4, blank=True, null=False, primary_key=True)  # Field name made lowercase.
    countryName = models.CharField(db_column='countryName', max_length=255, blank=True, null=True)
    countryBorder = models.CharField(db_column='kmlBorder', max_length=255, blank=True, null=True)
    isEnabled = models.BooleanField(db_column='enabled', default=False)
    countries = models.Manager()
    active = countriesManager()
    def __unicode__(self):
        return unicode(self.countryName)

    class Meta:
        managed = True
        db_table = 'conf_countries'
        verbose_name = 'Countries'
class dwhCountryStats(models.Model):
    statId = models.IntegerField(db_column='stat_id', blank=False, null=False, primary_key=True)
    fkCountryId = models.ForeignKey(dwhCountry, on_delete=models.CASCADE)
    TotalPop = models.IntegerField(db_column='i_tot_pop', blank=False, null=False,)
    TotalMPop = models.IntegerField(db_column='i_tot_m_pop', blank=False, null=False,)
    TotalFPop = models.IntegerField(db_column='i_tot_f_pop', blank=False, null=False,)
    TotalUnaccompanied = models.IntegerField(db_column='i_tot_um_pop', blank=False, null=False)
    demographics = models.CharField(db_column='s_demographics', max_length=255, blank=True, null=True)
    ageSex = models.CharField(db_column='s_age_sex', max_length=255, blank=True, null=True)
    popGender = models.CharField(db_column='s_gender', max_length=255, blank=True, null=True)
    dtUpdated = models.DateTimeField(default=datetime.now, db_column='dt_updated')
    dtUpdated = models.DateTimeField(default=datetime.now, db_column='dt_created')
    countrystats = models.Manager()
    statsManager = countryStatsManager()
    def __unicode__(self):
        return unicode(self.fkCountryId)
    
    class Meta:
        managed = True
        db_table = 'dwh_country_stats'
        verbose_name = 'Country Statistics'
        
class dwhStatsArrivals(models.Model):
    statIdArrival = models.IntegerField(db_column='arrival_stat_id',  blank=False, null=False, primary_key=True)
    fkStatId = models.ForeignKey(dwhCountryStats, on_delete=models.CASCADE)
    arrivalYear = models.IntegerField(db_column='i_arr_year', blank=False, null=False)
    arrivalWeek = models.IntegerField(db_column='i_arr_week', blank=False, null=False)
    arrivalTotalWeek = models.IntegerField(db_column='i_arr_total', blank=False, null=False)
    arrivalDemsWeek = models.CharField(db_column='s_demographics', max_length=255, blank=True, null=True)
    arrivalAgeSexWeek = models.CharField(db_column='s_age_sex', max_length=255, blank=True, null=True)
    arrivalMale = models.IntegerField(db_column='i_arr_m', blank=False, null=False, verbose_name='Male Arrivals')
    arrivalFemale = models.IntegerField(db_column='i_arr_f', blank=False, null=False, verbose_name='Female Arrivals')
    '''dtUpdated = models.DateTimeField(default=datetime.now, db_column='dt_updated')'''
    dtCreated = models.DateTimeField(default=datetime.now, db_column='dt_created')
    arrivals = models.Manager()
    arrManager = countryStatsManager()
    
    class Meta:
        managed = True
        db_table = 'dwh_c_arrival_stats'
        verbose_name = 'Arrival Trends'
class dwhStatsRegistered(models.Model):
    statRegId = models.IntegerField(db_column='arrival_stat_id',  blank=False, null=False, primary_key=True)
    StatId = models.ForeignKey(dwhCountryStats, on_delete=models.CASCADE)
    regYear = models.IntegerField(db_column='i_arr_year', blank=False, null=False)
    regWeek = models.IntegerField(db_column='i_arr_week', blank=False, null=False)
    regTotalWeek = models.IntegerField(db_column='i_arr_total', blank=False, null=False)
    regDemsWeek = models.CharField(db_column='s_demographics', max_length=255, blank=True, null=True)
    regAgeSexWeek = models.CharField(db_column='s_age_sex', max_length=255, blank=True, null=True)
    regMale = models.IntegerField(db_column='i_arr_m', blank=False, null=False, verbose_name='Male Arrivals')
    regFemale = models.IntegerField(db_column='i_arr_f', blank=False, null=False, verbose_name='Female Arrivals')
    dtUpdated = models.DateTimeField(default=datetime.now, db_column='dt_updated')
    dtCreated = models.DateTimeField(default=datetime.now, db_column='dt_created')
    registration = models.Manager()
    regManager = countryStatsManager()
    
    class Meta:
        managed = True
        db_table = 'dwh_c_registration_stats'
        verbose_name = 'Registration Trends'