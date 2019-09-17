from multiprocessing import Pool
import os,string,sys
from src.csv_recorder import Recoder
import csv
from itertools import izip_longest
import time
import datetime
import logging

directoryStart = r'files\import\Burundi'
extensionList=['.csv']
predb = 'dbo.base_data'
logging.basicConfig(filename='csvimport_test.log', level=logging.INFO)
localtime = time.asctime( time.localtime(time.time()) )
dest_tb ='t_individuals'

def process_chunk(d):
    d = d.strip() + ' processed'
    return d
def grouper(n, iterable,padvalue=None):
    izip_longest(*[iter(iterable)]*n, fillvalue=padvalue)
def process_line(line):
    print line
def process_csv_file(op_file):
    ''''''
    with open(op_file) as f:
        ''''''
        pool = Pool(4)
        results = pool.map(process_line, f, 4)
    print results
        
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
                    process_csv_file(op_file)
if __name__ == '__main__':
    walker( directoryStart, extensionList) 