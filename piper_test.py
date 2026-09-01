from piper.voice import PiperVoice
import wave

voice = PiperVoice.load(
    r"voices\en_US-amy-medium.onnx"
)

with wave.open("output.wav", "wb") as wav_file:

    voice.synthesize_wav(
        "Hello Boss. I am Friday.",
        wav_file
    )

print("Done")