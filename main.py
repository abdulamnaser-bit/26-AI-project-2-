from assistant import ask_llm
import pyttsx3

engine = pyttsx3.init()

# Speech settings
engine.setProperty("rate", 180)

# Select female voice if available
voices = engine.getProperty("voices")

engine.setProperty("voice", voices[1].id)

print("Limra AI Started")
print("Type 'exit' to quit\n")

while True:

    text = input("You: ")

    if text.lower() == "exit":
        break

    try:

        answer = ask_llm(text)

        print("\nLimra:", answer)
        print()

        engine.say(answer)
        engine.runAndWait()

    except Exception as e:
        print("Error:", e)