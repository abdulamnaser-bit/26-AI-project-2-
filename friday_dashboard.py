import tkinter as tk
import psutil
import time

from friday_status import (
    STATUS,
    LAST_COMMAND,
    LAST_RESPONSE
)
import friday_status

window = tk.Tk()

window.title("FRIDAY AI")
window.geometry("400x250")

title = tk.Label(
    window,
    text="FRIDAY",
    font=("Arial", 22, "bold")
)

title.pack(pady=10)

time_label = tk.Label(window, font=("Arial", 12))
time_label.pack()

cpu_label = tk.Label(window, font=("Arial", 12))
cpu_label.pack()

ram_label = tk.Label(window, font=("Arial", 12))
ram_label.pack()

status_label = tk.Label(
    window,
    text="Status: Sleeping",
    font=("Arial", 12)
)

status_label.pack(pady=5)

command_label = tk.Label(
    window,
    text="Last Command:",
    wraplength=350
)

command_label.pack()

response_label = tk.Label(
    window,
    text="Last Response:",
    wraplength=350
)

response_label.pack()

def update_dashboard():

    current_time = time.strftime("%I:%M:%S %p")

    cpu = psutil.cpu_percent()

    ram = psutil.virtual_memory().percent

    time_label.config(
        text=f"Time: {current_time}"
    )

    cpu_label.config(
        text=f"CPU Usage: {cpu}%"
    )

    ram_label.config(
        text=f"RAM Usage: {ram}%"
    )

    status_label.config(
        text=f"Status: {friday_status.STATUS}"
    )

    command_label.config(
        text=f"Last Command:\n{friday_status.LAST_COMMAND}"
    )

    response_label.config(
        text=f"Last Response:\n{friday_status.LAST_RESPONSE}"
    )

    window.after(1000, update_dashboard)

    update_dashboard()

    window.mainloop()