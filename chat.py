import speech_recognition as sr
import pyttsx3

from assistant import ask_llm

engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 180)

recognizer = sr.Recognizer()
recognizer.energy_threshold = 250
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 1.2

print("=================================")
print("      LIMRA VOICE MODE")
print(" Say 'exit' to stop Limra")
print("=================================")

while True:

    try:

        with sr.Microphone() as source:

            print("\nListening...")

            recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=15
            )

        print("Thinking...")

        text = recognizer.recognize_google(audio)

        print(f"\nBoss: {text}")

        if text.lower() == "exit":
            print("Goodbye Boss.")
            break

        answer = ask_llm(text)

        print(f"\nLimra: {answer}")

        engine.say(answer)
        engine.runAndWait()

    except sr.UnknownValueError:

        print("Sorry Boss, I didn't catch that.")

    except Exception as e:

        print("Error:", e) 