import time
import pyautogui
import os

from app_control import open_app

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

VOICE_ICON = os.path.join(
    BASE_DIR,
    "voice_call.png"
)

VIDEO_ICON = os.path.join(
    BASE_DIR,
    "video_call.png"
)


def whatsapp_call(contact):

    open_app("open whatsapp")

    time.sleep(3)

    pyautogui.hotkey("ctrl", "f")

    time.sleep(1)

    pyautogui.write(contact)

    time.sleep(2)

    pyautogui.press("enter")

    time.sleep(2)

    print("VOICE ICON =", VOICE_ICON)

    button = pyautogui.locateCenterOnScreen(
        VOICE_ICON,
        confidence=0.8
    )

    if button:

        pyautogui.click(button)

        return f"Calling {contact}, Boss."

    return "Voice call button not found, Boss."


def whatsapp_video_call(contact):

    open_app("open whatsapp")

    time.sleep(3)

    pyautogui.hotkey("ctrl", "f")

    time.sleep(1)

    pyautogui.write(contact)

    time.sleep(2)

    pyautogui.press("enter")

    time.sleep(2)

    print("VIDEO ICON =", VIDEO_ICON)

    button = pyautogui.locateCenterOnScreen(
        VIDEO_ICON,
        confidence=0.8
    )

    if button:

        pyautogui.click(button)

        return f"Starting video call with {contact}, Boss."

    return "Video call button not found, Boss."