"""
คุยกับ Agent ที่มีตัวตนและเติบโตได้ — รันบนเครื่องของคุณ
"""

from brain import GrowingBrain
import sys

def main():
    brain = GrowingBrain()

    print("\n" + "="*60)
    print("🤖 Agent พร้อมคุย — พิมพ์ 'quit' เพื่อออก")
    print("   พิมพ์ 'show' เพื่อดูตัวตนปัจจุบัน")
    print("   พิมพ์ 'learn <ชื่อไฟล์>' เพื่ออ่านหนังสือ")
    print("="*60 + "\n")

    brain.show_self()

    while True:
        try:
            user_input = input("\nคุณ: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\nAgent: ลาก่อนครับ 🙏")
            break

        if not user_input:
            continue

        if user_input.lower() == "quit":
            print("\nAgent: ลาก่อนครับ 🙏")
            break

        if user_input.lower() == "show":
            brain.show_self()
            continue

        if user_input.lower().startswith("learn "):
            filename = user_input[6:].strip()
            try:
                content = open(filename, encoding="utf-8").read()
                title = filename.split("/")[-1].replace(".txt", "").replace(".md", "")
                brain.learn_from_book(content, title)
            except FileNotFoundError:
                print(f"ไม่พบไฟล์: {filename}")
            continue

        print("\nAgent: ", end="", flush=True)
        response = brain.speak_as_myself(user_input)
        print(response)


if __name__ == "__main__":
    main()
