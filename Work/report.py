# report.py
#
# Exercise 2.4

import csv
from pprint import pprint
from collections import Counter

path_portfolio = r"C:\Users\David\Desktop\practical-python\Work\Data\portfolio.csv"
path_prices = r"Work/Data/prices.csv"

def read_portfolio(filename):
    '''Returns a portfolio as a list, made from a file'''
    portfolio = []
    
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        header = next(rows)
        for row_nr, row in enumerate(rows):
            #row.split(",")
            stock_dict = dict(zip(header, row))
            
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
    #print(f"Name {"":<5} Shares {"":>3} Price {"":>4} Change {"":<10}")
    #print("---------- ---------- ---------- -------")
    report = []

    for stock in portfolio:
        name = stock["name"]
        past_price = float(stock['price'])
        shares = int(stock["shares"])
        curr_price = prices[name]
        change = curr_price - past_price
        
        print(f"{name:<10s} {shares:<10d} {curr_price:<10.2f} {change:<10.2f}")
        r = (name, shares, curr_price, change)
        report.append(r)
    return report

if __name__ == "__main__":
    portfolio = read_portfolio(path_portfolio)
    portfolio2 = read_portfolio(r"C:\Users\David\Desktop\practical-python\Work\Data\portfolio2.csv")
    holdings = Counter()
    holdings2 = Counter()

    for s in portfolio2:
        holdings2[s['name']] += int(s['shares'])

    for s in portfolio:
        holdings[s['name']] += int(s['shares'])
    print(holdings2 + holdings)