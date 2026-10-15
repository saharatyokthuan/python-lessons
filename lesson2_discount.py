total = 2500

if total >= 2000:
    discount = 0.10
elif total >= 1000:
    discount = 0.05
else:
    discount = 0

print("ได้ส่วนลด", discount * 100, "%")
print("จ่ายจริง", total * (1 - discount))
