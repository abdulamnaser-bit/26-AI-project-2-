TODO_FILE = "todo.txt"

def add_task(task):

    with open(
        TODO_FILE,
        "a",
        encoding="utf-8"
    ) as f:

        f.write(task + "\n")

    return f"Task added: {task}"


def show_tasks():

    try:

        with open(
            TODO_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            tasks = f.read()

        if tasks.strip():
            return tasks

        return "No tasks available."

    except:
        return "No tasks available."


def remove_task(task):

    try:

        with open(
            TODO_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            lines = f.readlines()

        with open(
            TODO_FILE,
            "w",
            encoding="utf-8"
        ) as f:

            for line in lines:

                if task.lower() not in line.lower():

                    f.write(line)

        return f"Removed task: {task}"

    except:
        return "Task not found."