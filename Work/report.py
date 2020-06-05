#!/usr/bin/env python3
# report.py
#
# Exercise 2.4
from fileparse import parse_csv
import stock
import tableformat

def read_portfolio(filename):
    '''
    Reads a portfolio file into a list of dictionaries
    with keys: name, shares, and price.
    '''
    with open(filename) as lines:
        pdict = parse_csv(lines, select=['name','shares','price'], types=[str, int, float])
    portfolio = [ stock.Stock(d['name'], d['shares'], d['price']) for d in pdict]
    return portfolio

def read_prices(filename):
    '''
    Reads csv file of prices without header and stores 
    them in a dictionary.
    '''
    with open(filename) as lines:
        prices = dict(parse_csv(lines, has_headers=False))
    return prices

def make_report(stocks, prices):
    '''
    Reads from read_portfolio and read_prices functions
    and creates a list with the portfolio name, shares,
    current_price, and change.
    '''
    report = []
    for s in stocks:
        name = s.name
        shares = s.shares
        price = s.price
        current_price = float(prices.get(s.name))
        change = current_price - price
        row = (name, shares, current_price, change)
        report.append(row)
    return report

def print_report(reportdata, formatter):
    '''
    Reads the output of make_report and prints a table
    of results to console.
    '''
    formatter.headings(['Name','Shares','Price','Change'])
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)

    # headers = ('Name','Shares','Price','Change')
    # line = '-----------'
    # print('%10s %10s %10s %10s' % headers)
    # print('%10s %10s %10s %10s' % (line,line,line,line))
    # for i in report:
    #     print('%10s %10d %10.2f %10.2f' % i)

def portfolio_report(portfolio_filename, prices_filename, fmt='txt'):
    '''
    Runs the functions in this script in sequence to get
    a summary of the portfolio and prices given.
    '''
    # Read data files
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    # Create report
    report = make_report(portfolio,prices)
    # Print report
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

def main(argv):
    if len(argv) == 4:
        filenames = [argv[1], argv[2], argv[3]]
    else:
        filenames = ['Data/portfolio.csv', 'Data/prices.csv', 'txt']
    portfolio_report(filenames[0], filenames[1], filenames[2])

if __name__ == '__main__':
    import sys
    main(sys.argv)