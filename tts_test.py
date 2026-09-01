import pyttsx3

engine = pyttsx3.init()

engine.setProperty("voice",
                   engine.getProperty("voices")[1].id)

engine.say("Hello Boss")
engine.runAndWait()

print("Speech finished")