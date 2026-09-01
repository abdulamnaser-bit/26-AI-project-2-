import os
import subprocess
import webbrowser

# =========================
# OPEN APPS
# =========================

def open_app(command):

    command = command.lower().strip()

    # Only process open commands
    if not (
        command.startswith("open ")
        or command.startswith("launch ")
        or command.startswith("start ")
    ):
        return None

    # Remove launch words
    for word in ["open ", "launch ", "start "]:
        if command.startswith(word):
            command = command.replace(word, "", 1).strip()
            break
        
    # Websites
    websites = {
        "youtube": "https://www.youtube.com",
        "chatgpt": "https://chatgpt.com",
        "google": "https://www.google.com",
        "gmail": "https://mail.google.com",
        "instagram": "https://www.instagram.com",
        "facebook": "https://www.facebook.com",
        "github": "https://github.com",
    }

    if command in websites:

        webbrowser.open(websites[command])

        return f"Opening {command.title()}, Boss."

    # Built-in apps
    builtins = {
        "chrome": "start chrome",
        "calculator": "start calc",
        "notepad": "start notepad",
        "calc": "start calc",
        "notepad": "start notepad",
        "paint": "start mspaint",
        "explorer": "start explorer",
        "file explorer": "start explorer",
        "settings": "start ms-settings:",
        "cmd": "start cmd",
        "command prompt": "start cmd",
        "powershell": "start powershell",
        "edge": "start msedge",
        "vs code": r'"C:\Users\Naser\AppData\Local\Programs\Microsoft VS Code\Code.exe"',
        "visual studio code": r'"C:\Users\Naser\AppData\Local\Programs\Microsoft VS Code\Code.exe"',

    }

    if command in builtins:

        subprocess.Popen(builtins[command], shell=True)

        return f"Opening {command.title()}, Boss."

    # Search installed Windows apps
    try:

        ps_command = f'''
    $app = Get-StartApps |
    Where-Object {{$_.Name -like "*{command}*"}} |
    Select-Object -First 1

    if ($app) {{
        Start-Process "shell:AppsFolder\\$($app.AppID)"
    }}
    '''



        result = subprocess.run(
            ["powershell", "-Command", ps_command],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            return f"Opening {command.title()}, Boss."

        return f"I couldn't find {command}, Boss."

    except Exception:
        return None

# =========================
# CLOSE APPS
# =========================

def close_app(command):

    command = command.lower().strip()

    apps = {
        "chrome": "chrome.exe",
        "spotify": "spotify.exe",
        "notepad": "notepad.exe",
        "calculator": "CalculatorApp.exe",
        "calc": "CalculatorApp.exe",
        "whatsapp": "WhatsApp.Root.exe",
        "whats app": "WhatsApp.Root.exe",
        "edge": "msedge.exe",
        "paint": "mspaint.exe",
        "cmd": "cmd.exe",
        "powershell": "powershell.exe",
    }

    for app, process in apps.items():

        if f"close {app}" in command:

            os.system(
                f'taskkill /F /IM "{process}" >nul 2>&1'
            )

            return f"Closing {app.title()}, Boss."

    return None