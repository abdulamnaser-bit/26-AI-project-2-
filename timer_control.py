import threading
import time

def start_timer(minutes):

    def timer_thread():

        time.sleep(minutes * 60)

        print("\n⏰ TIMER FINISHED!")

    threading.Thread(
        target=timer_thread,
        daemon=True
    ).start()

    return f"Timer started for {minutes} minutes, Boss."