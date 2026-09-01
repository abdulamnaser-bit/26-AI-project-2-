import os

def volume_up():

    for _ in range(10):
        os.system(
            'powershell -command "(New-Object -ComObject WScript.Shell).SendKeys([char]175)"'
        )

    return "Volume increased, Boss."


def volume_down():

    for _ in range(10):
        os.system(
            'powershell -command "(New-Object -ComObject WScript.Shell).SendKeys([char]174)"'
        )

    return "Volume decreased, Boss."


def mute():

    os.system(
        'powershell -command "(New-Object -ComObject WScript.Shell).SendKeys([char]173)"'
    )

    return "Muted, Boss."


def unmute():

    os.system(
        'powershell -command "(New-Object -ComObject WScript.Shell).SendKeys([char]173)"'
    )

    return "Unmuted, Boss."
