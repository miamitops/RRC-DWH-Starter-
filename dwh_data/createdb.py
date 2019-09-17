'''
Created on May 4, 2016

@author: miami

FIXME : Find a way of detecting character encoding
'''
import os,string,sys
import csv
from src import pypyodbc
from src.csv_recorder import Recoder
import time

directoryStart = r'files\import'
extensionList=['.csv']
predb = 'base_data'
connection = pypyodbc.connect('Driver={SQL Server};'
                                      'Server=localhost;'
                                      'Database=dwh_data;'
                                      'uid=sa;pwd=filthy6SCENT!!')
cursor = connection.cursor()

def process_csv_file(tb_name):
    try:
        '''check if table exists in the DB'''
        tb_check = cursor.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format(tb_name.replace('\'', '\'\'')))
        '''if table exists'''
        if tb_check.fetchone()[0] == 1:
            print 'exists'
            
        else:
            sys.stderr.write("database Table dbo.{} for will be created \n".format(tb_name))
            createQ = "CREATE TABLE {}(    [IndividualID] [nvarchar](255) NULL,    [Individualguid] [nvarchar](255) NULL,    [FamilyName] [nvarchar](255) NULL,    [GivenName] [nvarchar](255) NULL,    [ConcatenatedName] [nvarchar](255) NULL,    [RegistrationDate] [nvarchar](255) NULL,    [DateofBirth] [nvarchar](255) NULL,    [CountryOfOrigin] [nvarchar](255) NULL,    [AsylumCountryCode] [nvarchar](255) NULL,    [ArrivalDate] [nvarchar](255) NULL,    [gender] [nvarchar](255) NULL,    [Age] [nvarchar](255) NULL,    [IndividualAgeCohortCode] [nvarchar](255) NULL,    [NationalityCode] [nvarchar](255) NULL,    [RSDStatusCode] [nvarchar](255) NULL,    [ResettlementStatusCode] [nvarchar](255) NULL,    [VolRepStatusCode] [nvarchar](255) NULL,    [MarriageStatusCode] [nvarchar](255) NULL,    [EthnicityCode] [nvarchar](255) NULL,    [EducationLevelCode] [nvarchar](255) NULL,    [OccupationCode] [nvarchar](255) NULL,    [ProcessStatusCode] [nvarchar](255) NULL,    [RefugeeStatusCode] [nvarchar](255) NULL,    [FatherName] [nvarchar](255) NULL,    [MotherName] [nvarchar](255) NULL,    [SiteIDOwner] [nvarchar](255) NULL,    [SiteIDCreate] [nvarchar](255) NULL,    [CreateDate] [nvarchar](255) NULL,    [IsAnyGroupPrincipalRepresentative] [nvarchar](255) NULL,    [HasSPNeed] [nvarchar](255) NULL,    [ProcessingGroupTypeCode] [nvarchar](255) NULL,    [ProcessingGroupNumber] [nvarchar](255) NULL,    [CurrentRationCardNumber] [nvarchar](255) NULL,    [ProcessingGroupFileNumber] [nvarchar](255) NULL,    [ProcessingGroupSize] [nvarchar](255) NULL,    [ProcessingGroupStatusCode] [nvarchar](255) NULL,    [ProcessGroupStatusDate] [nvarchar](255) NULL,    [ProcessingGroupRegistrationDate] [nvarchar](255) NULL,    [IndividualSequenceNumber] [nvarchar](255) NULL,    [PrincipalRepresentative] [nvarchar](255) NULL,    [RelationshipToPrincipalRepresentative] [nvarchar](255) NULL,    [RelationshipText] [nvarchar](255) NULL,    [COALocationLevel1ID] [nvarchar](255) NULL,    [COALocationLevel2ID] [nvarchar](255) NULL,    [COALocationLevel3ID] [nvarchar](255) NULL,    [COALocationLevel4ID] [nvarchar](255) NULL,    [COALocationLevel5ID] [nvarchar](255) NULL,    [COOLocationLevel1ID] [nvarchar](255) NULL,    [COOLocationLevel2ID] [nvarchar](255) NULL,    [COOLocationLevel3ID] [nvarchar](255) NULL,    [COOLocationLevel4ID] [nvarchar](255) NULL,    [COOLocationLevel5ID] [nvarchar](255) NULL,    [VulnerabilityCode] [nvarchar](255) NULL,    [VulnerabilityDetailsCode] [nvarchar](255) NULL) ON [PRIMARY]".format(tb_name) 
            cursor.execute(createQ)
        '''skip'''
        '''else create it'''
	''''''
	connection.commit() 
    finally:
        
        print("Tables created")

def walker ( directoryStart , extensionList ) :
    os.path.walk( directoryStart, walker_callback, extensionList )
    connection.close()

def walker_callback ( extensionList , directory, files) :
    sys.stderr.write("Scanning {} at {} \n".format(directory, time.asctime( time.localtime(time.time()) )))
    cur_dir = os.path.split(directory)[1]
    if cur_dir == "Tanzania":
        store_db = predb+'_tan'
    elif cur_dir == "SSD":
        store_db = predb+'_ssd'
    elif cur_dir == "Burundi":
        store_db = predb+'_bdi'
    elif cur_dir == "Sudan":
        store_db = predb+'_sud'
    elif cur_dir == "Djibouti":
        store_db = predb+'_djb'
    elif cur_dir == "Kenya":
        store_db = predb+'_ken'
    elif cur_dir == "Uganda":
        store_db = predb+'_uga'
    elif cur_dir == "Ethiopia":
        store_db = predb+'_eth'
    else:
        store_db = "None"
    if store_db == "None":
        #print "Country not in list"
        '''This is not a country so dont create a DB Table'''
        sys.stderr.write("""{} is not a country and therefore NO Table will be created \n if you believe this is an error please add it to the list of countries \n """.format(cur_dir))
    else:
        process_csv_file(store_db)

walker( directoryStart, extensionList) 
