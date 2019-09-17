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
predb = 'dbo.base_data'
db = pypyodbc
dbs = 'Driver={SQL Server};' 'Server=localhost;' 'Database=dwh_data;' 'uid=sa;pwd=filthy6SCENT!!'

def migrate_db(tb_name):
    connection = db.connect('Driver={SQL Server};'
                                      'Server=localhost;'
                                      'Database=dwh_data;'
                                      'uid=sa;pwd=filthy6SCENT!!')
    
    cursor = connection.cursor()
    allRowsSQL = """SELECT 
        CAST(Individualguid AS VARCHAR)
        ,CAST(IndividualID AS VARCHAR) 
        ,FamilyName 
        ,GivenName
        ,ConcatenatedName
        ,CAST(RegistrationDate  AS VARCHAR)
        ,CAST( DateofBirth AS VARCHAR)
        ,CAST(CountryOfOrigin AS VARCHAR)
        ,CAST(AsylumCountryCode AS VARCHAR)
        ,CAST(ArrivalDate   AS VARCHAR)
        ,CAST(gender AS VARCHAR)
        ,CAST(Age AS VARCHAR) 
        ,CAST(IndividualAgeCohortCode AS VARCHAR)
        ,CAST(NationalityCode AS VARCHAR) 
        ,CAST(RSDStatusCode  AS VARCHAR)
        ,CAST(ResettlementStatusCode AS VARCHAR)
        ,CAST(VolRepStatusCode AS VARCHAR)
        ,CAST(MarriageStatusCode AS VARCHAR)
        ,CAST(EthnicityCode AS VARCHAR)
        ,CAST(EducationLevelCode AS VARCHAR)
        ,CAST(OccupationCode AS VARCHAR)
        ,CAST(ProcessStatusCode AS VARCHAR)
        ,CAST(RefugeeStatusCode AS VARCHAR)
        ,CAST(FatherName  AS VARCHAR)
        ,CAST(MotherName AS VARCHAR)
        ,CAST(SiteIDOwner AS VARCHAR)
        ,CAST(SiteIDCreate AS VARCHAR)
        ,CAST(CreateDate AS VARCHAR) 
        ,CAST(IsAnyGroupPrincipalRepresentative  AS VARCHAR)
        ,CAST(HasSPNeed AS VARCHAR)
        ,CAST(PrincipalRepresentative AS VARCHAR)
        ,CAST(RelationshipToPrincipalRepresentative AS VARCHAR)
        ,CAST(RelationshipText AS VARCHAR)
        FROM {}""".format(tb_name)
    cursor.execute(allRowsSQL)
    for row in cursor:
        connection2 = db.connect(dbs)
        tb1IId = row[1]
        tb_2 ='t_individuals'
        '''
        do select
        '''
        confirmQuery = "SELECT COUNT(Individualguid) FROM {} WHERE Individualguid = '{}'".format(tb_2, tb1IId)
        cursor2 = connection2.cursor()
        confirmQuery = cursor2.execute(confirmQuery)
        numFound = confirmQuery.next()[0]
        
        if numFound == 0:
            insertQ = '''INSERT INTO t_individuals(
            [Individualguid]
      ,[IndividualID]
      ,[FamilyName]
      ,[GivenName]
      ,[ConcatenatedName]
      ,[RegistrationDate]
      ,[DateofBirth]
      ,[CountryOfOrigin]
      ,[AsylumCountryCode]
      ,[ArrivalDate]
      ,[gender]
      ,[Age]
      ,[IndividualAgeCohortCode]
      ,[NationalityCode]
      ,[RSDStatusCode]
      ,[ResettlementStatusCode]
      ,[VolRepStatusCode]
      ,[MarriageStatusCode]
      ,[EthnicityCode]
      ,[EducationLevelCode]
      ,[OccupationCode]
      ,[ProcessStatusCode]
      ,[RefugeeStatusCode]
      ,[FatherName]
      ,[MotherName]
      ,[SiteIDOwner]
      ,[SiteIDCreate]
      ,[CreateDate]
      ,[IsAnyGroupPrincipalRepresentative]
      ,[HasSPNeed]
      ,[RelationshipText]
      ,[PrincipalRepresentative]
      ,[RelationshipToPrincipalRepresentative]
      ) VALUES {}'''.format(row)
            cursor2.execute(insertQ)
            '''
            print insertQ'''
        else:
            print "{} record exists for {}".format(numFound, tb1IId)
        '''
        if exists update or skip
        
        '''
        '''
        else insert
        '''

migrate_db('base_data_bdi') 
