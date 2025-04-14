# pcost.py
#
# Exercise 1.27
import gzip
import csv
import sys
from Work.report_mine import read_portfolio

path = r"/home/david/Desktop/practical-python/Work/Data/portfolio.csv"
path2 = r"/home/david/Desktop/practical-python/Work/Data/portfolio.csv.gz"

def portfolio_cost(filename):
    'Input: path to file'
    'Output: cost of portfolio'
    total_cost = 0
    portfolio = read_portfolio(filename)
    for row_num, stock in enumerate(portfolio, 1):
        stock = list(stock.values())
        try:
            count = int(stock[1])
            cost = float(stock[2])
            total_cost += round(count*cost, 2)
        except ValueError:
            print(f"Row{row_num:>2d}: Couldn't parse {stock}")
    return total_cost

cost = portfolio_cost(path)
print("Total cost: ", cost)