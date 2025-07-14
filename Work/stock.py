from typedproperty import *

class Stock:
    name = String('name')
    shares = Integer('_shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return(f'Stock(\'{self.name:s}\', {self.shares}, {self.price:.2f})')

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, num):
        self.shares -= num


if __name__ == "__main__":
    goog = Stock('GOOG', 99, 490.10)
