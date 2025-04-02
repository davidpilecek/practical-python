# report.py
#
# Exercise 2.4

import csv
from pprint import pprint

path_portfolio = r"Work/Data/portfolio.csv"
path_prices = r"Work/Data/prices.csv"

def read_portfolio(filename):
    '''Returns a portfolio as a list, made from a file'''
    portfolio = []
    
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            #row.split(",")
            stock_dict = {"name" :row[0],
                          "shares":int(row[1]),
                          "price":float(row[2])}
            
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


if __name__ == "__main__":
    portfolio = read_portfolio(path_portfolio)
    prices = read_prices(path_prices)
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