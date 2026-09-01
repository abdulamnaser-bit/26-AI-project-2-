import os


# =========================
# CREATE FOLDER
# =========================

def create_folder(folder_name):

    path = os.path.join(
        os.getcwd(),
        folder_name
    )

    os.makedirs(path, exist_ok=True)

    return f'Created folder "{folder_name}", Boss.'

def delete_folder(folder_name):

    import shutil

    try:

        path = os.path.join(
            os.getcwd(),
            folder_name
        )

        shutil.rmtree(path)

        return f'Folder "{folder_name}" deleted, Boss.'

    except Exception as e:

        return f"Error deleting folder: {e}"


def open_folder(folder_name):

    try:

        path = os.path.join(
            os.getcwd(),
            folder_name
        )

        os.startfile(path)

        return f'Opening folder "{folder_name}", Boss.'

    except Exception as e:

        return f"Error opening folder: {e}"


def list_folders():

    try:

        folders = []

        for item in os.listdir(os.getcwd()):

            if os.path.isdir(item):
                folders.append(item)

        if not folders:
            return "No folders found, Boss."

        return "\n".join(folders)

    except Exception as e:

        return f"Error listing folders: {e}"


# =========================
# CREATE FILE
# =========================

BASE_DIR = r"C:\LimraAI"

def create_file(filename):

    print("CREATE FILE CALLED:", filename)

    path = os.path.join(BASE_DIR, filename)

    print("CREATING:", path)

    with open(path, "a", encoding="utf-8"):
        pass
    
    return f'Created file "{filename}", Boss.'



# =========================
# OPEN DOWNLOADS
# =========================

def open_downloads():

    downloads = os.path.join(
        os.path.expanduser("~"),
        "Downloads"
    )

    os.startfile(downloads)

    return "Opening Downloads, Boss."


# =========================
# OPEN DOCUMENTS
# =========================

def open_documents():

    documents = os.path.join(
        os.path.expanduser("~"),
        "Documents"
    )

    os.startfile(documents)

    return "Opening Documents, Boss."