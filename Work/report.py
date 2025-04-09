# report.py
#
# Exercise 2.4

import csv
from pprint import pprint
from collections import Counter

path_portfolio = r"C:\Users\David\Desktop\practical-python\Work\Data\portfolio.csv"
path_prices = r"C:\Users\David\Desktop\practical-python\Work\Data\prices.csv"

def read_portfolio(filename):
    '''Returns a portfolio as a list, made from a file'''
    portfolio = []
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        header = next(rows)
        for row_nr, row in enumerate(rows):
            stock_dict = dict(zip(header, row))
            stock_dict['shares'] = int(stock_dict['shares'])
            stock_dict['price'] = float(stock_dict['price'])
            portfolio.append(stock_dict)

        return portfolio
    
def read_prices(filename):
    '''Reads file with prices of stocks, puts into dictionary'''
    price_dict = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                price_dict[row[0]] = float(row[1])
            except Exception as e:
                print(e)
    return price_dict

def calc_gain(portfolio, prices):
    cost_purchase = 0
    cost_current = 0
    gain = 0

    for stock in portfolio:
        name = stock["name"]
        past_price = stock['price']
        shares = stock["shares"]

        curr_price = prices[name]

        cost_purchase += shares * past_price
        cost_current += shares * curr_price
        gain = cost_current - cost_purchase
        
    print(cost_purchase)
    print(cost_current)
    print(gain)

def make_report(portfolio, prices):
    '''
    Creates a report of state of portfolio according to current prices.
    '''
    report = []

    for stock in portfolio:

        name = stock["name"]
        past_price = float(stock['price'])
        shares = int(stock["shares"])
        curr_price = prices[name]
        change = curr_price - past_price
        
        #print(f"{name:<10s} {shares:<10d} {curr_price:<10.2f} {change:<10.2f}")
        r = (name, shares, curr_price, change)
        report.append(r)
    return report

def print_report(report):
    '''
    Prints report into console.
    '''
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s'  % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in report:
        print('%10s %10d %10.2f %10.2f' % row)

def test(types, path):
    f = open(path)
    rows = csv.reader(f)
    header = next(rows)
    row = next(rows)

    converted = [func(val) for func,val in zip(types, row)]
    record = dict(zip(header, converted))

    record["date"] = tuple([int(d) for d in record["date"].split('/')])
        
def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)

if __name__ == "__main__":
    portfolio_report(path_portfolio, path_prices)





 