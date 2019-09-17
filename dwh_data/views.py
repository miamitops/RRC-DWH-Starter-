from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from dwh_data.models import BaseDataManager, BaseDataBdi, BaseData, BDGroup, BDCOOAddress, BDCOAAddress, BDVulnerability
from dwh_data.src.csv_recorder import Recoder
from dwh_import.models import DWHImportFile, DWHImportLog
from countries.models import dwhCountry
from dwh.helpers import dwh_import
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from datetime import date, timedelta, datetime
from chartit import DataPool, Chart
from userena.views import signup, signin
from django.db import connections
from multiprocessing import Pool
import time
import csv
import logging
import os,string,sys
import signal
import re
import json
logging.basicConfig(filename='csvimport.log', level=logging.INFO)
  


from countries.models import dwhCountry, dwhCountryStats, dwhStatsArrivals
class DWHDataList(ListView):
    paginate_by = 20
    model = BaseDataBdi
    context_object_name = 'list-individuals'
class ViewHelper():
       def calcPercentage(self, part, whole):
           perc = 100 * float(part)/float(whole)
           return round(perc, 2)
       
       def pop_pie_chart(self):
           from dwh_data.models import BaseDataBdi
           from dwh_data.models import IndividualsManager
           ind = IndividualsManager()
           xdata, ydata = ind.with_counts()
           extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}}
           chartdata = {'x': xdata, 
                             'name1': 'Just fruits', 'y1': ydata, 'extra1': extra_serie}
           charttype = "discreteBarChart"            
           return chartdata, charttype

       def chartitDemo(self):
            ''''''
            #Step 1: Create a DataPool with the data we want to retrieve.
            arrdata = \
                DataPool(
                   series=
                    [{'options': {
                       'source': dwhStatsArrivals.arrManager.get_arrivalStatsLastThreeMonths(0)},
                      'terms': [
                        'arrivalWeek',
                        {'arrivalMale':{'data':{'name':'M'},}},
                        {'arrivalFemale':{'data':{'name':'F'},}}]}
                     ])
        
            #Step 2: Create the Chart object
            cht = Chart(
                    datasource = arrdata,
                    series_options =
                      [{'options':{
                          'type': 'line',
                          'stacking': False,
                          'dataLabels': {'enabled': False}
                                   },
                        'terms':{
                          'arrivalWeek': [
                            {'arrivalMale':{'type': 'line','yAxis':0, 'zIndex':10, 'showInLegend':False,  'tooltip':{'valuePrefix': 'Male '}}},
                            {'arrivalFemale':{'type':'area', 'fillColor': 'rgba(255, 127, 14,0.6)', 'showInLegend':False,'lineColor':'rgba(255, 127, 14,0.9)'}}]
                          }}],
                    chart_options =
                      {'tooltip':{
                                  'valuePrefix': '',
                                  'valueSuffix': ' POC'
                                  
                                  },
                       'title': {
                           'text': 'Three months Arrival Trends'},
                       'yAxis': {
                                 'title': {
                               'text': 'Arrivals'},
                                 },
                       'legend':{
                                 'title': {
                                           'text':'Legend'
                                            }},
                       'xAxis': {
                                 'labels':{'format':'week {value} '},
                            'title': {
                               'text': 'Week # of year 20{}'.format(16)}}})
        
            #Step 3: Send the chart object to the template.
            return {'weatherchart': cht}
       def m_f_piechart(self, data):
            ydata = data
            xdata = ["M","F"]
            extra_serie = {"tooltip": {"y_start": "", "y_end": " call"},}
            chartdata = {'x': xdata, 'y': ydata, 'extra': extra_serie}
            charttype = "pieChart"
            datum = {'e_m_type': charttype,'e_m_data': chartdata}
            return datum
       def chartBar_demographics_c(self, demoData):
           lCountry = []
           lCountryPop = []
           dData = json.loads(demoData)
           for country, countryPop in dData.iteritems():
               lCountry.append('{}'.format(country))
               lCountryPop.append(countryPop)
           xdata = lCountry
           ydata = lCountryPop
           extra_serie1 = {"tooltip": {"y_start": "", "y_end": " cal"}}
           chartdata = {
                'x': xdata, 'name1': '', 'y1': ydata, 'extra1': extra_serie1,
           }
           charttype = "discreteBarChart"
           data = {
                'charttype': charttype,
                'chartdata': chartdata,
           }
           return data
       def jsonAgeSex_Lsorted(self, ASJson):
           '''returns a list for KEYS and a list for Values'''
           keyList = []
           valList = []
           ASDict = json.loads(ASJson)
           keys = ASDict.keys()
           keys.sort()
           sorted = map(ASDict.get, keys)
           
           return sorted
       def get_week_days(self, year, week):
            d = date(year,1,1)
            if(d.weekday()>3):
                d = d+timedelta(7-d.weekday())
            else:
                d = d - timedelta(d.weekday())
            dlt = timedelta(days = (week-1)*7)
            return d + dlt,  d + dlt + timedelta(days=6)
       def arrivalTrend_3M_lineChart(self, arrivals):
            arrivals3months = {}
            arrivals3months['Male'] = []
            arrivals3months['Female'] = []
            arrivals3months['Totals'] = []
            arrivals3months['WeekNumbers'] = []
            for week in arrivals:
                arrivals3months['Male'].append(int(week.arrivalMale))
                arrivals3months['Female'].append(int(week.arrivalFemale))
                arrivals3months['Totals'].append(int(week.arrivalTotalWeek))
                arrivals3months['WeekNumbers'].append(week.arrivalWeek)
            '''Action points
            --> Convert week numbers to dates.
            --> Pass tooltip options to nvd3: remove extra tooltip being added'''
            xdata = arrivals3months['WeekNumbers']
            ydata = arrivals3months['Male']
            ydata2 = arrivals3months['Female']

            extra_serie = {"tooltip": {"y_start": "Week", "y_end": " call"}, "color": "#999", "x_axis_format":"WEEK_NUM", "color_category":"category10"}
            extra_serie2 = {"tooltip": {"y_start": "Week", "y_end": " call"}, "color": "#999", "color_category":"category10"}
            chartdata = {'x': xdata,
                         'name1': 'Male', 'y1': ydata, 'extra1': extra_serie,
                         'name2': 'Female', 'y2': ydata2, 'extra2': extra_serie2}
            charttype = "lineChart"
            datum = {'m_3_type': charttype,'m_3_data': chartdata, 'extra':extra_serie}
            return datum
            '''3 months arrival trends chart'''
           
class DWHDataDetail(DetailView):
    model = BaseDataBdi

class DWHDataCreate(CreateView):
    model = BaseDataBdi
    fields = ['individualid', 'individualguid', 'concatenatedname']

class DWHDataUpdate(UpdateView):
    model = BaseDataBdi
    fields = ['individualid', 'individualguid', 'concatenatedname']

class DWHDataDelete(DeleteView):
    model = BaseDataBdi
    success_url = reverse_lazy('bdi_list')
class DWHImport(CreateView):
    
    def importcsv(self, csvfile):
        
        fname = csvfile[-18:]
        countryid = fname[:3]
        prognstance = fname[3:5]
        d_generated = datetime.strptime(fname[6:14], "%Y%m%d")
        
        logger = DWHImportLog()
        importcountry = dwhCountry(countryID=countryid)
        importf = DWHImportFile()
        
        
        try:
            exist = DWHImportFile.objects.get(fcountry = importcountry, progressinstance =  prognstance, dategenerated= d_generated)
            '''file was imported with different success status'''
            if exist.importstatus == 'succs':
                '''file was imported successfully move to complete folder if still exists'''
            elif exist.importstatus == 'succe':
                '''import succeeded but with eroneous rows, action debug rows from import log'''
            elif exist.importstatus == 'faile':
                '''entire file failed to import debug entire file'''
            print "no import performed"
            '''test '''
        except:
            '''file isn't imported add record to db and import'''
            importf.fcountry = importcountry
            importf.progressinstance = prognstance
            importf.dategenerated = d_generated
            importf.dateimport = datetime.now()
            with open(csvfile,'rb') as f:
                try:
                    sr = Recoder(f, 'ISO-8859-1', 'utf-8')
                    recsv = csv.reader(sr, delimiter=',')
                    columns = next(recsv)
                    if len(columns)==54 and 'IndividualID' in columns[0] and 'VulnerabilityDetailsCode' in columns[53]:
                        print"verification passed"
                    else:
                        
                        rowerror = True
                        return
                    for row in recsv:
                        if len(row) != 54:
                             print "faulty row {}".format(row)
                             '''action: log this to report error log db'''
                             '''set variable indicating some rows had errors'''
                             
                             rowerror = True
                             continue
                        crow =[]
                        for col in row:
                            ccol = re.sub(' +',' ', col)
                            crow.append(ccol)
                        '''pool = Pool(4)
                        results = pool.map(self.saveupdate, f, 4)
                        '''
                        self.saveupdate(crow)
                        importf.importstatus = 'succs'
                    
                except UnicodeError as e:
                    importf.importstatus = 'faile'
            importf.save()
        
        '''%Y%B%D'''

    def importfiles(self, request):
        ''''''
        '''directoryStart = r'dwh_data\files\import' '''
        directoryStart = r'G:\RRC\import'
        extensionList=['.csv']
        '''action list'''
        '''daemonize process and save active session in db'''
        '''1st checK if import process is running before running another import'''
        '''if possible run multiple imports in parallel: with status in db - in progress or complete for files, if in-progress or complete then take next file in que'''
        '''in case of failure midway log line number in database to facilitate resumption'''
        self.walker( directoryStart, extensionList)
        
        '''self.saveupdate(csvi)'''
    def saveupdate(self, csvRow):
        '''save a csv row(list) into the database'''
        
        guid = csvRow[1]
        individual = csvRow[:28]

        hasPneed = csvRow[29]
        individual.insert(28, hasPneed)
        self.saveindividual(individual)
 
        familyData = csvRow[28:42]
        familyData.insert(0,guid)
        del(familyData[1])
        self.savefamilydetails(familyData)
                
        coaData = csvRow[42:47]
        coaData.insert(5,guid)
        self.savecoaaddress(coaData)
                
        cooData = csvRow[47:52]
        cooData.insert(5,guid)
        self.savecooaddress(cooData)
                
        vulnData = csvRow[-2:]
        vulnData.insert(2, guid)
        vulnData.insert(3, time.strftime('%Y-%m-%d %H:%M:%S'))
        self.savevulnerability(vulnData)
        '''record successfully saved'''

        
        
    def saveindividual(self, rowData):
        '''
        individualguid 
        individualid
        familyname 
        givenname 
        concatenatedname 
        registrationdate 
        dateofbirth 
        countryoforigin 
        asylumcountrycode 
        arrivaldate 
        gender 
        age 
        individualagecohortcode 
        nationalitycode 
        rsdstatuscode 
        resettlementstatuscode 
        volrepstatuscode 
        marriagestatuscode 
        ethnicitycode 
        educationlevelcode 
        occupationcode 
        processstatuscode 
        refugeestatuscode 
        fathername 
         mothername 
         siteidowner 
         siteidcreate 
         createdate 
         hasspneed 
         d_arrival 
         d_registration 
         d_dob 
         '''
        individual = BaseData()
        individual.individualguid = rowData[1]
        individual.individualid = rowData[0]
        individual.familyname = rowData[2]
        individual.givenname = rowData[3]
        individual.concatenatedname = rowData[4]
        individual.registrationdate = rowData[5]
        individual.dateofbirth = rowData[6]
        individual.countryoforigin = rowData[7]
        individual.asylumcountrycode = rowData[8]
        individual.arrivaldate = rowData[9]
        individual.gender = rowData[10]
        individual.age = rowData[11]
        individual.individualagecohortcode = rowData[12]
        individual.nationalitycode = rowData[13]
        individual.rsdstatuscode = rowData[14]
        individual.resettlementstatuscode = rowData[15]
        individual.volrepstatuscode = rowData[16]
        individual.marriagestatuscode = rowData[17]
        individual.ethnicitycode = rowData[18]
        individual.educationlevelcode = rowData[19]
        individual.occupationcode = rowData[20]
        individual.processstatuscode = rowData[21]
        individual.refugeestatuscode = rowData[22]
        individual.fathername = rowData[23]
        individual.mothername = rowData[24]
        individual.siteidowner = rowData[25]
        individual.siteidcreate = rowData[26]
        individual.createdate = rowData[27]
        individual.hasspneed = rowData[28]
        
        '''convert dates to datetime'''
        '''some dates are empty and datetime convertion fails'''
        '''work arround try except statement'''
        dateArrival = dwh_import.str_to_datetime(rowData[9])
        dateReg = dwh_import.str_to_datetime(rowData[5])
        dateDOB = dwh_import.str_to_datetime(rowData[6])
        if dateArrival == '':
            ''''''
        else:
            individual.d_arrival = dateArrival
        
        if dateReg == '':
            ''''''
        else:
            individual.d_registration = dateReg
        
        if dateDOB == '':
            ''''''
        else:
            individual.d_dob = dateDOB
        individual.save()
    def savecoaaddress(self, coaData):
        ''''''
        individual = BaseData(individualguid = coaData[5])
        address = BDCOAAddress()
        
        address.fkindividualguid = individual
        address.coalocationlevel1id = coaData[0]
        address.coalocationlevel2id = coaData[1]
        address.coalocationlevel3id = coaData[2]
        address.coalocationlevel4id = coaData[3]
        address.coalocationlevel5id = coaData[4]
        address.save()
        
    def savecooaddress(self, cooData):
        ''''''
        individual = BaseData(individualguid = cooData[5])
        address = BDCOOAddress()
        
        address.fkindividualguid = individual
        address.coolocationlevel1id  = cooData[0]
        address.coolocationlevel2id  = cooData[1]
        address.coolocationlevel3id  = cooData[2]
        address.coolocationlevel4id  = cooData[3]
        address.coolocationlevel5id  = cooData[4]
        address.save()
    def savefamilydetails(self, familyData):
        ''''''
        individual = BaseData(individualguid = familyData[0])
        family = BDGroup()
        '''
         processinggrouptypecode 
         processinggroupnumber 
         currentrationcardnumber 
         processinggroupfilenumber 
         processinggroupsize 
         processinggroupstatuscode 
         processgroupstatusdate 
         processinggroupregistrationdate 
         individualsequencenumber 
         fkindividualguid 
         isanygroupprincipalrepresentative 
         principalrepresentative 
         relationshiptoprincipalrepresentative 
         relationshiptext
        '''
        family.processinggrouptypecode = familyData[2]
        family.processinggroupnumber = familyData[3]
        family.currentrationcardnumber = familyData[4]
        family.processinggroupfilenumber = familyData[5]
        family.processinggroupsize = familyData[6]
        family.processinggroupstatuscode = familyData[7]
        family.processgroupstatusdate = familyData[8]
        family.processinggroupregistrationdate = familyData[9] 
        family.individualsequencenumber = familyData[10]
        family.fkindividualguid = individual
        family.isanygroupprincipalrepresentative = familyData[1]
        family.principalrepresentative = familyData[11]
        family.relationshiptoprincipalrepresentative = familyData[12]
        family.relationshiptext = familyData[13]
        family.save()
        
    def savevulnerability(self, vulnData):
        ''''''
        if vulnData[0] == '' and vulnData[1] == '':
            '''if both are empty dont do anything'''
        else:
            individual = BaseData(individualguid = vulnData[2])
            vuln = BDVulnerability()
            
            vuln.vulnerabilitycode = vulnData[0]
            vuln.vulnerabilitydetailscode = vulnData[1]
            vuln.fkindividualguid = individual
            vuln.dt_update = vulnData[3]
            vuln.save()

    
    def walker_callback (self,  extensionList , directory, files ) :
        predb = 'dbo.base_data'
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
        '''if store_db == "None":
            print "Country not in list"
        else:'''
        for fileName in files:
                if os.path.isfile( os.path.join(directory,fileName) ) :
                    if string.lower(os.path.splitext(fileName)[1]) in extensionList :
                        print fileName
                        op_file = '{}\{}'.format(directory, fileName)
                        self.importcsv(op_file)
    def walker (self, directoryStart , extensionList ) :
        os.path.walk( directoryStart, self.walker_callback, extensionList )
        
class PageView(DetailView):
    def get_situations(self):
        from situations.models import dwhSituations
        activesituations = dwhSituations.active.all() 
        return activesituations
    def get_countries(self):
        from countries.models import dwhCountry
        activecountries = dwhCountry.active.all() 
        return activecountries              

    def index(self, request):
        
        helper = ViewHelper()
        mdata, mtype = helper.pop_pie_chart()
        if request.user.is_authenticated():
            self.name = '{} {}'.format(request.user.first_name, request.user.last_name)
            self.pp = ''
        else:
            self.name = 'Anon User'
        pageData = {}
        pageData['situations'] = self.get_situations()
        pageData['countries'] = self.get_countries()
        pageData['user_name'] = self.name 
        pageData['chartdata'] = mdata
        pageData['charttype'] = mtype
        return render_to_response('dwh_data/dashboards/production/index.html', pageData, context_instance=RequestContext(request))
    def login(self, request):
        ''''''
        return render_to_response('dwh_data/dashboards/production/login.html', context_instance=RequestContext(request))
    def countrySitRep(self, request, **kwargs):
        from countries.models import dwhCountry, dwhCountryStats
        mCountry = kwargs['countryid']
        
        stats = get_object_or_404(dwhCountryStats, fkCountryId = mCountry)
        
        arrivals, stats3months = dwhStatsArrivals.arrManager.get_countryStatWithArr(stats.statId)
        
        helper = ViewHelper()
        ageSex = stats.ageSex
        demographics = stats.demographics
        lAgeSex = helper.jsonAgeSex_Lsorted(ageSex)
        '''First three items in the list are children 1 to 17 years'''
        children = lAgeSex[:3] 
        adults = lAgeSex[3:]
        lAdults = []
        lChildren = []
        for ageGroupC in children:
            for key, val in ageGroupC.iteritems():
                lChildren.append(val)
        totalChildren = sum(lChildren)
        for ageGroupA in adults:
            for keyA, valA in ageGroupA.iteritems():
                lAdults.append(valA)
        totalAdults = sum(lAdults)
        
        '''Male Female Total Population Data'''
        mfData = [stats.TotalMPop, stats.TotalFPop]
        '''Male|Female Total POP Pie Chart'''
        mfChart = helper.m_f_piechart(mfData)
        demographicsChart = helper.chartBar_demographics_c(demographics)
        
        '''Three Months Arrival trends data'''
        total3Months = 0
        arrivals3months = {}
        month3t = helper.arrivalTrend_3M_lineChart(stats3months)
        for week in stats3months:
            total3Months += week.arrivalTotalWeek
            
        curCountry = get_object_or_404(dwhCountryStats, fkCountryId=mCountry)
        if request.user.is_authenticated():
            self.name = '{} {}'.format(request.user.first_name, request.user.last_name)
            self.pp = ''
        else:
            self.name = 'Anon User'
        pageData = {}
        pageData['user_name'] = self.name
        pageData['situations'] = self.get_situations()
        pageData['countries'] = self.get_countries()
        pageData['chartdata'] = helper.chartitDemo()
        pageData['country'] = curCountry
        pageData['stats'] = stats
        pageData['stats3months'] = stats3months
        pageData['totalChildren'] = '{0:} % ({1:,})'.format(helper.calcPercentage(totalChildren, stats.TotalPop), int(totalChildren))
        pageData['totalAdults'] = '{0:} % ({1:,})'.format(helper.calcPercentage(totalAdults, stats.TotalPop), totalAdults)
        pageData['agegroups'] = lAgeSex
        pageData['demographicsChart'] = demographicsChart
        '''remove'''
        pageData['m_f_chart'] = mfChart
        pageData['m_3_chart'] = demographics
        return render_to_response('dwh_data/dashboards/production/country.html', pageData, context_instance=RequestContext(request))
    def situationSitRep(self, request, **kwargs):
        from situations.models import dwhSituations
        self.mSitid = kwargs['situationid']
        self.curSit = get_object_or_404(dwhSituations, situationID=self.mSitid)
        helper = ViewHelper()
        mdata, mtype = helper.pop_pie_chart()
        if request.user.is_authenticated():
            self.name = '{} {}'.format(request.user.first_name, request.user.last_name)
        else:
            self.name = 'Anon User'
        pageData = {}
        pageData['user_name'] = self.name
        pageData['situations'] = self.get_situations()
        pageData['countries'] = self.get_countries()
        pageData['situation'] = self.curSit
        return render_to_response('dwh_data/dashboards/production/situation.html', pageData, context_instance=RequestContext(request))
    def generate_stats(self, CID):
        cursor = connections['dwh_data'].cursor()
        qq = """
            SELECT YEAR(n_ArrivalDate), DATEPART(wk, n_ArrivalDate), gender, COUNT(Individualguid)
            FROM t_individuals 
            WHERE AsylumCountryCode = '{}'
            AND RefugeeStatusCode IN ('REF', 'ASR')
            AND gender in ('M', 'F')
            AND NOT n_ArrivalDate is null
            GROUP BY YEAR(n_ArrivalDate), DATEPART(wk, n_ArrivalDate), gender
            ORDER BY YEAR(n_ArrivalDate) DESC
            """.format(CID)
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
    def generate_demographic_stats(self, CID):
        cursor = connections['dwh_data'].cursor()
        qq = """
            SELECT YEAR(n_ArrivalDate), DATEPART(wk, n_ArrivalDate), CountryOfOrigin, COUNT(Individualguid)
            FROM t_individuals 
            WHERE AsylumCountryCode = '{}'
            AND RefugeeStatusCode IN ('REF', 'ASR')
            AND NOT n_ArrivalDate is null
            GROUP BY YEAR(n_ArrivalDate), DATEPART(wk, n_ArrivalDate), CountryOfOrigin
            ORDER BY YEAR(n_ArrivalDate) DESC
            """.format(CID)
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
    def gen_countryAS_stats(self, cid):
        cursor = connections['dwh_data'].cursor()
        qq = """
                SELECT IndividualAgeCohortCode, gender,  COUNT(Individualguid)
                FROM dwh_data.dbo.t_individuals
                WHERE ProcessStatusCode IN ('A', 'H')
                AND RefugeeStatusCode IN ('REF', 'ASR')
                AND gender IN ('M', 'F')
                AND IndividualAgeCohortCode in ('A1', 'A2', 'A3', 'A4', 'A5')
                AND AsylumCountryCode = '{}'
                AND NOT NationalityCode = '{}'
                GROUP BY IndividualAgeCohortCode, gender
                ORDER BY IndividualAgeCohortCode ASC
        """.format(cid, cid)
        cStats = cursor.execute(qq)
        totalMpop = 0
        totalFpop = 0
        
        rowStat = {'A1':{'M':0, 'F':0}, 'A2':{'M':0,'F':0}, 'A3':{'M':0, 'F':0}, 'A4':{'M':0, 'F':0}, 'A5':{'M':0, 'F':0}}
        for row in cStats :
            if '{}'.format(row[0]) in rowStat:
                '''age group'''
                
                if '{}'.format(row[1]) in rowStat['{}'.format(row[0])]:
                    ASList = row[2]
                    '''ASList = rowStat[row[0]][row[1]]
                    ASList['{}'.format(row[2])] = row[3]'''
                else:                   
                    ASList = row[2]
                rowStat['{}'.format(row[0])]['{}'.format(row[1])] = ASList
                '''remove U values in our dictionary we only need Male Female'''
                if 'U' in rowStat['{}'.format(row[0])]:
                    rowStat['{}'.format(row[0])].pop('U')
            else:
                ''''''
                rowStat['{}'.format(row[0])] = {}
                rowStat['{}'.format(row[0])]['{}'.format(row[1])] = row[2]
            
        return rowStat
        '''Statistics for the total pop'''
    def gen_coaDemographics(self, cid):
        cursor = connections['dwh_data'].cursor()
        qq = """
                SELECT NationalityCode, COUNT(Individualguid)
                FROM dwh_data.dbo.t_individuals
                WHERE ProcessStatusCode IN ('A', 'H')
                AND RefugeeStatusCode IN ('REF', 'ASR')
                AND AsylumCountryCode = '{}'
                AND NOT NationalityCode IN ('{}', '-', 'U')
                GROUP BY NationalityCode
                ORDER BY NationalityCode ASC
        """.format(cid,cid)
        cStats = cursor.execute(qq)
        rowStat = {}
        for row in cStats:
            if '{}'.format(row[0]) in rowStat:
                rowStat['{}'.format(row[0])] = row[1]
            else:
                rowStat['{}'.format(row[0])] = row[1]
            ''''''
        return rowStat
    def insertArrivalStats(self, stats, statID):
        '''statInsertSQL = """INSERT INTO dwh_country_stats(fkCountryId_id, i_tot_pop, i_tot_m_pop, i_tot_f_pop, s_demographics, s_age_sex, s_gender) VALUES('{}',{},{},{},'{}','{}','{}') """.format('BDI',120, 90, 30, 's_demographics', 's_age_sex', 's_gender')
        '''
        
        '''It would be great if the dwhStatsArrivals model could handle this but the ids of these objects are ephemeral'''
        '''records are identified by year and week num and not the stat_id'''
        cursor = connections['default'].cursor()                 
        for year, weeks in stats.iteritems():
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
                M = asB['M']
                F = asB['F']
                totalYear += weektotalArrivals
                confirmQuery = """
                SELECT * 
                FROM dwh_c_arrival_stats
                WHERE i_arr_year = {}
                AND  i_arr_week = {}
                AND fkStatId_id = {}
                """.format(year, weekNum, 0)
                
                numRecords = cursor.execute(confirmQuery)
                if numRecords >= 1 :
                    ''' Update an existing record
                    
                    '''
                    weekSql = """
                    UPDATE dwh_c_arrival_stats
                    SET i_arr_total = {}, s_demographics = '{}', s_age_sex = '{}', i_arr_m = {}, i_arr_f = {}, dt_created = '{}'
                    WHERE i_arr_year = {}
                    AND i_arr_week = {}
                    AND fkStatId_id = {}
                    """.format(weektotalArrivals,'0','0',M,F,datetime.now(),year,weekNum,statID)

                else:
                    ''''''
                    weekSql = """ INSERT INTO dwh_c_arrival_stats(fkStatId_id, i_arr_year, i_arr_week, i_arr_total, s_demographics,s_age_sex,i_arr_m,i_arr_f, dt_created)
                    VALUES ({},{},{},{},'{}','{}',{},{}, '{}')""".format(statID,year,weekNum,weektotalArrivals,'0','0',M,F, datetime.now())
                    '''Insert Arrivals to DB'''
                cursor.execute(weekSql)
    def updateArrivalDemographics(self, demographics, statID):
        '''It would be great if the dwhStatsArrivals model could handle this but the ids of these objects are ephemeral'''
        '''records are identified by year and week num and not the stat_id 
        updates can be achieved using the Q sub-directive of the method but that wouldnt be fun'''
        cursor = connections['default'].cursor()
        for year, weeks in demographics.iteritems():
            totalYear = 0
            '''year'''
            for weekNum, demograph in weeks.iteritems():
                weekSql = """
                UPDATE dwh_c_arrival_stats
                SET s_demographics = '{}'
                WHERE i_arr_year = {}
                AND i_arr_week = {}
                AND fkStatId_id = {}
                """.format(json.dumps(demograph),year,weekNum,statID)
                cursor.execute(weekSql)

    def saveCountryStat(self, request, **kwargs):

        cid = kwargs['countryid']
        stats = get_object_or_404(dwhCountryStats, fkCountryId = cid)
        
        '''
        sCountry = dwhCountry.countries.get(countryID = 'KEN')
        code for creating a new country stat
        cStats = dwhCountryStats()
        cStats.statId = 1
        cStats.TotalPop = 7600
        cStats.TotalMPop = 8000
        cStats.TotalFPop = 1600
        cStats.TotalUnaccompanied = 0
        cStats.demographics =''
        cStats.ageSex = ''
        cStats.popGender = ''
        cStats.fkCountryId = sCountry
        cStats.save()
        '''
        cursor = connections['default'].cursor()
        Arrstats = self.generate_stats(cid)
        ArrDemographics = self.generate_demographic_stats(cid)
        
        asStats = self.gen_countryAS_stats(cid)
        demographics = self.gen_coaDemographics(cid)
        
        stats.ageSex = json.dumps(asStats)
        stats.demographics = json.dumps(demographics)
        stats.save()
        
        arrIn = self.insertArrivalStats(Arrstats, stats.statId)
        self.updateArrivalDemographics(ArrDemographics, stats.statId)
    
        
        return render_to_response('dwh_data/dashboards/production/index2.html', {'stats':ArrDemographics})

    def logout(self, request):
        ''''''
        return render_to_response('dwh_data/dashboards/production/index2.html', context_instance=RequestContext(request))
