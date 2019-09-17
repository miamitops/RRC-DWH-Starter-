from django.db import models
from countries.models import dwhCountry
'''Reports Models'''
from report_builder.models import *
class importTypes(models.Model):
    id = models.AutoField(blank=False, null=False, db_column='id', primary_key=True)
    name = models.CharField(db_column='s_name', max_length=254)
    description = models.CharField(db_column='s_desc', max_length=254)
    class Meta:
        managed = True
        db_table = 't_dwh_import_types'
        verbose_name = "DWH Import Types"
        
class DWHImportFile(models.Model):
     fileid = models.AutoField(db_column='i_file_id', primary_key=True, blank=False, null=False)
     fcountry = models.ForeignKey(dwhCountry, db_column='fk_country_id', null=False, blank=False, verbose_name='Country')
     progressinstance = models.CharField(db_column='s_progress_instance', max_length=254, blank=False, null=False, verbose_name='Progress Instance')
     dategenerated = models.DateTimeField(db_column='d_generated', null=False, blank=False, verbose_name='Date Generated')
     dateimport = models.DateTimeField(db_column='d_imported', null=False, blank=False, verbose_name='Date Imported')
     importstatus = models.CharField(
                    max_length=5,
                    choices=(
                        ('succs', 'Successfull'),
                        ('faile', 'Failed'),
                        ('succe', 'Successfull but with errors')
                    ),
                    blank=True
                )
     class Meta:
         managed = True
         db_table = 't_dwh_import_files'
         verbose_name = 'CSV Import History'
class DWHImportLog(Report):
    ''''''
    logid = models.AutoField(db_column='log_id', primary_key=True)
    fileid = models.ForeignKey(DWHImportFile, db_column='file_id')
    loglevel = models.CharField(db_column='log_level',
                                max_length=5,
                                choices = (
                                    ('f', 'File'),
                                    ('r', 'Row')
                                ),
                                blank = True
                            )
    logmessage = models.CharField(db_column='log_message', blank=True, max_length=1200)

    
    class Meta:
        managed = True
        db_table = 't_dwh_import_logs'
        verbose_name = "DWH Import Log"
        
class DWHImportDaemon():
    ''''''
    
    class Meta:
        managed = True
        db_table = 't_dwh_import_daemon'
        verbose_name = "DWH Import Daemon Process"
