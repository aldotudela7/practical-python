# fileparse.py
#
# Exercise 3.3
import csv
import logging
log = logging.getLogger(__name__)

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a csv file into a list of records.
    '''
    # Check if the lines value is given as a str
    if type(lines) is str:
        raise ValueError('Lines can not be in str format')
    # Check if select is given without headers
    if select and not has_headers:
        raise RuntimeError('Select requires headers')
    
    rows = csv.reader(lines, delimiter=delimiter)
    # If csv file has headers read the first line as headers
    if has_headers:
        headers = next(rows)
    else:
        headers =[]
    # If a selector is given, find indices of those columns, else pass none
    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select
    else:
        indices = []

    records = []
    for rowno, row in enumerate(rows, 1):
        # Skips rows with no data
        if not row:
            continue
        # If selected columns are passed, filter only those column indices
        if select:
            row = [row[index] for index in indices]
        # Adds row to dictionary format and appends it to a list
        if types:
            try:
                row = [func(val) for func, val in zip(types,row)]
            except ValueError as e:
                if not silence_errors:
                    log.warning("Row %d: Couldn't convert %s", rowno, row)
                    log.debug("Row %d: Reason %s", rowno, e)
                continue
            
        # Makes a dictionary or a tuple, depending on whether you have headers or not
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)
    return records