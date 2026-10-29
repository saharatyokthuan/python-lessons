# หลักสูตร Python สู่การวิเคราะห์ข้อมูล 📊

**ผู้เรียน:** ระดับพื้นฐานเล็กน้อย
**เป้าหมาย:** วิเคราะห์ข้อมูล / งานอัตโนมัติ
**วิธีการเรียน:** อ่าน → **ทายผลก่อนรัน** → รันโค้ดเอง → ทำแบบฝึกหัด → เทียบเฉลย

🔗 **ใช้งานออนไลน์:** https://saharatyokthuan.github.io/python-lessons/

---

## เส้นทางการเรียน (เนื้อหาครบทั้ง 5 บทแล้ว ✅)

| บทที่ | เรื่อง | เอกสาร | โค้ดตัวอย่าง |
|---|---|---|---|
| 1 | ตัวแปรและชนิดข้อมูล | [lessons/lesson-01.md](lessons/lesson-01.md) | `lesson1_basic.py` |
| 2 | เงื่อนไข (if) และลูป (for) | [lessons/lesson-02.md](lessons/lesson-02.md) | `lesson2_if.py`, `lesson2_discount.py`, `lesson2_loop.py` |
| 3 | list กับ dict | [lessons/lesson-03.md](lessons/lesson-03.md) | `lesson3_list.py`, `lesson3_loop.py`, `lesson3_dict.py` |
| 4 | ฟังก์ชัน (function) | [lessons/lesson-04.md](lessons/lesson-04.md) | `lesson4_greet.py`, `lesson4_return.py`, `lesson4_discount.py` |
| 5 | อ่านไฟล์ CSV และสรุปข้อมูล 🎯 | [lessons/lesson-05.md](lessons/lesson-05.md) | `lesson5_read.py`, `lesson5_total.py`, `lesson5_function.py` |

---

## ไฟล์ในโฟลเดอร์นี้

| ไฟล์ | ใช้ทำอะไร |
|---|---|
| `README.md` | ภาพรวมหลักสูตร (ไฟล์นี้) |
| `manual.md` | **คู่มือการใช้** — คำสั่งรันทั้งหมด วิธีตรวจแบบฝึกหัด ตารางติดตามความคืบหน้า ปัญหาที่พบบ่อย |
| `lessons/lesson-01.md` … `lesson-05.md` | บทเรียนฉบับเต็ม — โจทย์ + เฉลยซ่อนใน `<details>` (เนื้อหาทุกบททดสอบรันจริงมาแล้ว) |
| `lesson1_basic.py` | ตัวอย่างบท 1: ตัวแปรและชนิดข้อมูล |
| `lesson2_*.py` | ตัวอย่างบท 2: if / elif / else และ for + range |
| `lesson3_*.py` | ตัวอย่างบท 3: list, วน list, dict |
| `lesson4_*.py` | ตัวอย่างบท 4: ฟังก์ชัน, return, ฟังก์ชัน + if |
| `lesson5_*.py` | ตัวอย่างบท 5: อ่าน CSV, สรุปยอด, ห่อเป็นฟังก์ชัน |
| `sales.csv` | ข้อมูลตัวอย่าง (ใช้ตั้งแต่บท 5) |
| `exercise1.py` | **โปรเจกต์จบบท 5** — เติม `???` ให้ครบ |
| `exercise1_tests.json` | ชุดทดสอบสำหรับตรวจ `exercise1.py` อัตโนมัติ |

## วิธีรันโค้ด

```bash
cd /root/python-lessons
python3 lesson1_basic.py     # เปลี่ยนชื่อไฟล์ตามบทที่กำลังเรียน
```

## ตรวจโปรเจกต์จบ (หลังเติม exercise1.py ครบ)

```bash
cd /root/python-lessons
python3 /root/.config/opencode/skills/code-teacher/scripts/check_exercise.py exercise1.py exercise1_tests.json
```

---

## กติกาการเรียน (สำคัญ)

1. **ทายผลก่อนรันทุกครั้ง** — ผิดไม่เป็นไร การทายคือการเรียน
2. **พิมพ์โค้ดเอง อย่า copy ทั้งดุ้น** — มือจะจำได้ดีกว่าตา
3. เจอ error → อ่าน**บรรทัดสุดท้าย**ของ error message ก่อนเสมอ
4. โค้ดทุกตัวอย่างผ่านการรันทดสอบมาแล้ว — ถ้าผลไม่ตรงเฉลย ให้เช็คว่าพิมพ์ครบหรือยัง
