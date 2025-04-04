# pcost.py
#
# Exercise 1.27
import gzip
import csv
import sys

path = r"/home/david/Desktop/practical-python/Work/Data/missing.csv"
path2 = r"/home/david/Desktop/practical-python/Work/Data/portfolio.csv.gz"

def portfolio_cost(filename):
    'Input: path to file'
    'Output: cost of portfolio'

    total_cost = 0
    f = open(filename)
    rows = csv.reader(f)
    header = next(rows)

    for row_num, stock in enumerate(rows, start=1):
        record = dict(zip(header, stock))
        print(record)
        try:
            #stock = stock.split(',')
            count = int(stock[1])
            cost = float(stock[2])
            total_cost += round(count*cost, 2)
        except ValueError:
            print(f"Row{row_num:>2d}: Couldn't parse {stock}")
    return total_cost

if len(sys.argv) == 2:
    path = sys.argv[1]
else:
    path = 'Work/Data/portfoliodate.csv'
    
cost = portfolio_cost(path)
print("Total cost: ", cost)