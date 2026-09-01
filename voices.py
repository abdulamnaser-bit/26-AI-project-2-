import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

for voice in speaker.GetVoices():

    if "zira" in voice.GetDescription().lower():

        speaker.Voice = voice

        print("USING:", voice.GetDescription())

        break
    