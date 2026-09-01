import psutil
from datetime import datetime

def battery_status():

    battery = psutil.sensors_battery()

    if battery is None:
        return "Battery information unavailable, Boss."

    return f"Battery is {battery.percent}% , Boss."


def current_time():

    return datetime.now().strftime(
        "Current time is %I:%M %p, Boss."
    )


def current_date():

    return datetime.now().strftime(
        "Today is %d %B %Y, Boss."
    )


def cpu_usage():

    return (
        f"CPU usage is "
        f"{psutil.cpu_percent()} percent, Boss."
    )


def ram_usage():

    memory = psutil.virtual_memory()

    return (
        f"Memory usage is "
        f"{memory.percent} percent, Boss."
    )


def system_status():

    cpu = psutil.cpu_percent()

    ram = psutil.virtual_memory().percent

    return (
        f"CPU usage is {cpu} percent "
        f"and memory usage is "
        f"{ram} percent, Boss."
    )

def disk_usage():

    disk = psutil.disk_usage("C:\\")

    total = round(disk.total / (1024**3), 2)
    used = round(disk.used / (1024**3), 2)
    free = round(disk.free / (1024**3), 2)

    percent = disk.percent

    return (
        f"Boss, storage used is {percent} percent. "
        f"Used {used} GB out of {total} GB. "
        f"Free space remaining is {free} GB."
    )