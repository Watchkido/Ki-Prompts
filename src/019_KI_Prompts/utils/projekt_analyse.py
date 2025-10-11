import os
import re
import subprocess
from collections import defaultdict
from config import CONFIG
# -------------------------------------------
# 🔎 Datei- & Import-Analyse (wie oben)
# -------------------------------------------

def finde_python_dateien(root):
    py_files = []
    for ordner, _, dateien in os.walk(root):
        for datei in dateien:
            if datei.endswith(".py"):
                pfad = os.path.join(ordner, datei)
                py_files.append(os.path.normpath(pfad))
    return py_files

def extrahiere_imports(dateipfad):
    imports = set()
    with open(dateipfad, "r", encoding="utf-8", errors="ignore") as f:
        for zeile in f:
            match_import = re.match(r'^\s*import\s+([\w\.]+)', zeile)
            match_from = re.match(r'^\s*from\s+([\w\.]+)', zeile)
            if match_import:
                imports.add(match_import.group(1).split('.')[0])
            elif match_from:
                imports.add(match_from.group(1).split('.')[0])
    return imports

def analysiere_imports(py_dateien):
    modulnamen_to_dateien = {os.path.splitext(os.path.basename(f))[0]: f for f in py_dateien}
    verwendete_module = set()
    verwendet_von = defaultdict(list)

    for datei in py_dateien:
        imports = extrahiere_imports(datei)
        for imp in imports:
            if imp in modulnamen_to_dateien:
                verwendete_module.add(imp)
                verwendet_von[imp].append(datei)
    
    nicht_verwendet = [f for name, f in modulnamen_to_dateien.items() if name not in verwendete_module]
    
    return modulnamen_to_dateien, verwendet_von, nicht_verwendet

# -------------------------------------------
# ✅ Flake8-Analyse
# -------------------------------------------

def flake8_pruefen(dateien):
    print("\n🧪 Flake8 Codeprüfung:")
    try:
        subprocess.run(["flake8", "--version"], check=True, capture_output=True)
    except FileNotFoundError:
        print("❌ flake8 ist nicht installiert. Bitte mit `pip install flake8` installieren.")
        return

    for datei in dateien:
        print(f"📂 {datei}")
        result = subprocess.run(["flake8", datei], capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        else:
            print("   ✅ Keine Probleme gefunden.")

# -------------------------------------------
# 🧰 Hauptfunktion
# -------------------------------------------

def hauptfunktion(startverzeichnis):
    print(f"🔍 Analyse im Projektordner: {startverzeichnis}\n")

    py_dateien = finde_python_dateien(startverzeichnis)
    alle_module, verwendet_von, nicht_genutzt = analysiere_imports(py_dateien)

    print("📄 Gefundene Python-Dateien:")
    for modul, pfad in alle_module.items():
        print(f"  {modul:<20} → {pfad}")

    print("\n🔗 Importierte Module (aus Projekt):")
    for modul, verwendet_durch in verwendet_von.items():
        print(f"  {modul:<20} verwendet in:")
        for nutzer in verwendet_durch:
            print(f"     └── watchkido")

    print("\n🧹 Nicht verwendete .py-Dateien:")
    for pfad in nicht_genutzt:
        print(f"  ❌ {pfad}")

    # Speichern
    with open("import_analyse_ergebnis.txt", "w", encoding="utf-8") as f:
        f.write("📄 Python-Dateien:\n")
        for modul, pfad in alle_module.items():
            f.write(f"{modul} → {pfad}\n")
        f.write("\n🔗 Verwendete Module:\n")
        for modul, verwendet_durch in verwendet_von.items():
            f.write(f"{modul} verwendet in:\n")
            for nutzer in verwendet_durch:
                f.write(f"  └── watchkido\n")
        f.write("\n🧹 Nicht verwendete Dateien:\n")
        for pfad in nicht_genutzt:
            f.write(f"❌ {pfad}\n")

    flake8_pruefen(py_dateien)
    print("\n✅ Analyse abgeschlossen. Ergebnisse gespeichert in 'import_analyse_ergebnis.txt'")

# -------------------------------------------
# 🏁 Ausführung
# -------------------------------------------

if __name__ == "__main__":
    projektpfad = "."  # Standard: aktuelles Verzeichnis
    hauptfunktion(projektpfad)
