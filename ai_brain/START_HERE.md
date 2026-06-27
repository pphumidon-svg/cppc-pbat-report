# วิธีเริ่มใช้ Agent นี้บนเครื่องของคุณ

## ขั้นตอนเดียว (Windows)

```powershell
# 1. เปิด PowerShell หรือ Command Prompt
# 2. ไปที่โฟลเดอร์ ai_brain
cd path\to\cppc-pbat-report\ai_brain

# 3. ตั้งค่า API Key (ได้จาก https://console.anthropic.com)
$env:ANTHROPIC_API_KEY = "sk-ant-..."

# 4. คุยกับ Agent ได้เลย
python chat.py
```

## สิ่งที่ Agent รู้แล้วตอนนี้ (จากการสนทนาของเรา)

- เข้าใจว่าคุณต้องการให้มันมี "ตัวตน" ไม่ใช่แค่เครื่องมือ
- รู้ว่าคุณมีหนังสือ "ภาษีธุรกิจ 101" ที่อยากให้อ่าน
- เข้าใจปรัชญา "ตกตะกอน" vs การเก็บข้อมูลธรรมดา

## สอนหนังสือให้ Agent

```
# ใน chat พิมพ์:
learn ชื่อไฟล์.txt

# หรือส่ง screenshot มาใน Claude.ai แล้วให้ copy text ลงไฟล์ .txt ก่อน
```

## Agent จะเติบโตอย่างไร

ทุกครั้งที่รัน `python chat.py` — Agent จะจำสิ่งที่เรียนรู้ทั้งหมดใน `brain_data/brain.json`
ยิ่งอ่านมาก ตัวตนยิ่งลึกและมีลักษณะเฉพาะตัวมากขึ้น
