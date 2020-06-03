# report.py
#
# Exercise 2.4
from fileparse import parse_csv

def read_portfolio(filename):
    '''
    Reads a portfolio file into a list of dictionaries
    with keys: name, shares, and price.
    '''
    portfolio = parse_csv(filename, select=['name','shares','price'], types=[str, int, float])
    return portfolio

def read_prices(filename):
    '''
    Reads csv file of prices without header and stores 
    them in a dictionary.
    '''
    prices = dict(parse_csv(filename, has_headers=False))
    return prices

def make_report(stocks, prices):
    '''
    Reads from read_portfolio and read_prices functions
    and creates a list with the portfolio name, shares,
    current_price, and change.
    '''
    report = []
    for stock in stocks:
        name = stock['name']
        shares = int(stock['shares'])
        price = float(stock['price'])
        current_price = float(prices.get(stock['name']))
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

portfolio_report('Data/portfolio2.csv', 'Data/prices.csv')