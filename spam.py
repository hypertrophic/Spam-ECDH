from instagrapi import Client
import time

USERNAME = "Username Dyalk"
PASSWORD = "Password Dyalk"

MESSAGE = """السلام عليكم
كنتمنى تكونو بخير.

حنا مجموعة شباب من مختلف التخصصات، أعضاء ومتطوعين فجمعية فضاء المواطنة للتنمية البشرية (ECDH)، وكنوجدو دابا للنسخة الثامنة من القافلة الإنسانية، وهو مشروع سنوي كنمشيو فيه لدوار بعيد, كنصلحو المدرسة ليفظروف قاسية، كنوفروا قافلة طبية مجانية لساكنة المنطقة، وكننظمو ورشات للصغار فيها ألعاب وتوجيه دراسي.
المبادرة مبنية على التضامن، ومشاركة بسيطة منك (فستوري ولا بوست) تقدر توصل الرسالة لناس اللي يقدرو يعاونو.
إلى كنت/ي مهتم/ة، نبعثو ليك التفاصيل أكثر على المشروع مرحبا،
شكرا بزاف على وقتك 💚
https://www.instagram.com/p/DMV5um8sVkP/?igsh=MW9rajlnOWVseHY0dg==
"""


def save_to_sent(username):
    with open('sent.txt', 'a', encoding='utf-8') as f:
        f.write(username + '\n')


def load_sent_accounts():
    try:
        with open('sent.txt', encoding='utf-8') as f:
            return set(line.strip() for line in f if line.strip())
    except FileNotFoundError:
        return set()


def main():
    with open('accounts.txt', encoding="utf-8") as account:
        accounts_list = [line.strip() for line in account if line.strip()]

    sent_accounts = load_sent_accounts()

    cl = Client()
    try:
        cl.login(USERNAME, PASSWORD)
        print("[✓] Login successful!")
    except Exception as e:
        print(f"[X] Login failed: {e}")
        return

    for username in accounts_list:
        if username in sent_accounts:
            print(f"[-] Already messaged: {username}")
            continue

        try:
            user_id = cl.user_id_from_username(username)
            cl.direct_send(MESSAGE, [user_id])
            print(f"[✓] Message sent to: {username}")
            save_to_sent(username)
            time.sleep(3)  # Fixed delay to avoid spam detection
        except Exception as e:
            print(f"[X] Failed to message {username}: {e}")


if __name__ == "__main__":
    main()
