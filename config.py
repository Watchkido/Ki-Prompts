"""
config.py    print(CONFIG.BASIS_PFAD)
Konfigurationseinstellungen für das Projekt.
Hier werden globale Einstellungen und Parameter definiert.
"""
import datetime
from types import SimpleNamespace

def aktuelle_version():
    """Gibt einen Zeitstempel für die aktuelle Version zurück."""
    return datetime.datetime.now().strftime("%Y-%m-%d--%H:%M:%SMESZ")

CONFIG = SimpleNamespace(
    BASIS_PFAD=".",
    PROJEKT_PFAD=".",
    TEMPLATE_DIR="./templates",
    EMAIL=f"script-{aktuelle_version()}@watchkido.de",
    AUTOR="Frank Albrecht",
    VERSION=aktuelle_version(),
    LIZENZ="MIT License",
    GITHUB_USER="watchkido",
    ORDNER_STRUKTUR=[
        "./.copilot",
        "./src/019_KI_Prompts",
        "./src/019_KI_Prompts/utils",
        "./tests",
        "./prompts",
        "./scripts",
        "./data/raw",
        "./data/processed",
        "./data/results",
        "./data/merged",
        "./data/finished",
        "./data/cached",
        "./docs",
        "./datenbank",
        "./notebooks"
    ],
    REQUIREMENTS="requirements.txt",
    DEBUG=False,
    LOG_LEVEL="INFO",
    DEFAULT_ENCODING="utf-8",
    SPRACHE="de"
    ,
    IGNORIERTE_ORDNER=(".venv", ".git", "__pycache__"),
    VERSTECKTE_ORDNER_PREFIX=".",
    ANALYSE_ERGEBNIS_DATEI="import_analyse_ergebnis.txt",
    PYTHON_DATEIENDUNG=".py",
    TOOL_FLAKE8="flake8"
    
    
)
