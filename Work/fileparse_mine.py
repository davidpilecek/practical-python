# fileparse.py
#
# Exercise 3.3

import csv
import gzip

def parse_csv(lines=None, select:list = None, types:list = [str, int, float], has_headers:bool = True, delimiter:str = ',', silence_errors = False) -> list:
    '''
    Parse a CSV file into a list of records
    '''
    if(not has_headers and select):
        raise RuntimeError("Select argument requires column headers")
    
    rows = csv.reader(lines, delimiter=delimiter)

    if has_headers:
        headers = next(rows)
        
        if select:
            indices = [headers.index(s) for s in select]
        else:
            select=headers
            indices = [headers.index(s) for s in select]
    else:
        headers = []
        select=headers

    records = []

    for rowno, row in enumerate(rows, 1):
        if not row:
            continue

        if has_headers:
            row = [(row[i]) for i in indices]
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f'Row {rowno}: Couldn\'t convert {row}')
                    print(f'Row {rowno}: Reason: {e}\n')

            if select:
                record = dict(zip(select, row))
            else:
                record = tuple(row)

            records.append(record)
    return records

if __name__ == "__main__":

    port = parse_csv(r'Work/Data/portfolio.csv', types=[str,int,float])
    
    print(port)