import speech_recognition as sr
from piper_speaker import speak
import random
import time
import numpy as np
import traceback

from PyQt6.QtWidgets import QApplication

from PyQt6.QtCore import QTimer, QThread, pyqtSignal

import sys

from friday_state import (
    set_status,
    set_audio_level
)

from daily_briefing import get_daily_briefing

from assistant import ask_llm


from friday_ui import FridayUI

class FridayWorker(QThread):

    status_signal = pyqtSignal(str)
    command_signal = pyqtSignal(str, str)

    def run(self):

        recognizer = sr.Recognizer()

        active_mode = False
        briefing_done = False

        while True:

            if not active_mode:

                with sr.Microphone() as source:

                    audio = recognizer.listen(
                        source,
                        timeout=2,
                        phrase_time_limit=2
                    )

                try:
                    text = recognizer.recognize_google(audio).lower()
                except:
                    continue

                print("HEARD:", text)

                if any(word in text for word in WAKE_WORDS):

                    print("WAKE WORD DETECTED")

                    active_mode = True

                    self.status_signal.emit(
                        "Listening..."
                    )

                    if not briefing_done:

                        print("STARTING BRIEFING")

                        briefing = get_daily_briefing()

                        print("BRIEFING =", briefing)

                        speak(briefing)

                        briefing_done = True

                    else:

                        speak("Yes Boss")

app = QApplication(sys.argv)

window = FridayUI()

window.show()

app.processEvents()

window.raise_()
window.activateWindow()

class FridayWorker(QThread):

    status_signal = pyqtSignal(str)
    command_signal = pyqtSignal(str, str)

    def run(self):

        recognizer = sr.Recognizer()

        active_mode = False
        briefing_done = False
        wake_message_shown = False

        while True:

            try:

                # =========================
                # WAKE MODE
                # =========================

                if not active_mode:
                    if not wake_message_shown:
                        print("Waiting for wake word...")
                        wake_message_shown = True

                    with sr.Microphone() as source:

                        audio = recognizer.listen(
                            source,
                            timeout=2,
                            phrase_time_limit=2
                        )

                    try:

                        text = recognizer.recognize_google(audio).lower()

                        print("HEARD:", text)

                    except:
                        continue

                    if any(word in text for word in WAKE_WORDS):

                        print("WAKE WORD DETECTED")

                        active_mode = True

                        wake_message_shown = False
                        command_message_shown = False

                        self.status_signal.emit(
                            "Listening..."
                        )

                        if not briefing_done:

                            briefing = get_daily_briefing()

                            speak(briefing)

                            briefing_done = True

                        else:

                            speak("Yes Boss")

                # =========================
                # ACTIVE MODE
                # =========================

                else:

                    if not command_message_shown:
                        print("Listening for command...")
                        command_message_shown = True


                    with sr.Microphone() as source:

                        audio = recognizer.listen(
                            source,
                            timeout=5,
                            phrase_time_limit=10
                        )

                    try:

                        command = recognizer.recognize_google(audio)

                        print("COMMAND =", command)

                    except:
                        continue

                    cmd = command.lower()

                    # Sleep Commands

                    if cmd in [
                        "sleep",
                        "go to sleep",
                        "sleep friday",
                        "stop listening"
                    ]:

                        active_mode = False

                        wake_message_shown = False
                        command_message_shown = False

                        self.status_signal.emit(
                            "Sleeping..."
                        )

                        speak(
                            "Going to sleep Boss."
                        )

                        continue

                    # Exit Friday

                    if cmd in [
                        "exit",
                        "shutdown",
                        "goodbye friday",
                        "close friday"
                    ]:

                        speak("Goodbye Boss.")

                        QApplication.quit()

                        return

                    # Thinking

                    self.status_signal.emit(
                        "Thinking..."
                    )

                    answer = ask_llm(command)

                    print("FRIDAY:", answer)

                    self.command_signal.emit(
                        command,
                        str(answer)
                    )

                    # Speaking

                    self.status_signal.emit(
                        "Speaking..."
                    )

                    speak(str(answer))

                    self.status_signal.emit(
                        "Listening..."
                    )

            except sr.WaitTimeoutError:

                pass        

            except Exception as e:

                traceback.print_exc()

timer = QTimer()

timer.timeout.connect(lambda: None)

timer.start(16)


BRIEFING_DONE = False

# =========================
# Speech Recognition
# =========================

recognizer = sr.Recognizer()

recognizer.energy_threshold = 300
recognizer.pause_threshold = 1.5
recognizer.phrase_threshold = 0.3
recognizer.non_speaking_duration = 0.5
recognizer.dynamic_energy_threshold = True

# =========================
# Wake Words
# =========================

WAKE_WORDS = [
    "friday",
    "hey friday",
    "hi friday",
    "hello friday"
]

RESPONSES = [
    "Yes Boss?",
    "I'm listening Boss.",
    "How can I help,Boss?",
    "Hey Boss.",
    "Ready when you are,Boss.",
    "What's next,Boss?"
]

# =========================
# Assistant State
# =========================

ACTIVE_MODE = False

set_status("Sleeping...")

# =========================
# Startup
# =========================

print("=================================")
print("        FRIDAY AI")
print("      Say: Friday")
print("=================================")

startup_greetings = [
    "Welcome back,Boss.",
    "Good to see you,Boss.",
    "What are we building today?,Boss.",
    "Hope you're having a good day,Boss.",
    "I'm ready boss.",
]

print("Friday initialized.")

worker = FridayWorker()

worker.status_signal.connect(
    window.update_state
)

worker.command_signal.connect(
    window.update_command_history
)

worker.start()

# =========================
# Main Loop
# =========================

print("PROGRAM STARTED")

sys.exit(app.exec())

