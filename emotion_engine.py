EMOTION_FILE = "friday_emotion.txt"


def set_emotion(emotion):

    print("SETTING EMOTION =", emotion)

    with open(
        EMOTION_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(emotion)

def get_emotion():

    try:

        with open(
            EMOTION_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            return f.read().strip()

    except:

        return "Neutral"