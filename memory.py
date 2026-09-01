import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEMORY_FILE = os.path.join(BASE_DIR, "memory.json")

# ==================================
# RAM CACHE
# ==================================

_memory_cache = None


def load_memory():

    global _memory_cache

    if _memory_cache is not None:
        return _memory_cache

    if not os.path.exists(MEMORY_FILE):
        _memory_cache = {}
        return _memory_cache

    with open(MEMORY_FILE, "r") as f:
        _memory_cache = json.load(f)

    print("MEMORY LOADED")

    return _memory_cache


def save_memory(memory):

    global _memory_cache

    _memory_cache = memory

    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)


def remember(key, value):

    memory = load_memory()

    memory[key.lower()] = value

    save_memory(memory)

    return f"I'll remember that your {key} is {value}, Boss."


def recall(key):

    memory = load_memory()

    return memory.get(
        key.lower(),
        None
    )


def clear_memory_cache():

    global _memory_cache

    _memory_cache = None