'''
Created on May 4, 2016

@author: miami
@version: 1.0.1.b
'''
'''Simple CSV file reader, version 0.0.2 (2002-11-06) , which can handle unlimited-sized CSV files.

This parser can read:
    - CSV (Comma-separated value) files (,)
    - SCSV (Semi-colon-separated value) files (;)
    - TSV (Tab-separated value) files (tabulation)

This parser:
    - supports lines with mixed quoted and unquoted strings.
    - supports cells which contain newlines (quoted strings spanning
      on several lines).
    - can optionnaly ignore comments.
    - can optionnaly ignore empty lines.
    - can optionnaly strip left and right spaces in cells.
    - can efficiently iterate over very large CSV files without eating
      all the memory.
    - can handle very badly-formatted CSV files.
    - does not use regular expressions (which makes it faster
      and "Maximum recursion limit exceeded"-error-proof.)

This class is very easy to use : open the file, and use nextrow()
to get each CSV row.

Usage example:
    import SCSV                    # import the SCSV module
    mydata = SCSV.SCSV()           # Create a SCSV parser
    mydata.opencsv('cat1.csv')     # Open a csv file for reading.
    currentrow = mydata.nextrow()  # Read a row
    while currentrow:     # While there are remaining row, read and print them.
        print currentrow
        currentrow = mydata.nextrow()

Versions:
    2002-06-27 : First version.
    2002-06-28 : - added next() method for iteration.
                 - removed extraneous \n at the end of each row.
                 - added support for TSV (tab-separated) and SCSV
                   (SemiColon-separated) files.
                 - added optional close() method.
                 - fixed problem with a special case (spaces between
                   quoted string marker and columns delimiter)
                 - added option to ignore comments (line starting with #)
                 - added option to ignore empty lines.
                 - added option to strip spaces in each cell.
                 - added getallrows() method to return the whole CSV file
                   at once [USES MORE MEMORY]
                 - added methods to return current line and row number
                   in CSV file (usefull for error reporting).
    2002-07-01 : - changed _startswith() and _endswith() to the native
                   methods string.startswith() and .endswith()
                 - added columnseparator()
    0.0.2 (2002-11-06):
                 - corrected an ugly stupid bug (yuk!).
                 - added version number for easier tracking.

FIXME : Transform this class into an iterator for a more Pythonic programming
        style.
FIXME : add support for named columns
FIXME : add support for CSV/TSV/SCSV writing
FIXME : add support for reading a set number of rows of data
FIXME : add support for batch reading(not line by line)

License:
    LGPL V2

Author:
    Miami Kelvin
'''
class SCSVError(Exception): pass

class SCSV:
    '''Simple CSV file handler. '''
    # States for the parser (used in _parsecsvline())
    _NORMAL    = 0
    _IN_STRING = 1

    def __init__(self, verbose = None):
        self._COLUMN_SEPARATOR  = ','     # Default columns separator : comma (,)
        self._QUOTING_DELIMITER = '"'     # Default string delimiter  : doublequote (")
        self._HAS_COMMENTS = None         # Default do not ignore line who's first character is #
        self._IGNORE_EMPTY_LINES = None   # Default do not ignore empty lines.
        self._STRIP_CELLSPACES = None     # Default Do not strip left and rights spaces in each cell.
        self._currentLine = -1  # Line counter in the CSV file.
        self._currentRow  = -1  # Row  counter in the CSV file.
        self.file = None          # File handle
        self.lineiterator = None  # Iterator over the lines of the file.

    def columnseparator(self):
        ''' Return the current columns separator. '''
        return self._COLUMN_SEPARATOR

    def opencsv(self, filename):
        ''' Open a CSV file (Comma-separated value) for reading. '''
        self._COLUMN_SEPARATOR  = ','
        self._QUOTING_DELIMITER = '"'
        try: # Try to open the file
            file = open(filename,'r')
        except:
            raise SCSVError, 'Could not open file %s for reading.' % filename
        self.lineiterator = file.xreadlines()
        self._currentLine = 0
        self._currentRow  = 0

    def opentsv(self, filename):
        ''' Open a TSV file (Tab-separated value) for reading. '''
        self._COLUMN_SEPARATOR  = '\t'
        self._QUOTING_DELIMITER = '"'
        try: # Try to open the file
            file = open(filename,'r')
        except:
            raise SCSVError, 'Could not open file %s for reading.' % filename
        self.lineiterator = file.xreadlines()
        self._currentLine = 0
        self._currentRow  = 0

    def openscsv(self, filename):
        ''' Open a SCSV file (Semi-Colon-separated value) for reading. '''
        self._COLUMN_SEPARATOR  = ';'
        self._QUOTING_DELIMITER = '"'
        try: # Try to open the file
            file = open(filename,'r')
        except:
            raise SCSVError, 'Could not open file %s for reading.' % filename
        self.lineiterator = file.xreadlines()
        self._currentLine = 0
        self._currentRow  = 0

    def close(self):
        ''' Explicitly close the file (if you need the file to be freed and you don't
            want the garbage collector to close it for you.
            In normal operation, you do not need to call this method. The garbage collector
            will close the file for you.
        '''
        self.lineiterator = None
        self.file.close()
        self.file = None
        self._currentLine = -1
        self._currentRow  = -1

    def currentLineNumber(self):
        ''' Returns the current line number in the CSV file. '''
        return self._currentLine

    def currentRowNumber(self):
        ''' Returns the current row number in the CSV file. '''
        return self._currentRow

    def hasComments(self, v):
        ''' Instruct the SCSV parser to ignore lines who's first character is #.
            Input : v    true -> ignore lines who's first character is #
                         false -> consider all lines CSV data.
        '''
        self._HAS_COMMENTS = v

    def ignoreEmptyLines(self, v):
        ''' Instruct the SCSV parser to ignore empty lines.
            Input : v    true -> the SCSV parser will ignore empty lines
                         false -> empty lines will be considered empty data rows.
        '''
        self._IGNORE_EMPTY_LINES = v

    def stripCellSpaces(self, v):
        ''' Instruct the SCSV parser to strip left and right spaces in each cell.
            Input : v    true -> the SCSV parser will strip left and right spaces.
                         false -> cell will be left as-is with their spaces.
        '''
        self._STRIP_CELLSPACES = v

    def nextrow(self):
        ''' Return next row from the CSV file, reading as many lines as needed from
            the CSV file.
            Output : a tuple containing the cells of the row.
                     or None if there are no more rows.
        '''
        if self.lineiterator == None:
            raise SCSVError, 'Cannot give next row: No file opened for reading. Use opencsv()/opentsv()/openscsv() method before calling nextrow().'
        # We read a line from the CSV file as long as the _parsecsvline() method tells us
        # the row is incomplete. Thus we can handle quoted string which contain newlines.
        try:
            line = self.lineiterator.next()  # Read a single line from the file.
            self._currentLine += 1
        except StopIteration:  # StopIteration exception means we are at the end of the file.
            return None   # There are not more lines in the CSV file.
        else:
            currentrow = line
            ( columns, requiresmore, ignore ) = self._parsecsvline(currentrow)
            if ignore: currentrow = ''
            while requiresmore: # Loop if we need more lines from the CSV file to complete the current row.
                try:
                    line = self.lineiterator.next()  # Read a line from the file.
                    self._currentLine += 1
                except StopIteration:
                    self._currentRow += 1
                    return columns # There are not more lines in the CSV file, return the current row as it is.
                else:
                    currentrow += line   # Append line read from the CSV file to our current row.
                    ( columns, requiresmore, ignore ) = self._parsecsvline(currentrow)  # Decode CSV and check if the row is complete.
                    if ignore: currentrow = ''
            self._currentRow += 1
            return columns

    def getallrows(self):
        ''' Return all rows of the CSV file at once.
            Output : a list containing rows.  Each row is a list of columns.
        '''
        allrows = []
        currentrow = self.nextrow()   # Read a row
        while currentrow:             # While there are remaining row, read and print them.
            allrows.append(currentrow)
            currentrow = self.nextrow()
        return allrows

    def _parsecsvline(self, line):
        '''Parse a single CSV line. Can handle badly-terminated quoted strings.
           Input : line = a line from a CSV file.
           Output : ( columns, isIncomplete, ignore )
                       columns = a list containing values of each cell, with quoted strings unquoted.
                       If a quoted string is not properly terminated, isComplete will be true.
                       (This can append when a cell contains newline character).
                       ignore tells the caller is this row is to be ignore or not.
                       Line to ignore can be comments and/or empty lines (see
                       hasComments() and ignoreEmptyLines().
        '''
        rawsplit = line.split(self._COLUMN_SEPARATOR)
        cleansplit = []
        i = 0

        if self._HAS_COMMENTS and line.startswith('#'): return (None, 1, 1)
        if self._IGNORE_EMPTY_LINES and len(line.strip()) == 0: return (None, 1, 1)

        state = self._NORMAL
        while i < len(rawsplit):
            cell = rawsplit[i]
            if state == self._NORMAL: # We are not in a quoted string: add a new cell.
                if cell.lstrip().startswith(self._QUOTING_DELIMITER):
                    state = self._IN_STRING # We enter a quoted string
                    if cell.rstrip().endswith(self._QUOTING_DELIMITER):
                        state = self._NORMAL
                        cleansplit.append( cell.strip()[1:-1].replace(self._QUOTING_DELIMITER * 2 ,self._QUOTING_DELIMITER))
                    else:
                        cleansplit.append(cell.lstrip()[1:])  # remove the quotes
                else:
                    cleansplit.append(cell) # We are not in a quoted string, just append the cell.
            else:  # We are in a quoted string: append the content of the current cell to the previous cell.
                if cell.rstrip().endswith(self._QUOTING_DELIMITER):  # This is the end of the quoted string
                    state = self._NORMAL    # We exit a quoted string
                    cleansplit[-1] = (cleansplit[-1] + self._COLUMN_SEPARATOR + cell.rstrip()[:-1]).replace(self._QUOTING_DELIMITER * 2,self._QUOTING_DELIMITER)    # remove the ending quote, and append the content of the current cell to the previous cell.
                else:
                    cleansplit[-1] += self._COLUMN_SEPARATOR + cell
            i += 1
        if len(cleansplit[-1]) > 0:
            if cleansplit[-1][-1] in ('\n','\r'): cleansplit[-1] = cleansplit[-1][:-1] # Strip the last \n from the line.
        if self._STRIP_CELLSPACES: # If caller asked to strip left and rights spaces in each cell.
            return (  [i.strip() for i in cleansplit], state, None)
        else:
            return (cleansplit, state, None)

if __name__ == "__main__":
    print __doc__
