import os
import subprocess
import tkinter as tk
import sys
from tkinter import messagebox
from config import CONFIG

def finde_scripts():
    scripts = {}
    for rootdir, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith(".py") and not file.startswith("__"):
                rel_path = os.path.relpath(os.path.join(rootdir, file), os.getcwd())
                scripts[rel_path] = os.path.join(rootdir, file)
    return scripts
def run_python_script(script_path):
    if not os.path.exists(script_path):
        return None, None, f"Script nicht gefunden: {script_path}"
    try:
        result = subprocess.run([sys.executable, script_path], check=True, capture_output=True, text=True)
        return result.stdout, result.stderr, None
    except subprocess.CalledProcessError as e:
        return e.stdout, e.stderr, f"Fehler beim Ausführen: {e}"
    except Exception as e:
        return None, None, f"Unerwarteter Fehler: {e}"

        
if __name__ == "__main__":
    # Code hier drunter wird nur ausgeführt wenn das Skript direkt aufgerufen wird
    pass