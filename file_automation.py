import os

BASE_DIR = r"C:\LimraAI"


def create_file(filename):

    try:

        path = os.path.join(BASE_DIR, filename)

        with open(path, "a", encoding="utf-8"):
            pass

        return f'Created file "{filename}", Boss.'

    except Exception as e:

        return f"Error creating file: {e}"


def write_file(filename, content):

    try:

        path = os.path.join(BASE_DIR, filename)

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

        return f'Written to "{filename}", Boss.'

    except Exception as e:

        return f"Error writing file: {e}"


def append_file(filename, content):

    try:

        path = os.path.join(BASE_DIR, filename)

        with open(path, "a", encoding="utf-8") as f:
            f.write("\n" + content)

        return f'Added content to "{filename}", Boss.'

    except Exception as e:

        return f"Error appending file: {e}"
    

def read_file(filename):

    try:

        path = os.path.join(BASE_DIR, filename)

        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    except Exception as e:

        return f"Error reading file: {e}"


def delete_file(filename):

    try:

        path = os.path.join(BASE_DIR, filename)

        os.remove(path)

        return f'Deleted "{filename}", Boss.'

    except Exception as e:

        return f"Error deleting file: {e}"


def open_file(filename):

    try:

        path = os.path.join(BASE_DIR, filename)

        os.startfile(path)

        return f'Opening "{filename}", Boss.'

    except Exception as e:

        return f"Error opening file: {e}"


def list_files():

    try:

        files = os.listdir(BASE_DIR)

        if not files:
            return "No files found, Boss."

        return "\n".join(files)

    except Exception as e:

        return f"Error listing files: {e}"