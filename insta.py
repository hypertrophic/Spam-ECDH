from instagrapi import Client

# Instagram login credentials
USERNAME = "----------USER DYALK--------"  # <-- Use your Instagram username, not your email!
PASSWORD = "----------PASSWORD ---------"

# List of Instagram usernames you want to message
accounts = ["ismail_enniou", "malak.en0"]

# The message you want to send
message = """السلام عليكم
كنتمنى تكونو بخير.

حنا مجموعة شباب من مختلف التخصصات، أعضاء ومتطوعين فجمعية فضاء المواطنة للتنمية البشرية (ECDH)، وكنوجدو دابا للنسخة الثامنة من القافلة الإنسانية، وهو مشروع سنوي كنمشيو فيه لدوار بعيد, كنصلحو المدرسة ليفظروف قاسية، كنوفروا قافلة طبية مجانية لساكنة المنطقة، وكننظمو ورشات للصغار فيها ألعاب وتوجيه دراسي.
المبادرة مبنية على التضامن، ومشاركة بسيطة منك (فستوري ولا بوست) تقدر توصل الرسالة لناس اللي يقدرو يعاونو.
إلى كنت/ي مهتم/ة، نبعثو ليك التفاصيل أكثر على المشروع مرحبا،
شكرا بزاف على وقتك 💚
https://www.instagram.com/p/DMV5um8sVkP/?igsh=MW9rajlnOWVseHY0dg==
"""

def main():
    cl = Client()
    try:
        cl.login(USERNAME, PASSWORD)
        print("Login successful!")
    except Exception as e:
        print(f"Failed to login: {e}")
        return

    for account in accounts:
        try:
            user_id = cl.user_id_from_username(account)
            cl.direct_send(message, [user_id])
            print(f"Message sent to {account}")
        except Exception as e:
            print(f"Failed to send message to {account}: {e}")

if __name__ == "__main__":
    main()