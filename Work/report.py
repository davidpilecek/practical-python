# report.py

import fileparse
import stock 
import tableformat

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
        portfolio = fileparse.parse_csv(lines, select=['name','shares','price'], types=[str,int,float])
        portfolio_classes = [stock.Stock(s['name'], s['shares'], s['price']) for s in portfolio]
        return portfolio_classes
    
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
        current_price = prices[stock.name]
        change = current_price - stock.price
        summary = (stock.name, stock.shares, current_price, change)
        rows.append(summary)
    return rows

def print_report(reportdata, formatter):
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    '''
    formatter.headings(['Name','Shares','Price','Change'])
    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)


def portfolio_report(portfoliofile, pricefile, fmt:str):        
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files 
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report_data(portfolio, prices)
    formatter = tableformat.create_formatter(fmt)

    # Print it out
    print_report(report, formatter)

def main(args):
    if len(args) != 4:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    portfolio_report(args[1], args[2], args[3])

if __name__ == '__main__':
    main()