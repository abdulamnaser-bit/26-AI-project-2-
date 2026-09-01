from memory import (
    load_memory,
    save_memory
)

def set_goal(goal):

    memory = load_memory()

    memory["goal"] = goal

    save_memory(memory)

    return f"Goal set: {goal}"


def get_goal():

    memory = load_memory()

    return memory.get("goal", None)


def clear_goal():

    memory = load_memory()

    if "goal" in memory:
        del memory["goal"]

    save_memory(memory)

    return "Goal cleared."