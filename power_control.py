import os

def shutdown_pc():

    os.system("shutdown /s /t 5")

    return "Shutting down in 5 seconds, Boss."


def restart_pc():

    os.system("shutdown /r /t 5")

    return "Restarting in 5 seconds, Boss."


def lock_pc():

    os.system(
        "rundll32.exe user32.dll,LockWorkStation"
    )

    return "Locking computer, Boss."


def sleep_pc():

    os.system(
        "rundll32.exe powrprof.dll,SetSuspendState 0,1,0"
    )

    return "Going to sleep, Boss."