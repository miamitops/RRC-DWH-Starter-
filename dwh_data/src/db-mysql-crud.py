'''
Created on May 4, 2016

@author: miami
'''
import pypyodbc
import pymysql
from config import Config
# Connect to the database
'''
 FIXME : create a configuration file to hold connection variables
 ''' 
class dbCrud:
    def __init__(self, **kwargs):
        
        ''' FIXME: pass connection details from kwargs'''
        configFile = file('pro.conf')
        self.cnf = Config(configFile)
        dbConf = self.cnf.connection
        connection = pypyodbc.connect('Driver={SQL Server};'
                                      'Server=localhost;'
                                      'Database=pro1_test;'
                                      'uid=sa;pwd=filthy6SCENT!!')
        cursor = connection.cursor() 
        SQLCommand = ("INSERT INTO trol (id, name, email) VALUES (?,?,?)")
        Values = [1,'Ibach','Toronto'] 
        cursor.execute(SQLCommand,Values) 
        connection.commit() 
        connection.close()
        
        self.connection = pymysql.connect(host=dbConf[0]['host'],
                                     user=dbConf[0]['user'],
                                     password=dbConf[0]['password'],
                                     db=dbConf[0]['database'],
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        
    def __initDB(self):
        '''
        initialise the Database structure
        '''
    
    def insertRecord(self, record):
        '''
        Insert a single record into the DB
        '''
    '''Read statements'''
    def getIndividualByIID(self, iid):
        '''
        get a user record based on their IndividuaID
        '''
    def getIndividualByIGID(self, igid):
        '''
         get a user by his individual group ID
        '''
''' Example on how to use the dbCrud Class
        try:
            with self.connection.cursor() as cursor:
                # Create a new record
                #sql = "CREATE TABLE IF NOT EXISTS `users` (`id` char(20), `email` varchar(255), `password` varchar(60))"
                #cursor.execute(sql)
                sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
                cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
        
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            self.connection.commit()
        
            with self.connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
                cursor.execute(sql, ('webmaster@python.org',))
                result = cursor.fetchmany(3)
                print(result)
        finally:
            self.connection.close()
    '''
dbClass = dbCrud()