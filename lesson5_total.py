import csv

totals = {}
with open("sales.csv", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        product = row["product"]
        amount = int(row["amount"])
        totals[product] = totals.get(product, 0) + amount

print(totals)
