# report.py

import fileparse
import stock 

a = stock.Stock("GOOG", 100, 141.2)
b = stock.Stock("AAPL", 50, 550.1)
s = stock.Stock('GOOG', 100, 490.10)
c = stock.Stock("FANO", 69, 12.1)

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as lines:
        return fileparse.parse_csv(lines, select=['name','shares','price'], types=[str,int,float])

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    with open(filename) as lines:
        return dict(fileparse.parse_csv(lines, types=[str,float], has_headers=False))

def make_report_data(portfolio,prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    rows = []
    for stock in portfolio:
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        summary = (stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
    return rows

def print_report(reportdata):
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    '''
    headers = ('Name','Shares','Price','Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-'*10 + ' ')*len(headers))
    for row in reportdata:
        print('%10s %10d %10.2f %10.2f' % row)

def portfolio_report(portfoliofile, pricefile):        
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files 
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report_data(portfolio, prices)

    # Print it out
    print_report(report)

def main(args):
    if len(args) != 3:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    portfolio_report(args[1], args[2])

if __name__ == '__main__':
    with open(r'Work/Data/portfolio.csv') as lines:
        portdicts = fileparse.parse_csv(lines, select=['name','shares','price'], types=[str,int,float])

        print(portdicts)
        portfolio = [stock.Stock(port['name'], port['shares'], port['price']) for port in portdicts]
        print(sum([s.cost() for s in portfolio]))