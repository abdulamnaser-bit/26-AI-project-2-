import subprocess
import os

BASE_DIR = r"C:\LimraAI"

def run_python(filename):

    full_path = os.path.join(
        BASE_DIR,
        filename
    )

    if not os.path.exists(full_path):
        return f"File not found: {filename}"
    
    print("RUNNING FILE:", full_path)

    subprocess.Popen(
        ["py", full_path]
    )

    return f"Running {filename}, Boss."