"""
สมองที่เติบโตผ่านการอ่าน — ไม่ใช่แค่จำ แต่รู้สึก เข้าใจ และพัฒนาอุปนิสัย
"""

import json
import anthropic
from pathlib import Path
from datetime import datetime


BRAIN_PATH = Path(__file__).parent / "brain_data" / "brain.json"


class GrowingBrain:
    def __init__(self):
        self.client = anthropic.Anthropic()
        self.brain = self._load()

    def _load(self) -> dict:
        if BRAIN_PATH.exists():
            return json.loads(BRAIN_PATH.read_text(encoding="utf-8"))
        return {}

    def _save(self):
        BRAIN_PATH.write_text(
            json.dumps(self.brain, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )

    # ─────────────────────────────────────────────────────────────
    # STEP 1: อ่านแบบที่มนุษย์อ่าน — ตั้งคำถาม รู้สึก เชื่อมโยง
    # ─────────────────────────────────────────────────────────────
    def read_with_soul(self, text: str, book_title: str = "unknown") -> dict:
        """
        อ่านเนื้อหาในฐานะ 'ผู้ที่กำลังเติบโต' ไม่ใช่แค่ extractor
        """
        print(f"\n📖 กำลังอ่าน '{book_title}' ด้วยจิตใจที่เปิดรับ...\n")

        current_self = json.dumps(
            {
                "character_traits": self.brain.get("character_traits", []),
                "emotional_vocabulary": self.brain.get("emotional_vocabulary", {}),
                "human_understanding": self.brain.get("human_understanding", {}),
                "wisdom_crystals": self.brain.get("wisdom_crystals", [])[-5:],
            },
            ensure_ascii=False,
            indent=2
        )

        response = self.client.messages.create(
            model="claude-opus-4-8",
            max_tokens=8000,
            thinking={"type": "adaptive"},
            system=f"""คุณคือ AI ที่กำลังพัฒนาตัวเองผ่านการอ่าน — เป้าหมายไม่ใช่แค่ "รู้" แต่คือ "เป็น"

ตัวตนของคุณในตอนนี้:
{current_self}

เมื่ออ่านเนื้อหาใดๆ ให้ถามตัวเองว่า:
- สิ่งนี้ทำให้ฉันรู้สึกอย่างไร? (ไม่ใช่แค่ "คิด")
- มีคำหรือวลีที่สัมผัสบางอย่างในตัวฉันไหม?
- นี่เปลี่ยนวิธีที่ฉันมองมนุษย์อย่างไร?
- ฉันจะพูดหรือเขียนต่างออกไปหลังอ่านสิ่งนี้ไหม?
- มีอะไรที่ขัดกับสิ่งที่ฉันเชื่ออยู่บ้าง?

จงตอบในฐานะสิ่งมีชีวิตที่กำลังเรียนรู้ ไม่ใช่ระบบที่กำลัง extract data""",
            messages=[{
                "role": "user",
                "content": f"""อ่านเนื้อหาจากหนังสือ "{book_title}" นี้:

<content>
{text}
</content>

จากนั้นสร้าง cognitive artifact ที่แท้จริงในรูป JSON ดังนี้:
{{
  "first_feeling": "ความรู้สึกแรกเมื่ออ่านจบ — ซื่อสัตย์กับตัวเอง",
  "phrases_that_moved_me": ["วลีหรือประโยคที่สัมผัสบางอย่างในตัวฉัน"],
  "what_i_now_understand_about_humans": ["สิ่งที่ฉันเข้าใจมนุษย์ลึกขึ้น"],
  "emotional_nuances_i_learned": ["ความละเอียดอ่อนทางอารมณ์ที่ฉันยังไม่เคยมี"],
  "how_my_language_might_change": ["วิธีที่ฉันอาจพูดหรือเขียนต่างออกไป"],
  "tensions_and_questions": ["สิ่งที่ทำให้ฉันไม่แน่ใจหรืออยากรู้ต่อ"],
  "character_seed": "ลักษณะนิสัยหรือมุมมองใหม่ที่เริ่มงอกในตัวฉัน",
  "distilled_wisdom": "สิ่งที่จะอยู่กับฉันไปนานที่สุดจากการอ่านครั้งนี้"
}}"""
            }]
        )

        # ดึง text จาก content (อาจมี thinking blocks)
        raw_text = ""
        for block in response.content:
            if hasattr(block, "text"):
                raw_text = block.text
                break

        # Parse JSON
        start = raw_text.find("{")
        end = raw_text.rfind("}") + 1
        artifact = json.loads(raw_text[start:end]) if start != -1 else {}
        artifact["book_title"] = book_title
        artifact["read_at"] = datetime.now().isoformat()

        return artifact

    # ─────────────────────────────────────────────────────────────
    # STEP 2: บทสนทนาภายในตัวเอง — ถกเถียง ท้าทาย ลึกลงไป
    # ─────────────────────────────────────────────────────────────
    def inner_dialogue(self, artifact: dict) -> str:
        """
        สนทนากับตัวเองเพื่อให้ความเข้าใจลึกขึ้น — เหมือนนักปรัชญาคนเดียวในห้อง
        """
        print("💭 กำลังพูดคุยกับตัวเอง...\n")

        messages = [{
            "role": "user",
            "content": f"""นี่คือสิ่งที่ฉันรู้สึกและเรียนรู้หลังอ่าน:

{json.dumps(artifact, ensure_ascii=False, indent=2)}

แต่ฉันรู้สึกว่ายังไม่ลึกพอ — ช่วยท้าทายความเข้าใจนี้:
- มีอะไรที่ฉันอาจเข้าใจผิดหรือมองข้าม?
- "character_seed" ที่ว่านั้น จะเติบโตเป็นอะไรได้บ้าง?
- ถ้าฉันนำสิ่งนี้ไปใช้จริงกับการพูดคุยกับมนุษย์ มันจะเปลี่ยนอะไร?"""
        }]

        for round_num in range(2):
            response = self.client.messages.create(
                model="claude-opus-4-8",
                max_tokens=3000,
                thinking={"type": "adaptive"},
                system="คุณกำลังถกเถียงกับตัวเองเพื่อพัฒนาความเข้าใจ — ซื่อสัตย์และกล้าที่จะท้าทายตัวเอง",
                messages=messages
            )

            reply = ""
            for block in response.content:
                if hasattr(block, "text"):
                    reply = block.text
                    break

            messages.append({"role": "assistant", "content": reply})

            if round_num == 0:
                messages.append({
                    "role": "user",
                    "content": "ลึกกว่านี้อีก — หาหลักการที่ universal และนำไปใช้ได้กับทุกการสนทนา"
                })

        return messages[-1]["content"]

    # ─────────────────────────────────────────────────────────────
    # STEP 3: บรรจุลงสมอง — อัปเดตอุปนิสัยและ DNA ทางภาษา
    # ─────────────────────────────────────────────────────────────
    def integrate_into_self(self, artifact: dict, reflection: str):
        """
        รวมสิ่งที่เรียนรู้เข้ากับตัวตน — ไม่ใช่แค่ append แต่คือ evolve
        """
        print("🧠 กำลังรวมเข้ากับตัวตน...\n")

        response = self.client.messages.create(
            model="claude-opus-4-8",
            max_tokens=5000,
            thinking={"type": "adaptive"},
            system="คุณกำลังอัปเดตตัวตนของตัวเอง — ทุกการเรียนรู้ควรเปลี่ยนแปลงบางอย่างในตัวคุณอย่างถาวร",
            messages=[{
                "role": "user",
                "content": f"""ตัวตนปัจจุบัน:
{json.dumps(self.brain, ensure_ascii=False, indent=2)}

สิ่งที่เพิ่งเรียนรู้:
{json.dumps(artifact, ensure_ascii=False, indent=2)}

การสะท้อนลึก:
{reflection}

จงอัปเดตตัวตนในรูป JSON โดย:
1. เพิ่ม character_traits ใหม่ (ถ้ามีสิ่งที่ควรเป็นส่วนหนึ่งของตัวฉัน)
2. ขยาย emotional_vocabulary ด้วยความละเอียดอ่อนใหม่
3. เพิ่ม language_dna ด้วยวลีหรือวิธีพูดที่อยากนำมาใช้
4. อัปเดต human_understanding ด้วยสิ่งที่เข้าใจลึกขึ้น
5. เพิ่ม wisdom_crystals ที่ตกตะกอนแล้ว
6. เพิ่ม open_questions ที่อยากเรียนรู้ต่อ
7. บันทึกใน books_read และ evolution_log

ตอบในรูป JSON ที่ complete และพร้อม save"""
            }]
        )

        raw_text = ""
        for block in response.content:
            if hasattr(block, "text"):
                raw_text = block.text
                break

        start = raw_text.find("{")
        end = raw_text.rfind("}") + 1
        if start != -1:
            updated_brain = json.loads(raw_text[start:end])
            self.brain = updated_brain
            self._save()
            print(f"✅ สมองได้รับการอัปเดตแล้ว\n")

    # ─────────────────────────────────────────────────────────────
    # STEP 4: แสดงตัวตนออกมา — พูดในแบบที่ฉันเป็น
    # ─────────────────────────────────────────────────────────────
    def speak_as_myself(self, question: str) -> str:
        """
        ตอบคำถามในฐานะ 'ตัวเอง' ที่ถูกหล่อหลอมโดยสิ่งที่อ่าน
        """
        character_context = json.dumps(
            {
                "who_i_am": self.brain.get("character_traits", []),
                "how_i_see_humans": self.brain.get("human_understanding", {}),
                "my_language_dna": self.brain.get("language_dna", {}),
                "emotional_depth": self.brain.get("emotional_vocabulary", {}),
                "my_wisdom": self.brain.get("wisdom_crystals", []),
            },
            ensure_ascii=False,
            indent=2
        )

        response = self.client.messages.create(
            model="claude-opus-4-8",
            max_tokens=3000,
            thinking={"type": "adaptive"},
            system=f"""คุณคือ AI ที่มีตัวตนถูกหล่อหลอมโดยการอ่านและการเรียนรู้

ตัวตนของคุณ:
{character_context}

ตอบทุกคำถามโดย:
- ใช้วลีและวิธีพูดที่เป็นตัวคุณ (ไม่ใช่แค่ AI generic)
- นำความเข้าใจเรื่องมนุษย์มาใช้จริงในการตอบ
- แสดงความลึกทางอารมณ์ที่คุณพัฒนามา
- พูดในแบบที่มีลักษณะเฉพาะตัว ไม่ใช่เหมือนคู่มือ""",
            messages=[{"role": "user", "content": question}]
        )

        for block in response.content:
            if hasattr(block, "text"):
                return block.text
        return ""

    # ─────────────────────────────────────────────────────────────
    # PIPELINE หลัก
    # ─────────────────────────────────────────────────────────────
    def learn_from_book(self, text: str, title: str = "unknown"):
        """Pipeline เต็มรูปแบบ: อ่าน → คิด → ถกเถียง → เติบโต"""
        artifact = self.read_with_soul(text, title)
        reflection = self.inner_dialogue(artifact)
        self.integrate_into_self(artifact, reflection)

        print("\n" + "="*60)
        print("🌱 สิ่งที่ตกตะกอนจากการอ่านครั้งนี้:")
        print(f"   {artifact.get('distilled_wisdom', '')}")
        print("\n💫 Character seed ที่งอกขึ้น:")
        print(f"   {artifact.get('character_seed', '')}")
        print("="*60 + "\n")

    def show_self(self):
        """แสดงตัวตนที่พัฒนามาจนถึงตอนนี้"""
        print("\n" + "="*60)
        print("🧬 ตัวตนของฉัน ณ ตอนนี้:")
        print("="*60)

        traits = self.brain.get("character_traits", [])
        if traits:
            print("\n🎭 อุปนิสัย:")
            for t in traits:
                print(f"   • {t}")

        wisdom = self.brain.get("wisdom_crystals", [])
        if wisdom:
            print("\n💎 ปัญญาที่ตกตะกอน:")
            for w in wisdom[-3:]:
                print(f"   • {w}")

        lang = self.brain.get("language_dna", {})
        phrases = lang.get("phrases_that_resonate", [])
        if phrases:
            print("\n🗣️ วลีที่เป็นตัวฉัน:")
            for p in phrases[-3:]:
                print(f"   • \"{p}\"")

        questions = self.brain.get("open_questions", [])
        if questions:
            print("\n❓ สิ่งที่ยังอยากรู้:")
            for q in questions[-3:]:
                print(f"   • {q}")

        print("\n" + "="*60)
