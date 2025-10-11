
import os
from config import CONFIG
from template_tools import copy_template


def kopfkommentar(dateiname, beschreibung, inhalt):
    return f'"""\n{dateiname}\n{beschreibung}\n{inhalt}\n"""\n\n'


def erstelle_struktur(projekt, nutzer, privat, basis_pfad=None):
    if basis_pfad is None:
        basis_pfad = CONFIG["BASIS_PFAD"]
    projekt_pfad = os.path.join(basis_pfad, projekt)
    struktur = [
        f"{projekt_pfad}/src/019_KI_Prompts",
        f"{projekt_pfad}/src/019_KI_Prompts/utils",
        f"{projekt_pfad}/tests",
        f"{projekt_pfad}/scripts",
        f"{projekt_pfad}/data/raw",
        f"{projekt_pfad}/data/processed",
        f"{projekt_pfad}/data/results",
        f"{projekt_pfad}/notebooks",
    ]

    files = {
        "README.md": f"{projekt_pfad}/README.md",
        ".gitignore": f"{projekt_pfad}/.gitignore",
        "requirements.txt": f"{projekt_pfad}/requirements.txt",
        "requirements-dev.txt": f"{projekt_pfad}/requirements-dev.txt",
        "pyprojekt.toml": f"{projekt_pfad}/pyprojekt.toml",
        "LICENSE": f"{projekt_pfad}/LICENSE",
    
        "src/data_loader.py": f"{projekt_pfad}/src/019_KI_Prompts/data_loader.py",
        "src/preprocessing.py": f"{projekt_pfad}/src/019_KI_Prompts/preprocessing.py",
        "src/analysis.py": f"{projekt_pfad}/src/019_KI_Prompts/analysis.py",
        "src/visualization.py": f"{projekt_pfad}/src/019_KI_Prompts/visualization.py",
        "src/reporting.py": f"{projekt_pfad}/src/019_KI_Prompts/reporting.py",
        "src/__init__.py": f"{projekt_pfad}/src/019_KI_Prompts/__init__.py",
        "src/main.py": f"{projekt_pfad}/src/019_KI_Prompts/main.py",
        "src/config.py": f"{projekt_pfad}/src/019_KI_Prompts/config.py",
        "src/constants.py": f"{projekt_pfad}/src/019_KI_Prompts/constants.py",
        "src/logging_config.py": f"{projekt_pfad}/src/019_KI_Prompts/logging_config.py",
        "src/exceptions.py": f"{projekt_pfad}/src/019_KI_Prompts/exceptions.py",
        "src/modul1.py": f"{projekt_pfad}/src/019_KI_Prompts/modul1.py",
        "src/modul2.py": f"{projekt_pfad}/src/019_KI_Prompts/modul2.py",
        "src/utils/__init__.py": f"{projekt_pfad}/src/019_KI_Prompts/utils/__init__.py",
        "src/utils/helper.py": f"{projekt_pfad}/src/019_KI_Prompts/utils/helper.py",
        "src/utils/konstanten.py": f"{projekt_pfad}/src/019_KI_Prompts/utils/konstanten.py",
    
        "tests/test_01_unit.py": f"{projekt_pfad}/tests/test_01_unit.py",
        "tests/test_02_integration.py": f"{projekt_pfad}/tests/test_02_integration.py",
        "tests/test_03_system.py": f"{projekt_pfad}/tests/test_03_system.py",
        "tests/test_04_fuzz.py": f"{projekt_pfad}/tests/test_04_fuzz.py",
        "tests/test_05_penetration.py": f"{projekt_pfad}/tests/test_05_penetration.py",
        "tests/test_05_security.py": f"{projekt_pfad}/tests/test_05_security.py",
        "tests/test_07_performance.py": f"{projekt_pfad}/tests/test_07_performance.py",
        "tests/test_08_Affe.py": f"{projekt_pfad}/tests/test_08_Affe.py",
        "tests/test_09_wiederherstellbarkeit.py": f"{projekt_pfad}/tests/test_09_wiederherstellbarkeit.py",
        "tests/test_10_Umwelt.py": f"{projekt_pfad}/tests/test_10_Umwelt.py",
        "tests/__init__.py": f"{projekt_pfad}/tests/__init__.py",
    
        "scripts/cleanup.py": f"{projekt_pfad}/scripts/cleanup.py",
        "scripts/data_processing.py": f"{projekt_pfad}/scripts/data_processing.py",
        "scripts/create_report.py": f"{projekt_pfad}/scripts/create_report.py",
    
        "notebooks/analysis.ipynb": f"{projekt_pfad}/notebooks/analysis.ipynb",
        "notebooks/sandbox.ipynb": f"{projekt_pfad}/notebooks/sandbox.ipynb",
        "notebooks/report.ipynb": f"{projekt_pfad}/notebooks/report.ipynb",
    }

    for folder in struktur:
        os.makedirs(folder, exist_ok=True)

    
    for template_name, target_path in files.items():
        template_path = os.path.join(CONFIG["TEMPLATE_DIR"], template_name)
        replacements = {
            "019_KI_Prompts": projekt,
            "watchkido": nutzer,
            # weitere Platzhalter nach Bedarf
        }
        copy_template(template_path, target_path, replacements)

if __name__ == "__main__":
    # Code hier drunter wird nur ausgeführt wenn das Skript direkt aufgerufen wird
    pass