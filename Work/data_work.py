import csv

path = r"/home/david/Desktop/practical-python/Work/Data/portfolio.csv"

f = open(path)
rows = csv.reader(f)
next(rows)
row = next(rows)

d = {"name": row[0],
     "shares": int(row[1]), 
     "price":float(row[2])}
d["shares"] = 75
d["account"] = "Smith"
print(d)
print(d["shares"] * d["price"])