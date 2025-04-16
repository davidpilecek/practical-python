import report
from tableformat import create_formatter, print_table

if __name__ == '__main__':
    portfolio = report.read_portfolio(r'Work\Data\portfolio.csv')
    formatter = create_formatter('txt')

    print_table(portfolio, ['name', 'price', 'shares'], formatter)