import os
import subprocess

BASE_DIR = r"C:\LimraAI"

def create_python_project(project_name):

    project_path = os.path.join(
        BASE_DIR,
        project_name
    )

    os.makedirs(
        project_path,
        exist_ok=True
    )

    open(
        os.path.join(project_path, "main.py"),
        "w"
    ).close()

    open(
        os.path.join(project_path, "requirements.txt"),
        "w"
    ).close()

    with open(
        os.path.join(project_path, "README.md"),
        "w",
        encoding="utf-8"
    ) as f:

        f.write(f"# {project_name}")

    try:

        subprocess.Popen(
            ["code", project_path]
        )

    except:
        pass

    return (
        f'Python project "{project_name}" '
        f'created and opened in VS Code, Boss.'
    )