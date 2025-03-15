import os
import time
from dotenv import load_dotenv
from twilio.rest import Client  # ✅ Import Twilio Client

# ✅ Load .env file properly
env_path = "/home/sakib951/Documents/auto sms sender/twilio.env"
if not os.path.exists(env_path):
    print(f"❌ ERROR: .env file not found at {env_path}")
else:
    print(f"✅ .env file found at {env_path}")

load_dotenv(env_path)

# ✅ Get Twilio credentials
ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")  
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")  
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")  

# ✅ Debug info
if not ACCOUNT_SID:
    print("❌ ERROR: TWILIO_ACCOUNT_SID is missing!")
if not AUTH_TOKEN:
    print("❌ ERROR: TWILIO_AUTH_TOKEN is missing!")
if not TWILIO_PHONE_NUMBER:
    print("❌ ERROR: TWILIO_PHONE_NUMBER is missing!")

print(f"✅ TWILIO_ACCOUNT_SID: {ACCOUNT_SID}")
print(f"✅ TWILIO_PHONE_NUMBER: {TWILIO_PHONE_NUMBER}")

# 🚀 ASCII Art for Style
ascii_banner = """
███╗   ███╗ █████╗ ███╗   ██╗     ██████╗  ██████╗ ███╗   ███╗██████╗ 
████╗ ████║██╔══██╗████╗  ██║    ██╔═══██╗██╔═══██╗████╗ ████║██╔══██╗
██╔████╔██║███████║██╔██╗ ██║    ██║   ██║██║   ██║██╔████╔██║██████╔╝
██║╚██╔╝██║██╔══██║██║╚██╗██║    ██║   ██║██║   ██║██║╚██╔╝██║██╔═══╝ 
██║ ╚═╝ ██║██║  ██║██║ ╚████║    ╚██████╔╝╚██████╔╝██║ ╚═╝ ██║██║     
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝     ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝     
"""
print("\033[1;92m" + ascii_banner + "\033[0m")  # Green Bold Text

# 📱 Get Receiver's Phone Number
print("\n\033[1;94m[📱] Enter the Receiver's Phone Number (include country code e.g., +966):\033[0m")
TO_PHONE_NUMBER = input("🔹 Phone Number: ")

# 💬 Get the Message
print("\n\033[1;94m[💬] Enter Your Message:\033[0m")
user_message = input("🔹 Message: ")

# ✉️ Function to Send SMS
def send_sms(to_number, message):
    try:
        if not ACCOUNT_SID or not AUTH_TOKEN or not TWILIO_PHONE_NUMBER:
            print("\n\033[1;91m[❌] ERROR: Twilio credentials are missing!\033[0m")
            return

        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        msg = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=to_number
        )
        print("\n\033[1;96m[✔] Message Sent Successfully!\033[0m 🚀")
        print(f"📌 Message SID: \033[1;93m{msg.sid}\033[0m")
    except Exception as e:
        print("\n\033[1;91m[❌] Error Sending SMS:\033[0m", e)

# 📢 Sending the SMS
print("\n\033[1;95m[⚡] Sending Message... Please Wait!\033[0m")
time.sleep(2)
send_sms(TO_PHONE_NUMBER, user_message)

# 🎉 Done
print("\n\033[1;92m[🔥] Task Completed! Stay Awesome!\033[0m 🚀")
