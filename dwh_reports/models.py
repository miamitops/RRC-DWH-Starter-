from django.db import models
'''Reports Models'''
from report_builder.models import *
class reportTypes(models.Model):
    id = models.AutoField(blank=False, null=False, db_column='id', primary_key=True)
    name = models.CharField(db_column='s_name', max_length=254)
    description = models.CharField(db_column='s_desc', max_length=254)
    class Meta():
        managed = True
        db_table = 't_report_types'
        verbose_name = "DWH Report Types"
class dwhReport(Report):
    ''''''
    mn = 'MN'
    yr = 'YR'
    dateOptions = (
                   (mn, 'MONTH' ),
                   (yr, 'YEAR')
                   )
    dateOperation = models.CharField(db_column='operation', max_length=2, choices=dateOptions, default=mn)
    raw_data = models.CharField(db_column='raw_data', max_length=254,  null=True, blank=True)
    '''fields
    filters'''
    class ReportBuilder:
        extra = ('raw_data')
        filters = ('dateOperation')
    
    class Meta():
        managed = True
        db_table = 't_dwh_reports'
        verbose_name = "DWH Report"
class dwhReportData(models.Model):
    id = models.AutoField(db_column='i_id', primary_key=True, blank=False, null=False)
    reportId = models.ForeignKey(dwhReport, db_column='fk_report_id')
    dataType = models.ForeignKey(reportTypes, db_column='fk_type')
    dataTitle = models.CharField(db_column='s_title', null=False, max_length=60)
    dataDescription = models.CharField(db_column='s_desc', max_length=254)
    x_axis = models.CharField(db_column='x_axis', max_length=254)
    y_axes = models.CharField(db_column='x_axes', max_length=254)
    created = models.DateTimeField(db_column='dt_created', auto_now=True)
    updated = models.DateTimeField(db_column='dt_updated', auto_now=True)

    class Meta():
        managed = True
        db_table = 't_dwh_report_data'
        verbose_name = 'Report Data'
        app_label = 'dwh report'
class dwhReportView(models.Model):
    ''''''
    class Meta():
        managed = True
        db_table = 't_dwh_report_view'
        verbose_name = 'Report Views'
class dwhFormat(models.Model):
    ''''''
    tid = models.AutoField(db_column='i_id', primary_key=True, blank=False, null=False)
    fName = models.CharField(db_column='s_name', max_length=254)
    fDescription = models.CharField(db_column='s_desc', max_length=254)
    class Meta():
        managed = True
        db_table = 't_dwh_report_format'
        verbose_name = 'Format Type'
