import shutil
from config import CONFIG
def copy_template(src, dst, replacements=None):
    with open(src, "r", encoding="utf-8") as f:
        content = f.read()
    if replacements:
        for key, value in replacements.items():
            content = content.replace(key, value)
    with open(dst, "w", encoding="utf-8") as f:
        f.write(content)

        
        
if __name__ == "__main__":
# Code hier drunter wird nur ausgeführt wenn das Skript direkt aufgerufen wird