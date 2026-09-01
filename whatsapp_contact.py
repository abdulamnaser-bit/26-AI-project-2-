import webbrowser
import time
import pyautogui
import pyperclip

from contacts import get_contact

def whatsapp_message(name, message):

    number = get_contact(name)

    if not number:

        return f"I don't know {name}, Boss."

    url = f"https://web.whatsapp.com/send?phone={number}"

    webbrowser.open(url)

    time.sleep(8)

    pyperclip.copy(message)

    pyautogui.hotkey("ctrl", "v")

    time.sleep(1)

    pyautogui.press("enter")

    return f"Message sent to {name}, Boss."