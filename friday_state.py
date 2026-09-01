STATE_FILE = "friday_state.txt"
AUDIO_FILE = "friday_audio.txt"


def set_status(status):

    with open(
        STATE_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(status)


def get_status():

    try:

        with open(
            STATE_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            return f.read().strip()

    except:

        return "Sleeping"


def set_audio_level(level):

    with open(
        AUDIO_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(str(level))


def get_audio_level():

    try:

        with open(
            AUDIO_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            return int(f.read().strip())

    except:

        return 0
    