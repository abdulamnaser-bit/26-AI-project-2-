import pyautogui
import os
from datetime import datetime

def take_screenshot():

    folder = r"C:\LimraAI\Screenshots"

    os.makedirs(folder, exist_ok=True)

    filename = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S.png"
    )

    path = os.path.join(folder, filename)

    pyautogui.screenshot(path)

    return path