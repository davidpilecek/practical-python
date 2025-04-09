# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename:str, select:list=['name', 'shares', 'price'], types:list = [str, int, float], has_headers:bool = True, delimiter:str = ',') -> list:
    '''
    Parse a CSV file into a list of records
    '''

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        if has_headers:
            headers = next(rows)
            if select:
                indices = [headers.index(s) for s in select]
            else:
                indices = []
        else:
            select=[]

        records = []
        for row in rows:
            if not row:
                continue
            if has_headers:
                row = [(row[i]) for i in indices]
                if types:
                    row = [func(val) for func, val in zip(types, row)]
                    record = dict(zip(select, row))
                    records.append(record)
            else:
                records.append(row)
    return records

portfolio = parse_csv(r"C:\Users\David\Desktop\practical-python\Work\Data\prices.csv", types=[str,float], has_headers=False)
print(portfolio)

        