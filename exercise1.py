import csv


def total_by_product(path):
    totals = {}
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            # ข้อ 1: เปลี่ยน row["amount"] จากข้อความ (str) เป็นตัวเลข (int)
            amount = ???

            product = row["product"]
            # ข้อ 2: บวก amount เข้า totals ของสินค้าชิ้นนี้
            ???

    return totals


print(total_by_product("sales.csv"))
