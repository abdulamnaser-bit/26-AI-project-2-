from memory import load_memory, save_memory

def save_session_note(text):

    memory = load_memory()

    if "session_notes" not in memory:
        memory["session_notes"] = []

    memory["session_notes"].append(text)

    memory["session_notes"] = memory["session_notes"][-20:]

    save_memory(memory)


def get_session_notes():

    memory = load_memory()

    return memory.get(
        "session_notes",
        []
    )