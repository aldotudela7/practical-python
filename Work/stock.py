#!/usr/bin/env python3
# stock.py
#
# Exercise 4.1
from typedproperty import String, Integer, Float

class Stock:
    '''
    An instance of a stock holding consisting of name, shares, price.
    '''
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'

    @property
    def cost(self):
        return self.shares*self.price
    
    def sell(self, number):
        self.shares = self.shares-number
