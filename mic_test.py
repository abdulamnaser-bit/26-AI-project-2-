import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening...")
    recognizer.adjust_for_ambient_noise(source, duration=1)

    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)

    print("You said:", text)

except Exception as e:
    print("Error:", e)