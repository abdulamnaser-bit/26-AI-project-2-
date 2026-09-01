"""
FRIDAY CORE FOR 26 BATMAN HUD

26 = visual interface
FRIDAY = voice + commands + application control
Piper Amy = Friday's voice
"""

import os
import re
import subprocess
import threading
import time
import wave
import webbrowser
from datetime import datetime

import speech_recognition as sr

from piper import PiperVoice
from faster_whisper import WhisperModel

print("[FRIDAY] Loading Faster-Whisper...")
_whisper_model = WhisperModel(
    "base.en",
    device="cpu",
    compute_type="int8"
)
print("[FRIDAY] Faster-Whisper ready.")


# ============================================================
# PATHS
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

VOICE_MODEL = os.path.join(
    BASE_DIR,
    "voices",
    "en_US-amy-medium.onnx"
)


# ============================================================
# PIPER VOICE
# ============================================================

print(
    f"[FRIDAY] Loading Piper voice: {VOICE_MODEL}"
)

try:

    piper_voice = PiperVoice.load(
        VOICE_MODEL
    )

    print(
        "[FRIDAY] Piper Amy voice loaded."
    )

except Exception as error:

    piper_voice = None

    print(
        "[FRIDAY] Piper voice error:",
        error
    )


_speak_lock = threading.Lock()


def speak(text):

    """
    Speak using the custom Piper Amy voice.
    """

    print(
        f"FRIDAY: {text}"
    )

    if piper_voice is None:

        print(
            "[FRIDAY] Voice unavailable."
        )

        return


    output_file = os.path.join(
        BASE_DIR,
        "_friday_voice.wav"
    )


    with _speak_lock:

        try:

            # Piper generates raw audio into a WAV file.
            with wave.open(
                output_file,
                "wb"
            ) as wav_file:

                piper_voice.synthesize_wav(
                    text,
                    wav_file
                )


            # Use Windows' built-in audio player.
            #
            # This does NOT change the voice.
            # Piper already generated the Amy voice.
            #
            # The WAV is simply played.

            import winsound

            winsound.PlaySound(
                output_file,
                winsound.SND_FILENAME
            )

        except Exception as error:

            print(
                "[FRIDAY] TTS error:",
                error
            )

        finally:
            # The WAV is only a temporary playback buffer.
            # Remove it so C:\LimraAI does not fill with generated audio files.
            try:
                if os.path.exists(output_file):
                    os.remove(output_file)
            except Exception as cleanup_error:
                print(
                    "[FRIDAY] Could not remove temporary voice WAV:",
                    cleanup_error
                )


def speak_async(text):

    threading.Thread(
        target=speak,
        args=(text,),
        daemon=True
    ).start()


# ============================================================
# WAKE PHRASES
# ============================================================

WAKE_PHRASES = [

    "hey friday",

    "hi friday",

    "hello friday",

    "ok friday",

    "okay friday",

    "wake up friday",

    "friday",

]


# ============================================================
# WINDOWS APPLICATION DISCOVERY
# ============================================================

def get_windows_apps():

    """
    Ask Windows for registered Start Menu applications.

    This is designed to handle:

        WhatsApp
        Spotify
        Discord
        Telegram
        Microsoft Store apps
        MSIX applications
        normal installed applications
    """

    apps = {}


    powershell_script = r"""
Get-StartApps | ForEach-Object {
    "$($_.Name)||$($_.AppID)"
}
"""


    try:

        result = subprocess.run(

            [
                "powershell.exe",

                "-NoProfile",

                "-ExecutionPolicy",
                "Bypass",

                "-Command",
                powershell_script
            ],

            capture_output=True,

            text=True,

            timeout=10
        )


        for line in result.stdout.splitlines():

            if "||" not in line:

                continue


            name, app_id = line.split(
                "||",
                1
            )


            name = name.strip()

            app_id = app_id.strip()


            if name and app_id:

                apps[
                    name.lower()
                ] = (
                    name,
                    app_id
                )


    except Exception as error:

        print(
            "[FRIDAY] App discovery error:",
            error
        )


    return apps


def find_windows_app(
    requested_name
):

    requested = (
        requested_name
        .lower()
        .strip()
    )


    apps = get_windows_apps()


    # Exact match

    if requested in apps:

        return apps[
            requested
        ]


    # Partial match

    for app_name, app_data in apps.items():

        if requested in app_name:

            return app_data


    return None


def launch_windows_app(
    name
):

    result = find_windows_app(
        name
    )


    if not result:

        print(
            f"[FRIDAY] App not found: {name}"
        )

        return False


    display_name, app_id = result


    print(
        f"[FRIDAY] Launching: {display_name}"
    )

    print(
        f"[FRIDAY] AppID: {app_id}"
    )


    try:

        command = (
            "explorer.exe "
            f"shell:AppsFolder\\{app_id}"
        )


        subprocess.Popen(
            command,
            shell=True
        )


        return True


    except Exception as error:

        print(
            "[FRIDAY] App launch error:",
            error
        )

        return False


# ============================================================
# APPLICATION LAUNCHER
# ============================================================

def launch_application(
    name
):

    name = (
        name
        .strip()
        .lower()
    )


    print(
        f"[FRIDAY] Requested app: {name}"
    )


    # --------------------------------------------------------
    # WEBSITES
    # --------------------------------------------------------

    websites = {

        "google":
            "https://www.google.com",

        "youtube":
            "https://www.youtube.com",

        "gmail":
            "https://mail.google.com",

    }


    if name in websites:

        webbrowser.open(
            websites[name]
        )

        return True


    # --------------------------------------------------------
    # NORMAL WINDOWS PROGRAMS
    # --------------------------------------------------------

    commands = {

        "chrome":
            "chrome",

        "google chrome":
            "chrome",

        "edge":
            "msedge",

        "microsoft edge":
            "msedge",

        "notepad":
            "notepad",

        "calculator":
            "calc",

        "paint":
            "mspaint",

        "terminal":
            "wt",

        "windows terminal":
            "wt",

        "command prompt":
            "cmd",

        "cmd":
            "cmd",

        "file explorer":
            "explorer",

        "explorer":
            "explorer",

        "vs code":
            "code",

        "vscode":
            "code",

        "visual studio code":
            "code",

    }


    if name in commands:

        try:

            subprocess.Popen(
                commands[name],
                shell=True
            )

            return True

        except Exception as error:

            print(
                "[FRIDAY] Command launch error:",
                error
            )


    # --------------------------------------------------------
    # WINDOWS REGISTERED APPS
    # --------------------------------------------------------

    if launch_windows_app(
        name
    ):

        return True


    # --------------------------------------------------------
    # FALLBACK
    # --------------------------------------------------------

    try:

        subprocess.Popen(
            f'start "" "{name}"',
            shell=True
        )

        return True

    except Exception as error:

        print(
            "[FRIDAY] Application error:",
            error
        )

        return False


# ============================================================
# COMMAND HANDLER
# ============================================================

def handle_command(
    command
):

    command = command.strip()


    if not command:

        return None


    lower = command.lower()


    # --------------------------------------------------------
    # OPEN APPLICATION
    # --------------------------------------------------------

    match = re.match(

        r"^(open|launch|start)\s+(.+)$",

        command,

        re.IGNORECASE
    )


    if match:

        app_name = match.group(
            2
        ).strip()


        success = launch_application(
            app_name
        )


        if success:

            speak_async(
                f"Opening {app_name}, Boss."
            )

        else:

            speak_async(
                f"I couldn't find {app_name}, Boss."
            )


        return None


    # --------------------------------------------------------
    # SEARCH
    # --------------------------------------------------------

    if lower.startswith(
        "search "
    ):

        query = command[
            7:
        ].strip()


        if query:

            speak_async(
                f"Searching for {query}, Boss."
            )


            url = (

                "https://www.google.com/search?q="

                + query.replace(
                    " ",
                    "+"
                )

            )


            webbrowser.open(
                url
            )


        return None


    # --------------------------------------------------------
    # PLAY YOUTUBE
    # --------------------------------------------------------

    if lower.startswith(
        "play "
    ):

        query = command[
            5:
        ].strip()


        if query:

            speak_async(
                f"Playing {query}, Boss."
            )


            url = (

                "https://www.youtube.com/results?search_query="

                + query.replace(
                    " ",
                    "+"
                )

            )


            webbrowser.open(
                url
            )


        return None


    # --------------------------------------------------------
    # TIME
    # --------------------------------------------------------

    if "time" in lower:

        current_time = datetime.now().strftime(
            "%I:%M %p"
        )


        speak_async(
            f"It is {current_time}, Boss."
        )


        return None


    # --------------------------------------------------------
    # DOWNLOADS
    # --------------------------------------------------------

    if lower in [

        "open downloads",

        "open download folder",

    ]:

        path = os.path.join(

            os.path.expanduser("~"),

            "Downloads"

        )


        os.startfile(
            path
        )


        speak_async(
            "Opening Downloads, Boss."
        )


        return None


    # --------------------------------------------------------
    # DOCUMENTS
    # --------------------------------------------------------

    if lower in [

        "open documents",

        "open documents folder",

    ]:

        path = os.path.join(

            os.path.expanduser("~"),

            "Documents"

        )


        os.startfile(
            path
        )


        speak_async(
            "Opening Documents, Boss."
        )


        return None


    # --------------------------------------------------------
    # LOCK
    # --------------------------------------------------------

    if lower in [

        "lock computer",

        "lock pc",

        "lock the computer",

    ]:

        speak_async(
            "Locking the computer, Boss."
        )


        time.sleep(
            0.5
        )


        subprocess.Popen(

            "rundll32.exe user32.dll,LockWorkStation",

            shell=True
        )


        return None


    # --------------------------------------------------------
    # STANDBY
    # --------------------------------------------------------

    if lower in [

        "sleep",

        "go to sleep",

        "stand by",

        "standby",

    ]:

        speak_async(
            "Going to standby, Boss."
        )


        return "sleep"


    # --------------------------------------------------------
    # UNKNOWN COMMAND
    # --------------------------------------------------------

    speak_async(

        "I heard you, Boss, "
        "but I don't have that command yet."

    )


    return None


# ============================================================
# FRIDAY VOICE ENGINE
# ============================================================

class FridayVoice:

    def __init__(
        self,
        on_state_change=None,
        on_command=None,
    ):

        self.on_state_change = (
            on_state_change
        )

        self.on_command = (
            on_command
        )

        self.running = False

        self.thread = None


    # --------------------------------------------------------
    # STATE
    # --------------------------------------------------------

    def state(
        self,
        value
    ):

        print(
            f"[FRIDAY] {value}"
        )


        if self.on_state_change:

            try:

                self.on_state_change(
                    value
                )

            except Exception as error:

                print(
                    "[FRIDAY] UI callback error:",
                    error
                )


    # --------------------------------------------------------
    # START
    # --------------------------------------------------------

    def start(
        self
    ):

        if self.running:

            return


        self.running = True


        self.thread = threading.Thread(

            target=self.listen_loop,

            daemon=True

        )


        self.thread.start()


    # --------------------------------------------------------
    # STOP
    # --------------------------------------------------------

    def stop(
        self
    ):

        self.running = False

    def recognize(self, audio):
        """
        Convert captured microphone audio into text using
        local Faster-Whisper.
        """

        diagnostic_file = os.path.join(
            BASE_DIR,
            "_friday_last_command.wav"
        )

        try:
            with wave.open(diagnostic_file, "wb") as wav_file:
                wav_file.setnchannels(1)
                wav_file.setsampwidth(audio.sample_width)
                wav_file.setframerate(audio.sample_rate)
                wav_file.writeframes(
                    audio.get_raw_data()
                )

            print(
                f"[FRIDAY] Saved command audio: "
                f"{diagnostic_file}"
            )

        except Exception as error:
            print(
                "[FRIDAY] Audio save error:",
                repr(error)
            )
            return ""

        try:
            print(
                "[FRIDAY] Whisper transcription..."
            )

            segments, info = _whisper_model.transcribe(
                diagnostic_file,
                language="en",
                beam_size=5,
                vad_filter=True
            )

            text = " ".join(
                segment.text.strip()
                for segment in segments
                if segment.text.strip()
            )

            text = text.lower().strip()

            if text:
                print(
                    f"[FRIDAY] HEARD (Whisper): {text}"
                )
                return text

            print(
                "[FRIDAY] Whisper returned no speech."
            )
            return ""

        except Exception as error:
            print(
                "[FRIDAY] Whisper recognition error:",
                repr(error)
            )
            return ""


    # --------------------------------------------------------
    # MICROPHONE LOOP
    # --------------------------------------------------------

    def listen_loop(
        self
    ):

        recognizer = sr.Recognizer()


        recognizer.energy_threshold = 300

        recognizer.dynamic_energy_threshold = True

        recognizer.pause_threshold = 0.6

        recognizer.non_speaking_duration = 0.3


        # ----------------------------------------------------
        # MICROPHONE
        # ----------------------------------------------------

        try:

            # Device 1 was verified by the standalone microphone test.
            # Keep it as the primary device instead of matching a fragile
            # device-name string. If Windows changes the index, choose the
            # first device that actually exposes an input channel.
            MIC_DEVICE_INDEX = 1

            try:
                microphone = sr.Microphone(device_index=MIC_DEVICE_INDEX)
                print("[FRIDAY] Using microphone device 1")
            except Exception:
                print("[FRIDAY] Device 1 unavailable; searching for an input device...")
                microphone = None
                for idx, info in enumerate(sr.Microphone.list_microphone_names()):
                    try:
                        candidate = sr.Microphone(device_index=idx)
                        microphone = candidate
                        MIC_DEVICE_INDEX = idx
                        print(f"[FRIDAY] Using fallback microphone device {idx}: {info}")
                        break
                    except Exception:
                        continue
                if microphone is None:
                    raise RuntimeError("No usable microphone device found")
            
        except Exception as error:

            print(
                "[FRIDAY] Microphone error:",
                error
            )

            self.state(
                "MIC ERROR"
            )

            return


        # ----------------------------------------------------
        # CALIBRATION
        # ----------------------------------------------------

        try:

            with microphone as source:

                self.state(
                    "CALIBRATING"
                )


                recognizer.adjust_for_ambient_noise(

                    source,

                    duration=1

                )


        except Exception as error:

            print(
                "[FRIDAY] Calibration error:",
                error
            )

            self.state(
                "MIC ERROR"
            )

            return


        self.state(
            "STANDBY"
        )


        session_active = False


        # ====================================================
        # MAIN LOOP
        # ====================================================

        while self.running:

            try:

                if session_active:

                    self.state(
                        "LISTENING"
                    )

                else:

                    self.state(
                        "STANDBY"
                    )


                with microphone as source:

                    audio = recognizer.listen(

                        source,

                        timeout=None,

                        phrase_time_limit=8

                    )


            except Exception as error:

                print(
                    "[FRIDAY] Listening error:",
                    error
                )

                continue

            # =================================================
            # WAKE WORD + OPTIONAL INLINE COMMAND
            # =================================================

            if not session_active:

                wake_phrase = None

                for phrase in sorted(WAKE_PHRASES, key=len, reverse=True):
                    if phrase in heard:
                        wake_phrase = phrase
                        break

                if wake_phrase:
                    session_active = True
                    self.state("AWAKE")

                    # Example:
                    #   "hey friday"
                    #   "hey friday open whatsapp"
                    # The old code discarded the second form because it
                    # always continued after detecting the wake phrase.
                    inline_command = heard.replace(wake_phrase, "", 1).strip()

                    if inline_command:
                        heard = inline_command
                        print(
                            f"[FRIDAY] INLINE COMMAND: {heard}"
                        )
                    else:
                        speak_async("Yes Boss.")
                        continue


            # =================================================
            # REMOVE WAKE PHRASE
            # =================================================

            for phrase in WAKE_PHRASES:

                if heard.startswith(
                    phrase
                ):

                    heard = heard[
                        len(phrase):
                    ].strip()

                    break


            if not heard:

                continue


            # =================================================
            # COMMAND
            # =================================================

            self.state(
                "THINKING"
            )


            if self.on_command:

                try:

                    self.on_command(
                        heard
                    )

                except Exception as error:

                    print(
                        "[FRIDAY] Command callback error:",
                        error
                    )


            result = handle_command(
                heard
            )


            if result == "sleep":

                session_active = False

                self.state(
                    "STANDBY"
                )

            else:

                self.state(
                    "LISTENING"
                )
