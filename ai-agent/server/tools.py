import os
import subprocess

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def _resolve_path(path):
    full_path = os.path.abspath(os.path.join(BASE_DIR, path))
    if not full_path.startswith(BASE_DIR + os.sep) and full_path != BASE_DIR:
        raise ValueError("Path is outside of the project directory")
    return full_path

def create_file(path, content):
    full_path = _resolve_path(path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(content)
    return f"Created {path}"

def read_file(path):
    with open(_resolve_path(path), "r") as f:
        return f.read()

def delete_file(path):
    os.remove(_resolve_path(path))
    return f"Deleted {path}"

def run_command(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout + result.stderr
