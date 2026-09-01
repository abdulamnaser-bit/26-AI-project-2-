from memory import load_memory, save_memory

def add_achievement(text):

    memory = load_memory()

    if "achievements" not in memory:
        memory["achievements"] = []

    memory["achievements"].append(text)

    save_memory(memory)


def get_achievements():

    memory = load_memory()

    return memory.get(
        "achievements",
        []
    )