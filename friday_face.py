import tkinter as tk
from friday_state import (
    get_status,
    get_audio_level
)
from emotion_engine import get_emotion

window = tk.Tk()

window.title("FRIDAY")
window.geometry("500x500")
window.configure(bg="black")

title = tk.Label(
    window,
    text="FRIDAY",
    fg="cyan",
    bg="black",
    font=("Arial", 24, "bold")
)
title.pack(pady=20)

canvas = tk.Canvas(
    window,
    width=300,
    height=300,
    bg="black",
    highlightthickness=0
)
canvas.pack()

orb = canvas.create_oval(
    100, 100, 200, 200,
    outline="cyan",
    width=4
)

status_label = tk.Label(
    window,
    text="Sleeping",
    fg="white",
    bg="black",
    font=("Arial", 14)
)
status_label.pack(pady=20)

pulse_size = 0
pulse_direction = 1

def animate():

    global pulse_size
    global pulse_direction

    emotion = get_emotion()
    status = get_status()
    level = get_audio_level()

    print("AUDIO LEVEL =", level)

    status_label.config(
        text=f"Status: {status}"
    )

    # =========================
    # LISTENING
    # =========================

    if status == "Listening":

        canvas.itemconfig(
            orb,
            outline="cyan"
        )

        pulse_size += pulse_direction * 2

        if pulse_size > 20:
            pulse_direction = -1

        if pulse_size < 0:
            pulse_direction = 1

        canvas.coords(
            orb,
            100 - pulse_size,
            100 - pulse_size,
            200 + pulse_size,
            200 + pulse_size
        )

    # =========================
    # THINKING
    # =========================

    elif status == "Thinking":

        canvas.itemconfig(
            orb,
            outline="yellow"
        )

        canvas.coords(
            orb,
            100,
            100,
            200,
            200
        )

    # =========================
    # SPEAKING
    # =========================

    elif status == "Speaking":

        canvas.itemconfig(
            orb,
            outline="lime"
        )

        size = 20 + level

        canvas.coords(
            orb,
            100 - size,
            100 - size,
            200 + size,
            200 + size
        )

    # =========================
    # SLEEPING + EMOTIONS
    # =========================

    else:

        if emotion == "Happy":

            canvas.itemconfig(
                orb,
                outline="cyan"
            )

        elif emotion == "Excited":

            canvas.itemconfig(
                orb,
                outline="lime"
            )

        elif emotion == "Proud":

            canvas.itemconfig(
                orb,
                outline="purple"
            )

        elif emotion == "Relaxed":

            canvas.itemconfig(
                orb,
                outline="blue"
            )

        else:

            canvas.itemconfig(
                orb,
                outline="gray"
            )

        canvas.coords(
            orb,
            100,
            100,
            200,
            200
        )

    window.after(
        50,
        animate
    )
animate()
window.mainloop()