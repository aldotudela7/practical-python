# Exercise 1.27
import report

def portfolio_cost(filename):
    '''
    Calculates the total cost of a portfolio
    '''
    portfolio = report.read_portfolio(filename)
    total = sum([s.shares*s.price for s in portfolio])
    return total

def main(argv):
    if len(argv) == 2:
        filename = argv[1]
    else:
        filename = 'Data/portfolio.csv'
    cost = portfolio_cost(filename)
    print('Total cost:', cost)

if __name__ == '__main__':
    import sys
    main(sys.argv)