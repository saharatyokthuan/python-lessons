# บทเรียนที่ 5: อ่านไฟล์ CSV และสรุปข้อมูล 🎯

> **เป้าหมายบทสุดท้าย:** อ่านไฟล์จริง → แปลงข้อมูล → สรุปยอด → ห่อเป็นฟังก์ชัน แล้วปิดจ็อบด้วยโปรเจกต์จบ
> โค้ดทุกตัวอย่างในบทนี้ **รันผ่านทดสอบมาแล้ว**

---

## 1. ทบทวน: อ่านไฟล์ CSV

โค้ดอยู่ที่ไฟล์ `lesson5_read.py` (เป็นโค้ดตัวเดียวกับที่เราเคยรันในวันแรก!):

```python
import csv

with open("sales.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["product"], row["amount"])
```

**อธิบาย (ทบทวน):**

- `import csv` — เครื่องมืออ่าน CSV มีมาให้ใน Python แล้ว (ไม่ต้องติดตั้งเพิ่ม)
- `open("sales.csv", encoding="utf-8")` — เปิดไฟล์, `encoding="utf-8"` บอกว่ารองรับอักษร UTF-8 (ภาษาไทย)
- `with ... as f:` — ใช้เสร็จแล้วปิดไฟล์ให้อัตโนมัติ (จำรูปแบบนี้ไว้ใช้ได้เลย)
- `csv.DictReader(f)` — อ่านหัวตาราง (`date`, `product`, `amount`) เป็น "ป้าย" แล้วคืนแต่ละแถวออกมาเป็น **dict!**
- `row["product"]` — เปิดช่องตามป้ายของแถวนั้น (เหมือน dict บทที่ 3 เป๊ะ)

### 🔮 ทายก่อนรัน

1. โค้ดนี้จะ print ทั้งหมดกี่บรรทัด? (sales.csv มีข้อมูลกี่แถว)
2. ค่า `row["amount"]` ที่ได้เป็น type อะไร? (ย้อนไปวันแรก…)

### ✅ เฉลย

<details>
<summary>กดดูเฉลย</summary>

```
pen 120
book 350
pen 80
bag 450
book 350
pen 200
bag 450
pen 150
```

8 บรรทัด (ไฟล์มีข้อมูล 8 แถว) — และทุกค่าเป็น **str** ตามที่คุณตอบถูกในวันแรก! นี่คือกับดักที่เจอบ่อยสุดในงานข้อมูลจริง: ตัวเลขในไฟล์ CSV ไม่ใช่ตัวเลขใน Python จนกว่าเราจะแปลง

</details>

---

## 2. แปลง + สรุปยอดต่อสินค้า

โจทย์: หายอดขายรวมของสินค้าแต่ละชนิด

โค้ดอยู่ที่ไฟล์ `lesson5_total.py`:

```python
import csv

totals = {}
with open("sales.csv", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        product = row["product"]
        amount = int(row["amount"])
        totals[product] = totals.get(product, 0) + amount

print(totals)
```

**อธิบาย — นี่คือการรวมทุกบทที่เรียนมา:**

- `totals = {}` — dict เปล่าไว้สะสมยอด (บทที่ 3)
- `int(row["amount"])` — **แปลง str → int ก่อนบวก!** (กับดักบทที่ 1 — ลืมแล้วพังทันที)
- `totals.get(product, 0) + amount` แล้วเก็บทับ — ท่าไม้ตายจากบทที่ 3: "ยอดเดิม (ถ้าไม่มี = 0) + ยอดใหม่"
- ทุกครั้งที่ loop วน 1 แถว → ยอดของสินค้านั้นถูกบวกเพิ่มเรื่อยๆ จนจบไฟล์

### 🔮 ทายก่อนรัน

`print(totals)` ออกมาเป็น dict อะไร? pen / book / bag ยอดละเท่าไหร่? (ดูจากไฟล์จริงด้านบน)

### ✅ เฉลย

<details>
<summary>กดดูเฉลย</summary>

```
{'pen': 550, 'book': 700, 'bag': 900}
```

- pen: 120 + 80 + 200 + 150 = 550
- book: 350 + 350 = 700
- bag: 450 + 450 = 900

</details>

---

## 3. ห่อเป็นฟังก์ชัน + แสดงผลสวยๆ

โจทย์: ทำเป็นฟังก์ชันใช้ซ้ำได้ กับไฟล์ไหนก็ได้ + print ให้อ่านง่าย

โค้ดอยู่ที่ไฟล์ `lesson5_function.py`:

```python
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
```

**อธิบาย:**

- ห่อทั้งหมดเป็น `total_by_product(path)` — รับชื่อไฟล์เข้า คืน dict ยอดรวมออกมา (บทที่ 4)
- `for product, total in totals.items():` — **ของใหม่!** `.items()` วน dict ออกมาเป็น**คู่** (ป้าย, ค่า) เตรียมรับด้วยตัวแปร 2 ตัว
- ครั้งแรกที่เห็นอาจดูเยอะ — อ่านว่า "สำหรับแต่ละคู่ (ป้าย, ค่า) ใน totals..." ก็พอ

### 🔮 ทายก่อนรัน

3 บรรทัดที่ print ออกมาคืออะไรบ้าง?

### ✅ เฉลย

<details>
<summary>กดดูเฉลย</summary>

```
pen ขายได้ 550 บาท
book ขายได้ 700 บาท
bag ขายได้ 900 บาท
```

</details>

---

## 4. จุดพลาดบ่อย

1. **ลืม `int()`** → เจอ `TypeError: can only concatenate str (not "int") to str` (ข้อความนี้เจอกันมาแล้วในบทที่ 1!)
2. **ไฟล์อยู่คนละที่** → `FileNotFoundError: ... No such file or directory`
   รันจากโฟลเดอร์ที่มีไฟล์ (ที่นี่คือรันใน `/root/python-lessons`) หรือใส่ path เต็ม
3. **คิดว่า DictReader ให้ตัวเลขมาแล้ว** — ไม่! ทุกอย่างเป็น str เสมอ จนกว่าเราจะแปลง (กับดักที่ 1 ในงานข้อมูล)
4. **ลืม `:` / เยื้องผิด** — กฎเดียวกับ if/for/def ทุกประการ

---

## 5. แบบฝึกหัด (ชุดสุดท้าย!)

### ข้อ 1 — เติมโค้ดให้สมบูรณ์

หาสินค้าที่ขายดีที่สุด:

```python
totals = {"pen": 550, "book": 700, "bag": 900}

best_product = None
best_total = 0
for product, total in totals.items():
    # เติม: ถ้ายอดนี้มากกว่าสถิติสูงสุดเดิม ให้อัปเดต best_product กับ best_total ทั้งคู่
    ???

print("ขายดีสุด:", best_product, "ยอด", best_total, "บาท")
```

**ผลลัพธ์ที่คาดหวัง:** `ขายดีสุด: bag ยอด 900 บาท`

### ข้อ 2 — แก้บั๊ก

โค้ดนี้พังด้วย TypeError — หาสาเหตุและแก้ให้บวกได้:

```python
import csv

with open("sales.csv", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        print(row["amount"] + 10)
```

**ผลลัพธ์ที่คาดหวังหลังแก้:** `130` `360` `90` `460` `360` `210` `460` `160` (บรรทัดละค่า)

### ข้อ 3 — โปรเจกต์จบหลักสูตร 🏆

ไปที่ไฟล์ `exercise1.py` — มี `???` อยู่ 2 จุด ให้เติมให้ครบ:

```python
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
```

เติมเสร็จแล้ว **ตรวจคำตอบอัตโนมัติ** ได้เลย:

```bash
cd /root/python-lessons
python3 /root/.config/opencode/skills/code-teacher/scripts/check_exercise.py exercise1.py exercise1_tests.json
```

---

## 6. เฉลยแบบฝึกหัด

<details>
<summary>กดดูเฉลย</summary>

**ข้อ 1:**

```python
for product, total in totals.items():
    if total > best_total:
        best_product = product
        best_total = total
```

→ `ขายดีสุด: bag ยอด 900 บาท` (เริ่มจาก 0 แล้วเจอ 550 → 700 → 900 ไต่ขึ้นเรื่อยๆ)

**ข้อ 2:** ลืมแปลง str → int

```python
print(int(row["amount"]) + 10)
```

→ `130` `360` `90` `460` `360` `210` `460` `160`

**ข้อ 3:** ฉบับสมบูรณ์ของ `exercise1.py`

```python
import csv


def total_by_product(path):
    totals = {}
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            amount = int(row["amount"])

            product = row["product"]
            totals[product] = totals.get(product, 0) + amount

    return totals


print(total_by_product("sales.csv"))
```

ผลรันสคริปต์ตรวจ (เมื่อเติมถูกครบ):

```
{'pen': 550, 'book': 700, 'bag': 900}
[PASS] เคสที่ 1: total_by_product('sales.csv') = {'pen': 550, 'book': 700, 'bag': 900}

สรุป: ผ่าน 1/1 เคส
ยินดีด้วย! ทุกเคสผ่านหมด
```

> บรรทัดแรกคือ output ของ `print` ท้ายไฟล์ (ตัวตรวจ import ไฟล์เราจึงเห็น print ด้วย) — ปกติ ไม่ต้องตกใจ 🙂

</details>

---

## 7. สรุป + จบหลักสูตร 🎓

**ทักษะทั้งหมดในคอร์สนี้:**

| บท | ทักษะ | ใช้จริงกับงานข้อมูลยังไง |
|---|---|---|
| 1 | ตัวแปร + ชนิดข้อมูล | รู้ว่า `"120"` ≠ `120` — กับดักอันดับ 1 |
| 2 | if + for | ให้โปรแกรมตัดสินใจ / ไล่ทีละแถว |
| 3 | list + dict | เก็บรายการ และสรุปยอดเป็นคู่ ป้าย–ค่า |
| 4 | ฟังก์ชัน | ห่องานเป็นก้อน reuse ได้ |
| 5 | CSV | อ่านไฟล์จริง → แปลง → สรุป |

**ก้าวต่อไปที่แนะนำ (เลือกทำได้เลย):**
1. **สร้างไฟล์ CSV ของตัวเอง** — เอาข้อมูลที่สนใจ (รายรับรายจ่าย, คะแนนสอบ) มาลองสรุปยอด/เฉลี่ย/หาตัวมากสุด
2. **ต่อยอด exercise1** — เพิ่มฟังก์ชันหาวันที่ยอดขายสูงสุด / นับจำนวนออเดอร์ต่อสินค้า
3. **ลอง pandas** — ไลบรารีวิเคราะห์ข้อมูลยอดนิยมของ Python: อ่าน CSV 1 บรรทัดแทน 10 บรรทัด และมีฟีเจอร์เพียบ (นี่คือก้าวถัดไปตามธรรมชาติของสายนี้)

**จำไว้:** คุณพิชิตครบทุกเครื่องมือพื้นฐานของ "อ่านข้อมูล → สรุปผล" แล้ว 🎉 เหลือแค่ฝึกกับข้อมูลจริงบ่อยๆ
