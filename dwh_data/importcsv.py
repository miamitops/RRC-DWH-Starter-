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
import datetime
import logging
import signal
import re


directoryStart = r'files\import\Uganda'
extensionList=['.csv']
predb = 'dbo.base_data'
sdbtxt = 'Driver={SQL Server};''Server=localhost;''Database=dwh_data;''uid=sa;pwd=filthy6SCENT!!'
logging.basicConfig(filename='csvimport.log', level=logging.INFO)
localtime = time.asctime( time.localtime(time.time()) )
dest_tb ='t_individuals'

class CSVStructureError(Exception):
     def __init__(self, value):
         self.value = value
     def __str__(self):
         return repr(self.value)
    
def signal_handler(signal, frame):
        logging.info('{} : You pressed Ctrl+C!'.format(localtime))
        sys.exit(0)
        signal.pause()
def rowexists(operation, confirmid, table='t_individuals'):
    '''checks if a row exists in the db'''
    '''operation:
    primary will check the primary for existance of individualguid 
    secondary will check relation table if fkindividualguid_id exists'''
    connection = pypyodbc.connect(sdbtxt)
    cursor = connection.cursor()
    if operation == 'primary':
        idname = 'Individualguid'
    elif operation == 'secondary':
        idname = 'fkindividualguid_id'
    confirmQuery = "SELECT count({}) FROM {} WHERE {} ='{}' ".format(idname, table, idname, confirmid)
    confirmation = cursor.execute(confirmQuery)
    if confirmation.next()[0] != 0:
        return True
    else:
        return False
    connection.close()



def process_csv_file(csvfile, tb_name):
    signal.signal(signal.SIGINT, signal_handler)
    connection = pypyodbc.connect(sdbtxt)
    cursor = connection.cursor()

    
    with open(csvfile,'rb') as f:
        try:
            logging.info('{} :Reading csv: {}'.format(localtime,csvfile))
            sr = Recoder(f, 'ISO-8859-1', 'utf-8')
            '''with open(sr) as filecsv:'''
            recsv = csv.reader(sr, delimiter=',')
            columns = next(recsv)
            if len(columns)==54 and 'IndividualID' in columns[0] and 'VulnerabilityDetailsCode' in columns[53]:
                '''perform further verification'''
                print"verification passed"
            else:
                '''
                Raise Exception
                '''
                logging.error("{} {} is not a valid CSV Format".format(localtime,csvfile))
                raise CSVStructureError('Unsuported CSV Suplied')
                return
            for row in recsv:
                if len(row) != 54:
                     print "faulty row {}".format(row)
                     logging.error("faulty row {} passed as value".format(row))
                     continue
                crow =[]
                for col in row:
                    ccol = re.sub(' +',' ', col)
                    crow.append(ccol)
                guid = crow[1]
                
                connection2 = pypyodbc.connect(sdbtxt)
                cursor2 = connection2.cursor()
                slicer = crow[:28]
                dt = datetime.datetime.strptime(slicer[6], "%b %d %Y %H:%M%p")

                                
                hasPneed = crow[29]
                slicer.insert(28, hasPneed)
                
 
                groupInfo = crow[28:42]
                groupInfo.insert(0,guid)
                
                COAInfo = crow[42:47]
                COAInfo.insert(5,guid)
                
                COOInfo = crow[47:52]
                COOInfo.insert(5,guid)
                
                VulnInfo = crow[-2:]
                VulnInfo.insert(2, guid)
                VulnInfo.insert(3, time.strftime('%Y-%m-%d %H:%M:%S'))

                del(groupInfo[1])

                if rowexists('primary', guid):
                   '''Update individuals table if changed'''
                   usttmt = ''
                   '''Age,IndividualAgeCohortCode,RSDStatusCode,ResettlementStatusCode,VolRepStatusCode,
                   MarriageStatusCode,EthnicityCode,EducationLevelCode,OccupationCode,
                   ProcessStatusCode,RefugeeStatusCode'''
                   age = slicer[11]
                   gender = slicer[10]
                   ageCohort = slicer[12]
                   rsdStatusCode = slicer[15]
                   resettlementStatus = slicer[16]
                   volrepStatus = slicer[17]
                   educationLevel = slicer[19]
                   occupation = slicer[20]
                   processStatus = slicer[21]
                   refugeeStatus = slicer[22]
                   if age == '' or age == '-' or age == ' ':
                        usttmt += ''
                   else:
                        usttmt += 'Age = \'{}\', '.format(age)
                   
                   if ageCohort == '' or age == '-' or ageCohort == ' ':
                        usttmt += ''
                   else:
                        usttmt += 'IndividualAgeCohortCode = \'{}\', '.format(ageCohort)
                        
                   if rsdStatusCode == '' or rsdStatusCode == '-' or rsdStatusCode == ' ':
                        usttmt += ''
                   else:
                        usttmt += 'RSDStatusCode = \'{}\', '.format(rsdStatusCode)
                   
                   if resettlementStatus == '' or resettlementStatus == '-' or resettlementStatus == ' ':
                        usttmt += ''
                   else:
                        usttmt += 'ResettlementStatusCode = \'{}\', '.format(resettlementStatus)
                   
                   if volrepStatus == '' or volrepStatus == '-' or volrepStatus == ' ':
                        usttmt += ''
                   else:
                        usttmt += 'VolRepStatusCode = \'{}\', '.format(volrepStatus)
                   
                   if educationLevel == '' or educationLevel == '-' or educationLevel == ' ':
                        usttmt += ''
                   else:
                        usttmt += 'EducationLevelCode = \'{}\', '.format(educationLevel)
                   
                   if occupation == '' or occupation == '-' or occupation == ' ':
                        usttmt += ''
                   else:
                        usttmt += 'OccupationCode = \'{}\', '.format(occupation)
                   
                        
                   if processStatus == '' or processStatus == '-' or processStatus == ' ':
                        usttmt += ''
                   else:
                        usttmt += 'ProcessStatusCode = \'{}\', '.format(processStatus)
                   
                   if refugeeStatus == '' or refugeeStatus == '-' or refugeeStatus == ' ':
                        usttmt += ''
                   else:
                        usttmt += 'RefugeeStatusCode = \'{}\', '.format(refugeeStatus)
                   
                             
                   inst = usttmt.replace(" ", "")
                   ix = inst.split(',')
                   if len(ix) == 1:
                       iupdtSttmt = 'gender = \'{}\''.format(gender)
                   elif ix[-1] == '' or ix[-1] == ' ' :
                       iupdtSttmt = ','.join(ix[:-1])
                   else:
                       ''''''
                       iupdtSttmt = ','.join(ix)
                   indUpdate = '''
                   UPDATE t_individuals
                   SET {}
                   WHERE Individualguid = '{}'                   
                   '''.format(iupdtSttmt, guid)
                   cursor2.execute(indUpdate)
              
              
                   '''Update relations'''
                   if rowexists('secondary', guid, 't_group'):
                       '''do update'''
                       processinggroupfilenumber = ''
                       processgroupstatuscode = ''
                       
                       grpUpdate = '''
             
                       '''
                   else:
                        
                       grpInsertSt = """ INSERT INTO t_group(fkindividualguid_id,IsAnyGroupPrincipalRepresentative,ProcessingGroupTypeCode,ProcessingGroupNumber,CurrentRationCardNumber,ProcessingGroupFileNumber,ProcessingGroupSize,ProcessingGroupStatusCode,ProcessGroupStatusDate,ProcessingGroupRegistrationDate,IndividualSequenceNumber,PrincipalRepresentative,RelationshipToPrincipalRepresentative,RelationshipText) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
                       cursor2.execute(grpInsertSt, groupInfo)
                   if rowexists('secondary', guid, 't_coa_address'):
                       '''do update'''
                       coaLL1id = COAInfo[0]
                       coaLL2id = COAInfo[1]
                       coaLL3id = COAInfo[2]
                       coaLL4id = COAInfo[3]
                       coaLL5id = COAInfo[4]
                       sttmt = ''
                       
                       if coaLL1id == '' or coaLL1id == '-':
                           sttmt += ''
                       else:
                           sttmt += 'COALocationLevel1ID = \'{}\', '.format(coaLL1id)
                       
                       if coaLL2id == '' or coaLL2id == '-':
                           sttmt += ''
                       else:
                           sttmt += 'COALocationLevel2ID = \'{}\', '.format(coaLL2id)
                       
                       if coaLL3id == '' or coaLL3id == '-':
                           sttmt += ''
                       else:
                           sttmt += 'COALocationLevel3ID = \'{}\', '.format(coaLL3id)
                       
                       if coaLL4id == '' or coaLL4id == '-':
                           sttmt += ''
                       else:
                           sttmt += 'COALocationLevel4ID = \'{}\', '.format(coaLL4id)
                       
                       if coaLL5id == '' or coaLL5id == '-':
                           sttmt += ''
                       else:
                           sttmt += 'COALocationLevel5ID = \'{}\' '.format(coaLL5id)
                       nst = sttmt.replace(" ", "")
                       x = nst.split(',')
                       if len(x) == 1:
                           updtSttmt = 'COALocationLevel5ID = \'{}\''.format(coaLL5id)
                       elif x[-1] == '' or x[-1] == ' ' :
                           updtSttmt = ','.join(x[:-1])
                       else:
                           ''''''
                           updtSttmt = ','.join(x)

                       coaUpdate = '''
                       UPDATE t_coa_address
                       SET {}
                       WHERE fkindividualguid_id = '{}'
                       '''.format(updtSttmt, guid)
                       cursor2.execute(coaUpdate)
                       
                       

                   else:
                       coaInsertSt =""" INSERT INTO t_coa_address(COALocationLevel1ID,COALocationLevel2ID,COALocationLevel3ID,COALocationLevel4ID,COALocationLevel5ID,fkindividualguid_id) VALUES(?,?,?,?,?,?)"""
                       cursor2.execute(coaInsertSt, COAInfo)
                                   
                   if rowexists('secondary', guid, 't_coo_address'):
                       '''do update'''
                       cooLL1id = COOInfo[0]
                       cooLL2id = COOInfo[1]
                       cooLL3id = COOInfo[2]
                       cooLL4id = COOInfo[3]
                       cooLL5id = COOInfo[4]
                       sttmt = ''
                       
                       if cooLL1id == '' or cooLL1id == '-':
                           sttmt += ''
                       else:
                           sttmt += 'COOLocationLevel1ID = \'{}\', '.format(cooLL1id)
                       
                       if cooLL2id == '' or cooLL2id == '-':
                           sttmt += ''
                       else:
                           sttmt += 'COOLocationLevel2ID = \'{}\', '.format(cooLL2id)
                       
                       if cooLL3id == '' or cooLL3id == '-':
                           sttmt += ''
                       else:
                           sttmt += 'COOLocationLevel3ID = \'{}\', '.format(cooLL3id)
                       
                       if cooLL4id == '' or cooLL4id == '-':
                           sttmt += ''
                       else:
                           sttmt += 'COOLocationLevel4ID = \'{}\', '.format(cooLL4id)
                       
                       if cooLL5id == '' or cooLL5id == '-':
                           sttmt += ''' '''
                       else:
                           sttmt += 'COOLocationLevel5ID = \'{}\', '.format(cooLL5id)
                       nst = sttmt.replace(" ", "")
                       x = nst.split(',')
                       if len(x) == 1:
                           updtSttmt = 'COOLocationLevel5ID = \'{}\''.format(cooLL5id)
                       elif x[-1] == '' or x[-1] == ' ' :
                           updtSttmt = ','.join(x[:-1])
                       else:
                           ''''''
                           updtSttmt = ','.join(x)

                       cooUpdate = '''
                       UPDATE t_coo_address
                       SET {}
                       WHERE fkindividualguid_id = '{}'
                       '''.format(updtSttmt, guid)
                       cursor2.execute(cooUpdate)
                       

                   else:
                       cooInsertSt =""" INSERT INTO t_coo_address(COOLocationLevel1ID,COOLocationLevel2ID,COOLocationLevel3ID,COOLocationLevel4ID,COOLocationLevel5ID,fkindividualguid_id) VALUES(?,?,?,?,?,?)"""
                       cursor2.execute(cooInsertSt, COOInfo)
                   
                   vulnInsertSt = """INSERT INTO t_vuln_status(VulnerabilityCode,VulnerabilityDetailsCode,fkindividualguid_id, dt_update) VALUES (?,?,?,?)"""
                   cursor2.execute(vulnInsertSt, VulnInfo)
                   logging.info('{} : Individualguid: {} already has record in the DB'.format(localtime, guid))
                    
                   connection2.commit()
                   logging.info('record was updated')
                else:
                   insertSt = """INSERT INTO {}(IndividualID,Individualguid,FamilyName,GivenName,ConcatenatedName,RegistrationDate,DateofBirth,CountryOfOrigin,AsylumCountryCode,ArrivalDate,gender,Age,IndividualAgeCohortCode,NationalityCode,RSDStatusCode,ResettlementStatusCode,VolRepStatusCode,MarriageStatusCode,EthnicityCode,EducationLevelCode,OccupationCode,ProcessStatusCode,RefugeeStatusCode,FatherName,MotherName,SiteIDOwner,SiteIDCreate,CreateDate,HasSPNeed) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""".format(dest_tb)
                   cursor2.execute(insertSt, slicer)
                   connection2.commit()
                   
                   grpInsertSt = """ INSERT INTO t_group(fkindividualguid_id,IsAnyGroupPrincipalRepresentative,ProcessingGroupTypeCode,ProcessingGroupNumber,CurrentRationCardNumber,ProcessingGroupFileNumber,ProcessingGroupSize,ProcessingGroupStatusCode,ProcessGroupStatusDate,ProcessingGroupRegistrationDate,IndividualSequenceNumber,PrincipalRepresentative,RelationshipToPrincipalRepresentative,RelationshipText) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
                   cursor2.execute(grpInsertSt, groupInfo)
                   connection2.commit()
                   
                   coaInsertSt =""" INSERT INTO t_coa_address(COALocationLevel1ID,COALocationLevel2ID,COALocationLevel3ID,COALocationLevel4ID,COALocationLevel5ID,fkindividualguid_id) VALUES(?,?,?,?,?,?)"""
                   cursor2.execute(coaInsertSt, COAInfo)
                   connection2.commit()
                   
                   cooInsertSt =""" INSERT INTO t_coo_address(COOLocationLevel1ID,COOLocationLevel2ID,COOLocationLevel3ID,COOLocationLevel4ID,COOLocationLevel5ID,fkindividualguid_id) VALUES(?,?,?,?,?,?)"""
                   cursor2.execute(cooInsertSt, COOInfo)
                   connection2.commit()
                   
                   vulnInsertSt = """INSERT INTO t_vuln_status(VulnerabilityCode,VulnerabilityDetailsCode,fkindividualguid_id, dt_update) VALUES (?,?,?,?)"""
        
                   cursor2.execute(vulnInsertSt, VulnInfo)
                   connection2.commit()
                   
                   logging.info('{} : new record inserted with Individualguid: {}'.format(localtime, guid))
                connection2.close()
            
        except UnicodeError as e:
            '''file is not utf-16 presumed utf8'''
            sr = Recoder(f, 'ISO-8859-1', 'utf-8')
            recsv = csv.reader(sr, delimiter=',')
            columns = next(recsv)
            if len(columns)==54 and 'IndividualID' in columns[0] and 'VulnerabilityDetailsCode' in columns[53]:
                '''perform further verification'''
            else:
                '''
                '''
                logging.error("{} {} is not a valid CSV Format".format(localtime,csvfile))
                raise CSVStructureError('Unsuported CSV Suplied')
                return
            for row in recsv:
                crow =[]
                for col in row:
                    ccol = re.sub(' +',' ', col)
                    crow.append(ccol)
                '''SQLCommand = ("INSERT INTO {} (IndividualID, Individualguid, FamilyName, GivenName, ConcatenatedName, RegistrationDate, DateofBirth, CountryOfOrigin, AsylumCountryCode, ArrivalDate, gender, Age, IndividualAgeCohortCode, NationalityCode, RSDStatusCode, ResettlementStatusCode, VolRepStatusCode, MarriageStatusCode, EthnicityCode, EducationLevelCode, OccupationCode, ProcessStatusCode, RefugeeStatusCode, FatherName, MotherName, SiteIDOwner, SiteIDCreate, CreateDate, IsAnyGroupPrincipalRepresentative, HasSPNeed, ProcessingGroupTypeCode, ProcessingGroupNumber, CurrentRationCardNumber, ProcessingGroupFileNumber, ProcessingGroupSize, ProcessingGroupStatusCode, ProcessGroupStatusDate, ProcessingGroupRegistrationDate, IndividualSequenceNumber, PrincipalRepresentative, RelationshipToPrincipalRepresentative, RelationshipText, COALocationLevel1ID, COALocationLevel2ID, COALocationLevel3ID, COALocationLevel4ID, COALocationLevel5ID, COOLocationLevel1ID, COOLocationLevel2ID, COOLocationLevel3ID, COOLocationLevel4ID, COOLocationLevel5ID, VulnerabilityCode, VulnerabilityDetailsCode) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)".format(tb_name))
                Values = row 
                cursor.execute(SQLCommand,Values) 
                connection.commit() '''
                guid = crow[1]
                connection2 = pypyodbc.connect(sdbtxt)
                cursor2 = connection2.cursor()
                confirmQuery = "SELECT count(Individualguid) FROM {} WHERE Individualguid ='{}' ".format(dest_tb, guid)
                cConfirm = cursor2.execute(confirmQuery)
                slicer = crow[:28]
                                
                hasPneed = crow[29]
                slicer.insert(28, hasPneed)
                
 
                groupInfo = crow[28:42]
                groupInfo.insert(0,guid)
                
                COAInfo = crow[42:47]
                COAInfo.insert(5,guid)
                
                COOInfo = crow[47:52]
                COOInfo.insert(5,guid)
                
                VulnInfo = crow[-2:]
                VulnInfo.insert(2, guid)
                VulnInfo.insert(3, time.strftime('%Y-%m-%d %H:%M:%S'))
                
                del(groupInfo[1])


                numF = cConfirm.next()[0]
                
                if numF  == 0:
                   insertSt = """INSERT INTO {}(IndividualID,Individualguid,FamilyName,GivenName,ConcatenatedName,RegistrationDate,DateofBirth,CountryOfOrigin,AsylumCountryCode,ArrivalDate,gender,Age,IndividualAgeCohortCode,NationalityCode,RSDStatusCode,ResettlementStatusCode,VolRepStatusCode,MarriageStatusCode,EthnicityCode,EducationLevelCode,OccupationCode,ProcessStatusCode,RefugeeStatusCode,FatherName,MotherName,SiteIDOwner,SiteIDCreate,CreateDate,HasSPNeed) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""".format(dest_tb)
                   cursor2.execute(insertSt, slicer)
                   connection2.commit()
                   
                   grpInsertSt = """ INSERT INTO t_group(fkindividualguid_id,IsAnyGroupPrincipalRepresentative,ProcessingGroupTypeCode,ProcessingGroupNumber,CurrentRationCardNumber,ProcessingGroupFileNumber,ProcessingGroupSize,ProcessingGroupStatusCode,ProcessGroupStatusDate,ProcessingGroupRegistrationDate,IndividualSequenceNumber,PrincipalRepresentative,RelationshipToPrincipalRepresentative,RelationshipText) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
                   cursor2.execute(grpInsertSt, groupInfo)
                   connection2.commit()
                   
                   coaInsertSt =""" INSERT INTO t_coa_address(COALocationLevel1ID,COALocationLevel2ID,COALocationLevel3ID,COALocationLevel4ID,COALocationLevel5ID,fkindividualguid_id) VALUES(?,?,?,?,?,?)"""
                   cursor2.execute(coaInsertSt, COAInfo)
                   connection2.commit()
                   
                   cooInsertSt =""" INSERT INTO t_coo_address(COOLocationLevel1ID,COOLocationLevel2ID,COOLocationLevel3ID,COOLocationLevel4ID,COOLocationLevel5ID,fkindividualguid_id) VALUES(?,?,?,?,?,?)"""
                   cursor2.execute(cooInsertSt, COOInfo)
                   connection2.commit()
                   
                   vulnInsertSt = """INSERT INTO t_vuln_status(VulnerabilityCode,VulnerabilityDetailsCode,fkindividualguid_id, dt_update) VALUES (?,?,?,?)"""
        
                   cursor2.execute(vulnInsertSt, VulnInfo)
                   connection2.commit()
                   
                   logging.info('{} : new record inserted with Individualguid: {}'.format(localtime, guid))
                    
                else:
                   grpInsertSt = """ INSERT INTO t_group(fkindividualguid_id,IsAnyGroupPrincipalRepresentative,ProcessingGroupTypeCode,ProcessingGroupNumber,CurrentRationCardNumber,ProcessingGroupFileNumber,ProcessingGroupSize,ProcessingGroupStatusCode,ProcessGroupStatusDate,ProcessingGroupRegistrationDate,IndividualSequenceNumber,PrincipalRepresentative,RelationshipToPrincipalRepresentative,RelationshipText) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
                   cursor2.execute(grpInsertSt, groupInfo)
                   connection2.commit()
                   
                   coaInsertSt =""" INSERT INTO t_coa_address(COALocationLevel1ID,COALocationLevel2ID,COALocationLevel3ID,COALocationLevel4ID,COALocationLevel5ID,fkindividualguid_id) VALUES(?,?,?,?,?,?)"""
                   cursor2.execute(coaInsertSt, COAInfo)
                   connection2.commit()
                   
                   cooInsertSt =""" INSERT INTO t_coo_address(COOLocationLevel1ID,COOLocationLevel2ID,COOLocationLevel3ID,COOLocationLevel4ID,COOLocationLevel5ID,fkindividualguid_id) VALUES(?,?,?,?,?,?)"""
                   cursor2.execute(cooInsertSt, COOInfo)
                   connection2.commit()
                   
                   vulnInsertSt = """INSERT INTO t_vuln_status(VulnerabilityCode,VulnerabilityDetailsCode,fkindividualguid_id, dt_update) VALUES (?,?,?,?)"""
                   cursor2.execute(vulnInsertSt, VulnInfo)
                   connection2.commit()
                   logging.info('{} : Individualguid: {} already has {} record in the DB'.format(localtime, guid, numF))
                    
                   connection2.commit()
                   logging.info('record was be updated')
                connection2.close()

        finally:
            f.close()
            connection.close()
        logging.info('{}Data import finished successfully'.format(localtime))

def walker ( directoryStart , extensionList ) :
    os.path.walk( directoryStart, walker_callback, extensionList )

def walker_callback ( extensionList , directory, files ) :
    print("Please wait while CSV Scans for, and imports data")
    logging.info("Scanning {} at {} \n".format(directory, time.asctime( time.localtime(time.time()) )))
    if directory.find("Tanzania") != -1:
        store_db = predb+'_tan'
    elif directory.find("SSD") != -1:
        store_db = predb+'_ssd'
    elif directory.find("Sudan") != -1:
        store_db = predb+'_sud'
    elif directory.find("Burundi") != -1:
        store_db = predb+'_bdi'
    elif directory.find("Djibouti") != -1:
        store_db = predb+'_djb'
    elif directory.find("Kenya") != -1:
        store_db = predb+'_ken'
    elif directory.find("Uganda") != -1:
        store_db = predb+'_uga'
    elif directory.find("Ethiopia") != -1:
        store_db = predb+'_eth'
    else:
        store_db = "None"
    if store_db == "None":
        print "Country not in list"
    else:
        for fileName in files:
            if os.path.isfile( os.path.join(directory,fileName) ) :
                if string.lower(os.path.splitext(fileName)[1]) in extensionList :
                    print fileName
                    op_file = '{}\{}'.format(directory, fileName)
                    process_csv_file(op_file, store_db)

walker( directoryStart, extensionList) 
