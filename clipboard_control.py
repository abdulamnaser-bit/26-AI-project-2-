import pyperclip

def show_clipboard():

    try:
        return pyperclip.paste()

    except:
        return "Clipboard is empty, Boss."


def clear_clipboard():

    pyperclip.copy("")

    return "Clipboard cleared, Boss."