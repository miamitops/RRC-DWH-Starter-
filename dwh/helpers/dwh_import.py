'''data import helper methods'''
from datetime import datetime
class csv_helper():
    def read(self):
        ''''''
def walker ( directoryStart , extensionList ) :
    os.path.walk( directoryStart, walker_callback, extensionList )
def str_to_datetime(strTime):
    try:
        ''''''
        dtobj = datetime.strptime(strTime, "%b %d %Y %H:%M%p")
    except ValueError as e:
        ''''''
        print strTime
        dtobj = ''
        
    return dtobj
    
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