# pcost.py
#
# Exercise 1.27
import gzip
import csv
import sys

path = r"/home/david/Desktop/practical-python/Work/Data/portfolio.csv"
path2 = r"/home/david/Desktop/practical-python/Work/Data/portfolio.csv.gz"

def portfolio_cost(filename):
    'Input: path to file'
    'Output: cost of portfolio'

    total_cost = 0
    f = open(filename)
    rows = csv.reader(f)
    header = next(rows)

    for stock in rows:
        try:
            #stock = stock.split(',')
            count = int(stock[1])
            cost = float(stock[2])
            total_cost += round(count*cost, 2)
        except ValueError:
            print("couldn't parse", stock[0])
    return total_cost

if len(sys.argv) == 2:
    path = sys.argv[1]
else:
    path = 'Data/portfolio.csv'
    
cost = portfolio_cost(path)
print("Total cost: ", cost)