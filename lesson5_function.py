import csv


def total_by_product(path):
    totals = {}
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            product = row["product"]
            totals[product] = totals.get(product, 0) + int(row["amount"])
    return totals


totals = total_by_product("sales.csv")
for product, total in totals.items():
    print(product, "ขายได้", total, "บาท")
