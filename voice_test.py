import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty("voices")

for i, voice in enumerate(voices):
    print(i, voice.name)

engine.setProperty("voice", voices[1].id)

engine.setProperty("rate", 180)

print("Speaking now...")

engine.say("Hello Boss. This is Friday speaking.")

engine.runAndWait()

print("Finished.")