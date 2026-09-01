import os
import datetime

def system_command(command):

    command = command.lower()

    if "what time is it" in command:

        current_time = datetime.datetime.now().strftime(
            "%I:%M %p"
        )

        return f"The time is {current_time}, Boss."

    if "shutdown computer" in command:

        os.system("shutdown /s /t 10")

        return "Shutting down the computer in 10 seconds, Boss."

    if "restart computer" in command:

        os.system("shutdown /r /t 10")

        return "Restarting the computer in 10 seconds, Boss."

    if "cancel shutdown" in command:

        os.system("shutdown /a")

        return "Shutdown cancelled, Boss."

    return None