from piper.voice import PiperVoice
from playsound import playsound
import wave
import uuid

voice = PiperVoice.load(
    r"voices\en_US-amy-medium.onnx"
)

def speak(text):

    filename = f"voice_{uuid.uuid4().hex}.wav"

    with wave.open(filename, "wb") as wav_file:

        voice.synthesize_wav(
            text,
            wav_file
        )

    playsound(filename)