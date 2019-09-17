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
import json

import re
from datetime import date


sdbtxt = 'Driver={SQL Server};''Server=localhost;''Database=dwh_data;''uid=sa;pwd=filthy6SCENT!!'
localtime = time.asctime( time.localtime(time.time()) )
dest_tb ='t_individuals'

def generate_stats():
    connection = pypyodbc.connect(sdbtxt)
    cursor = connection.cursor()
    qq = """
        SELECT YEAR(n_ArrivalDate), DATEPART(wk, n_ArrivalDate), gender, COUNT(Individualguid)
        FROM t_individuals 
        GROUP BY YEAR(n_ArrivalDate), DATEPART(wk, n_ArrivalDate), gender
        ORDER BY YEAR(n_ArrivalDate) DESC
        """
    statsRes = cursor.execute(qq)
    rowStat = {}
    for row in statsRes:
        '''Do Something
        0=> year
        1=> WeekNum
        2=> M|F  
        3 => total      
        '''
        
        if row[0] in rowStat:
            ''''''
            if row[1] in rowStat[row[0]]:
                ASList = rowStat[row[0]][row[1]]
                ASList['{}'.format(row[2])] = row[3]
            else:
                ASList = {'{}'.format(row[2]): row[3]}
            rowStat[row[0]][row[1]] = ASList
        else:
            ''''''
            rowStat[row[0]] = {}
            rowStat[row[0]][row[1]] = {'{}'.format(row[2]):row[3]}
            
    return rowStat
def saveStats():
    ''''''
    connection = pypyodbc.connect(sdbtxt)
    cursor = connection.cursor()
    '''Insert Stat and Get Last StatID'''
    curStats = generate_stats()
    for year, weeks in curStats.iteritems():
        totalYear = 0
        '''year'''
        for weekNum, a_s in weeks.iteritems():
            '''week Number'''
            weektotalArrivals = sum(a_s.values())
            asB = {}
            if 'M' in a_s:
                asB['M'] = a_s['M']
            else:
                asB['M'] = 0
                
            if 'F' in a_s:
                asB['F'] = a_s['F']
            else:
                asB['F'] = 0
            totalYear += weektotalArrivals
            if year == 2016:
                print '{} - {} - {} - {}'.format(year, weekNum, json.dumps(asB), weektotalArrivals)
                start, ends = get_week_days(year, weekNum)
                print (start, ends)
                '''Insert Arrivals to DB'''
            '''from isoweek import Week
            d = Week(year, weekNum).monday()
            print d'''
                
        import datetime
        import dateutil.relativedelta
            
        d = datetime.datetime.strptime("{}".format(date.today()), "%Y-%m-%d")
        d2 = d - dateutil.relativedelta.relativedelta(months=3)
        print d2
        
    today = date.today().isocalendar()[1]
    print "Todays Week Number is {}".format(today)
    print "Three months ago was week {}".format(d2.isocalendar()[1])

from datetime import date, timedelta
def gen_countryStats():
    connection = pypyodbc.connect(sdbtxt)
    cursor = connection.cursor()
    query = """
    SELECT IndividualAgeCohortCode, gender,  COUNT(Individualguid)
                FROM dwh_data.dbo.t_individuals
                WHERE ProcessStatusCode IN ('A', 'H')
                GROUP BY IndividualAgeCohortCode, gender
                ORDER BY IndividualAgeCohortCode ASC
                """
    statsRes = cursor.execute(query)
    rowStat = {'A1':{'M':0, 'F':0}, 'A2':{'M':0,'F':0}, 'A3':{'M':0, 'F':0}, 'A4':{'M':0, 'F':0}, 'A5':{'M':0, 'F':0}}
    for row in statsRes :
        if '{}'.format(row[0]) in rowStat:
            
            if '{}'.format(row[1]) in rowStat['{}'.format(row[0])]:
                '''ASList = rowStat[row[0]][row[1]]
                ASList['{}'.format(row[2])] = row[3]'''
                ASList = row[2]
            else:
                ASList = row[2]
            rowStat['{}'.format(row[0])]['{}'.format(row[1])] = ASList
        else:
            ''''''
            rowStat['{}'.format(row[0])] = {}
            rowStat['{}'.format(row[0])]['{}'.format(row[1])] = row[2]
    print json.dumps(rowStat)
def gen_coaDemographics():
    connection = pypyodbc.connect(sdbtxt)
    cursor = connection.cursor()
    qq = """
                SELECT CountryOfOrigin, COUNT(Individualguid)
                FROM dwh_data.dbo.t_individuals
                WHERE ProcessStatusCode IN ('A', 'H')
                AND AsylumCountryCode = 'BDI'
                GROUP BY CountryOfOrigin
                ORDER BY CountryOfOrigin ASC
        """.format('BDI')
    cStats = cursor.execute(qq)
    rowStat = {}
    for row in cStats:
        if '{}'.format(row[0]) in rowStat:
            rowStat['{}'.format(row[0])] = row[1]
        else:
            rowStat['{}'.format(row[0])] = row[1]
    keyList = []
    valueList = []
    for key, value in rowStat.iteritems():
        keyList.append(key)
        valueList.append(value)
    print keyList
    print valueList
def get_week_days(year, week):
    d = date(year,1,1)
    if(d.weekday()>3):
        d = d+timedelta(7-d.weekday())
    else:
        d = d - timedelta(d.weekday())
    dlt = timedelta(days = (week-1)*7)
    return d + dlt,  d + dlt + timedelta(days=6)
def get_ArrivalDemographics(CID):
    connection = pypyodbc.connect(sdbtxt)
    cursor = connection.cursor()
    qq = """
        SELECT YEAR(n_ArrivalDate), DATEPART(wk, n_ArrivalDate), IndividualAgeCohortCode, gender, COUNT(Individualguid)
        FROM t_individuals 
        WHERE AsylumCountryCode = '{}'
        AND YEAR(n_ArrivalDate) = 2016

        GROUP BY YEAR(n_ArrivalDate), DATEPART(wk, n_ArrivalDate), IndividualAgeCohortCode, gender
        ORDER By YEAR(n_ArrivalDate) DESC
        """.format(CID)
    allDemog = cursor.execute(qq)
    rowStat = {}
    dASBreakDown = {'A1':{'M':0, 'F':0},'A2':{'M':0, 'F':0},'A3':{'M':0, 'F':0},'A4':{'M':0, 'F':0},'A5':{'M':0, 'F':0}}
    for row in allDemog:
        demographs = dASBreakDown
        
        if row[0] in rowStat:
            '''year is in dictionary'''
            if row[1] in rowStat[row[0]]:
                '''week is in dictionary'''
                demographs['{}'.format(row[2])]['{}'.format(row[3])] = row[4]
                exist = rowStat[row[0]][row[1]]
                print "this "
                
            else:
                if row[2] == '' :
                    continue
                demographs['{}'.format(row[2])] ['{}'.format(row[3])] = row[4]
                rowStat[row[0]][row[1]] = demographs
                print rowStat
            rowStat[row[0]][row[1]]= demographs
        else:
            ''''''
            rowStat[row[0]] = {row[1]: demographs}
            
    print rowStat
get_ArrivalDemographics('BDI')
    
 
