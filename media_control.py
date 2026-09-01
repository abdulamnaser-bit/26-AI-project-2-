import pyautogui

def play_pause():
    pyautogui.press("playpause")
    return "Media toggled, Boss."

def next_track():
    pyautogui.press("nexttrack")
    return "Next track, Boss."

def previous_track():
    pyautogui.press("prevtrack")
    return "Previous track, Boss."