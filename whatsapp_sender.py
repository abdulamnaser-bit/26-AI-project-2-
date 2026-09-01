import pyautogui
import pyperclip
import time

def send_whatsapp_message(contact, message):

    try:

        # Open WhatsApp
        pyautogui.press("win")
        time.sleep(1)

        pyautogui.write("WhatsApp", interval=0.05)
        time.sleep(1)

        pyautogui.press("enter")
        time.sleep(5)

        # Search contact
        pyautogui.hotkey("ctrl", "f")
        time.sleep(1)

        pyperclip.copy(contact)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(2)

        pyautogui.press("enter")
        time.sleep(2)

        # Type message
        pyperclip.copy(message)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(1)

        pyautogui.press("enter")

        return f"Message sent to {contact}, Boss."

    except Exception as e:

        print("WHATSAPP ERROR:", e)

        return "Failed to send WhatsApp message, Boss."