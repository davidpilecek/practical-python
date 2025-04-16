
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return(f'Stock({self.name:s}, {self.shares}, {self.price:.2f})')

    def cost(self):
        self.stock_cost= self.shares * self.price
        return self.stock_cost

    def sell(self, num):
        self.shares -= num
        return self.shares

if __name__ == "__main__":
    s = Stock('GOOG', 100, 490.1)
    columns = ['name', 'shares']

    for colname in columns:
        print(colname, '=', getattr(s, colname))