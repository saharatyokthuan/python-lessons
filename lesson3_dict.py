row = {"product": "pen", "amount": 120}

print(row["product"])
row["amount"] = row["amount"] + 30
print(row)
print(row.get("color", "ไม่มีข้อมูล"))
