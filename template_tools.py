import shutil

def copy_template(src, dst, replacements=None):
    with open(src, "r", encoding="utf-8") as f:
        content = f.read()
    if replacements:
        for key, value in replacements.items():
            content = content.replace(key, value)
    with open(dst, "w", encoding="utf-8") as f:
        f.write(content)