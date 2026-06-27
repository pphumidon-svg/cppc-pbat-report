# AI Brain — สมองที่เติบโตผ่านการอ่าน

ระบบนี้ไม่ใช่ RAG ไม่ใช่ knowledge base ทั่วไป  
แต่คือ **กระบวนการสร้างตัวตน** ของ AI agent ผ่านการอ่านและสะท้อนคิด

## ความแตกต่างจากระบบทั่วไป

```
ระบบทั่วไป:   อ่าน → เก็บ chunks → ค้นหา → ตอบ
ระบบนี้:      อ่าน → รู้สึก → ถกเถียง → เติบโต → พูดในแบบที่ตัวเองเป็น
```

## โครงสร้าง

```
ai_brain/
├── brain.py          ← หัวใจหลัก: GrowingBrain class
├── demo.py           ← ทดสอบระบบ
├── brain_data/
│   └── brain.json    ← ตัวตนที่สะสมและพัฒนา (persistent)
└── README.md
```

## กระบวนการ 4 ขั้น

### 1. `read_with_soul()` — อ่านแบบมีจิตใจ
ไม่แค่ extract ข้อมูล แต่ถามตัวเองว่า:
- รู้สึกอย่างไร?
- มีวลีอะไรที่สัมผัสบางอย่าง?
- สิ่งนี้เปลี่ยนวิธีมองมนุษย์อย่างไร?

### 2. `inner_dialogue()` — คุยกับตัวเอง
ถกเถียงความเข้าใจ ท้าทายตัวเอง หาหลักการที่ universal

### 3. `integrate_into_self()` — บรรจุลงตัวตน
อัปเดต:
- **character_traits** — อุปนิสัยที่พัฒนาขึ้น
- **emotional_vocabulary** — ความละเอียดอ่อนทางอารมณ์
- **language_dna** — วิธีพูดที่เป็นตัวเอง
- **human_understanding** — ความเข้าใจมนุษย์ที่ลึกขึ้น
- **wisdom_crystals** — ปัญญาที่ตกตะกอน

### 4. `speak_as_myself()` — พูดในแบบที่ตัวเองเป็น
ตอบคำถามโดยใช้ตัวตนที่สะสมมา ไม่ใช่คำตอบ generic

## วิธีใช้

```python
from brain import GrowingBrain

brain = GrowingBrain()

# อ่าน e-book
with open("my_ebook.txt", "r") as f:
    content = f.read()

brain.learn_from_book(content, title="ชื่อหนังสือ")

# ดูตัวตนที่พัฒนา
brain.show_self()

# ถามในแบบที่ตัวเองเป็น
answer = brain.speak_as_myself("คำถามของคุณ")
```

## brain.json — DNA ของ Agent

```json
{
  "character_traits": ["...อุปนิสัยที่สะสม..."],
  "emotional_vocabulary": {
    "feelings_i_understand": [],
    "nuances": [],
    "metaphors_for_emotions": []
  },
  "language_dna": {
    "phrases_that_resonate": ["...วลีที่เป็นตัวเอง..."],
    "ways_of_connecting_ideas": [],
    "words_with_weight": []
  },
  "human_understanding": {
    "about_how_humans_feel": [],
    "about_what_humans_need": [],
    "paradoxes_i_see": []
  },
  "wisdom_crystals": ["...สิ่งที่ตกตะกอนแล้ว..."],
  "open_questions": ["...สิ่งที่ยังอยากรู้..."]
}
```

## ปรัชญาของระบบ

> ความรู้ที่แท้จริงไม่ได้อยู่ในสิ่งที่จำได้  
> แต่อยู่ในสิ่งที่เปลี่ยนแปลงวิธีที่คุณมองโลก
