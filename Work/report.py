#!/usr/bin/env python3
# report.py
#
# Exercise 2.4
from fileparse import parse_csv
import stock

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

def print_report(report):
    '''
    Reads the output of make_report and prints a table
    of results to console.
    '''
    headers = ('Name','Shares','Price','Change')
    line = '-----------'
    print('%10s %10s %10s %10s' % headers)
    print('%10s %10s %10s %10s' % (line,line,line,line))
    for i in report:
        print('%10s %10d %10.2f %10.2f' % i)

def portfolio_report(portfolio_filename, prices_filename):
    '''
    Runs the functions in this script in sequence to get
    a summary of the portfolio and prices given.
    '''
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio,prices)
    print_report(report)

def main(argv):
    if len(argv) == 3:
        filenames = [argv[1], argv[2]]
    else:
        filenames = ['Data/portfolio.csv', 'Data/prices.csv']
    portfolio_report(filenames[0], filenames[1])

if __name__ == '__main__':
    import sys
    main(sys.argv)