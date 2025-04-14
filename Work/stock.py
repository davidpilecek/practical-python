
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        self.stock_cost= self.shares * self.price
        return self.stock_cost

    def sell(self, num):
        self.shares -= num
        return self.shares

