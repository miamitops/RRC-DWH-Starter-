from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render_to_response
import random
import datetime
import time
from django.template import RequestContext

'''
data formats
r => raw
p => processed
'''
class DefaultView(View):
    def demo_linechart(request):
        start_time = int(time.mktime(datetime.datetime(2012, 6, 1).timetuple()) * 1000)
        nb_element = 100
        xdata = range(nb_element)
        xdata = map(lambda x: start_time + x * 1000000000, xdata)
        ydata = [i + random.randint(1, 10) for i in range(nb_element)]
        ydata2 = map(lambda x: x * 2, ydata)
    
        tooltip_date = "%d %b %Y %H:%M:%S %p"
        extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"},
                       "date_format": tooltip_date}
        chartdata = {'x': xdata,
                     'name1': 'series 1', 'y1': ydata, 'extra1': extra_serie,
                     'name2': 'series 2', 'y2': ydata2, 'extra2': extra_serie}
        charttype = "lineChart"
        data = {
            'charttype': charttype,
            'chartdata': chartdata
        }
        render_to_response('about.html', data)
    def demo_piechart(request):
            """
            pieChart page
            """
            xdata = [0,1, 2, 3, 4, 5, 6, 7, 8, 9]
            ydata = [52, 48, 160, 94, 75, 71, 490, 82, 46, 17]
            
            xdata1 = ["Apple", "Apricot", "Avocado", "Banana", "Boysenberries", "Blueberries", "Dates", "Grapefruit", "Kiwi", "Lemon"]
            ydata1 = [52, 48, 160, -94, 75, -71, 290, 82, 46, 17]
            ydata11 = [22, 48, 160, 4, 75, 1, 290, -82, 46, 17]
        
            extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}}
            extra_serie1 = {"tooltip": {"y_start": "", "y_end": " cal"}}
            
            chartdata = {'x': xdata, 
                         'name1': 'Just fruits', 'y1': ydata, 'extra1': extra_serie,
                         'name2': 'somethin else', 'y2': ydata11, 'extra1': extra_serie}
            charttype = "lineChart"
            
            chartdata1 = {'x': xdata1, 'name1': '', 'y1': ydata1, 'extra1': extra_serie1}
            charttype1 = "discreteBarChart"
            
            
        
            data = {
                'charttype': charttype,
                'chartdata': chartdata,
            
                'charttype1': charttype1,
                'chartdata1': chartdata1,
            }
            ret_returm = render_to_response('about.html', data)
            return ret_returm
    def demo_queryset(request):
        from dwh_data.models import BaseDataBdi
        from dwh_data.models import IndividualsManager
        ind = IndividualsManager()
        xdata, ydata = ind.with_counts()
        extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}}
        chartdata = {'x': xdata, 
                         'name1': 'Just fruits', 'y1': ydata, 'extra1': extra_serie}
        charttype = "discreteBarChart"
        data = {
                'charttype': charttype,
                'chartdata': chartdata,
                }
                    
        return render_to_response('about.html', {'resp':xdata, 'htm': ydata, 'charttype': charttype, 'chartdata': chartdata})
    def prepareReport(self, rReport):
        ''''''
    def renderReport(self, pReport, view):
        '''
        render a report to view'''
    def get(self, request):
        rr = self.demo_queryset()
        return HttpResponse(rr)