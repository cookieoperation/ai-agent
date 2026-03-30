import os
import subprocess

BASE_DIR = "/workspaces/ai-agent"

def create_file(path, content):
    full_path = os.path.join(BASE_DIR, path)
    with open(full_path, "w") as f:
        f.write(content)
    return f"Created {path}"

def read_file(path):
    with open(os.path.join(BASE_DIR, path), "r") as f:
        return f.read()

def delete_file(path):
    os.remove(os.path.join(BASE_DIR, path))
    return f"Deleted {path}"

def run_command(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout + result.stderr