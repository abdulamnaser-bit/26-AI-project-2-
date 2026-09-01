import threading
import time

def set_reminder(text, minutes):

    def reminder_thread():

        time.sleep(minutes * 60)

        print(f"\n🔔 REMINDER: {text}")

    threading.Thread(
        target=reminder_thread,
        daemon=True
    ).start()

    return f"Reminder set for {minutes} minutes, Boss."