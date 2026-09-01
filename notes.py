NOTES_FILE = "notes.txt"

def save_note(note):

    with open(
        NOTES_FILE,
        "a",
        encoding="utf-8"
    ) as f:

        f.write(note + "\n")

    return "Note saved, Boss."


def read_notes():

    try:

        with open(
            NOTES_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            return f.read()

    except:
        return "No notes found, Boss."