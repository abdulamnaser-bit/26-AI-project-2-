import os
import subprocess

BASE_DIR = r"C:\LimraAI"


def create_python_project(project_name):

    try:

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

            f.write(
                f"# {project_name}\n"
            )

        return (
            f"Python project "
            f'"{project_name}" created, Boss.'
        )

    except Exception as e:

        return f"Error: {e}"


def open_project(project_name):

    try:

        project_path = os.path.join(
            BASE_DIR,
            project_name
        )

        subprocess.Popen(
            ["code", project_path]
        )

        return (
            f'Opening project "{project_name}", Boss.'
        )

    except Exception as e:

        return f"Error opening project: {e}"