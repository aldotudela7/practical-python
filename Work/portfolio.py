# Exercise 1.27
import report
import sys

def portfolio_cost(filename):
    '''
    Calculates the total cost of a portfolio
    '''
    portfolio = report.read_portfolio(filename)
    total = sum([s['shares']*s['price'] for s in portfolio])
    return total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
