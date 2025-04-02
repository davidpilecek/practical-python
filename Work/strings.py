#ex1.13

symlist = ['HPQ', 'AA', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']

mysym = []

name = 'IBM'
shares = 100
price = 91.1

stock = f'{shares} shares of {name} at $ {price:0.1f}'
symlist.append("HTQ")
symlist.insert(0, 'BREH')
symlist.remove("HTQ")
print(symlist.count("AA"))
symlist.sort()

print(symlist)

""" 
for s in sym_list:
    print('s=', s)
 """

