import os
import subprocess
import sys
from pathlib import Path
from config import CONFIG

class GitOperationError(Exception):
    """Custom Exception für Git-Operationen"""
    pass

def run_git_command(command, error_message):
    """
    Führt einen Git-Befehl aus und behandelt Fehler
    
    Args:
        command (list): Git-Befehl als Liste
        error_message (str): Fehlermeldung bei Misserfolg
    
    Returns:
        subprocess.CompletedProcess: Ergebnis des Befehls
    
    Raises:
        GitOperationError: Bei Fehlern während der Ausführung
    """
    try:
        print(f"🔄 Führe aus: {' '.join(command)}")
        result = subprocess.run(
            command, 
            capture_output=True, 
            text=True, 
            check=True
        )
        print(f"✅ Erfolgreich: {' '.join(command)}")
        return result
    except subprocess.CalledProcessError as e:
        error_msg = f"{error_message}\nFehlercode: {e.returncode}\nStderr: {e.stderr}\nStdout: {e.stdout}"
        print(f"❌ {error_msg}")
        raise GitOperationError(error_msg) from e
    except FileNotFoundError:
        error_msg = f"Git ist nicht installiert oder nicht im PATH verfügbar"
        print(f"❌ {error_msg}")
        raise GitOperationError(error_msg)

def create_readme_file():
    """
    Erstellt oder erweitert die README.md Datei
    
    Raises:
        GitOperationError: Bei Fehlern beim Schreiben der Datei
    """
    try:
        readme_path = Path("README.md")
        content = "# Ki-Prompts\n"
        
        if readme_path.exists():
            print("📝 README.md existiert bereits, füge Inhalt hinzu...")
            with open(readme_path, 'a', encoding='utf-8') as f:
                f.write(f"\n{content}")
        else:
            print("📝 Erstelle neue README.md...")
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(content)
        
        print("✅ README.md erfolgreich erstellt/erweitert")
        return readme_path
    except IOError as e:
        error_msg = f"Fehler beim Erstellen/Erweitern der README.md: {e}"
        print(f"❌ {error_msg}")
        raise GitOperationError(error_msg) from e

def initialize_git_repository():
    """
    Initialisiert ein neues Git-Repository
    
    Raises:
        GitOperationError: Bei Fehlern während der Git-Initialisierung
    """
    # Prüfe ob bereits ein Git-Repository existiert
    if Path(".git").exists():
        print("⚠️  Git-Repository existiert bereits, überspringe Initialisierung")
        return
    
    run_git_command(
        ["git", "init"],
        "Fehler beim Initialisieren des Git-Repositories"
    )

def add_files_to_git():
    """
    Fügt README.md zum Git-Repository hinzu
    
    Raises:
        GitOperationError: Bei Fehlern beim Hinzufügen der Dateien
    """
    run_git_command(
        ["git", "add", "README.md"],
        "Fehler beim Hinzufügen der README.md zu Git"
    )

def create_initial_commit():
    """
    Erstellt den ersten Commit
    
    Raises:
        GitOperationError: Bei Fehlern beim Erstellen des Commits
    """
    run_git_command(
        ["git", "commit", "-m", "first commit"],
        "Fehler beim Erstellen des ersten Commits"
    )

def set_main_branch():
    """
    Setzt den Hauptbranch auf 'main'
    
    Raises:
        GitOperationError: Bei Fehlern beim Umbenennen des Branches
    """
    run_git_command(
        ["git", "branch", "-M", "main"],
        "Fehler beim Setzen des main-Branches"
    )

def add_remote_origin():
    """
    Fügt das GitHub-Repository als remote origin hinzu
    
    Raises:
        GitOperationError: Bei Fehlern beim Hinzufügen des Remote-Repositories
    """
    # Prüfe ob bereits ein remote origin existiert
    try:
        result = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            capture_output=True,
            text=True,
            check=True
        )
        print(f"⚠️  Remote origin existiert bereits: {result.stdout.strip()}")
        return
    except subprocess.CalledProcessError:
        # Remote origin existiert nicht, füge es hinzu
        pass
    
    run_git_command(
        ["git", "remote", "add", "origin", "https://github.com/Watchkido/Ki-Prompts.git"],
        "Fehler beim Hinzufügen des Remote-Repositories"
    )

def push_to_github():
    """
    Pusht den Code zum GitHub-Repository
    
    Raises:
        GitOperationError: Bei Fehlern beim Pushen
    """
    run_git_command(
        ["git", "push", "-u", "origin", "main"],
        "Fehler beim Pushen zum GitHub-Repository"
    )

def setup_git_repository():
    """
    Hauptfunktion zum Einrichten des Git-Repositories
    
    Diese Funktion führt alle Schritte aus:
    1. README.md erstellen/erweitern
    2. Git initialisieren
    3. Dateien hinzufügen
    4. Ersten Commit erstellen
    5. Main-Branch setzen
    6. Remote origin hinzufügen
    7. Zum GitHub pushen
    
    Returns:
        bool: True bei Erfolg, False bei Fehlern
    """
    try:
        print("🚀 Starte Git-Repository Setup...")
        print(f"📁 Arbeitsverzeichnis: {os.getcwd()}")
        
        # Schritt 1: README.md erstellen
        create_readme_file()
        
        # Schritt 2: Git initialisieren
        initialize_git_repository()
        
        # Schritt 3: Dateien hinzufügen
        add_files_to_git()
        
        # Schritt 4: Ersten Commit erstellen
        create_initial_commit()
        
        # Schritt 5: Main-Branch setzen
        set_main_branch()
        
        # Schritt 6: Remote origin hinzufügen
        add_remote_origin()
        
        # Schritt 7: Zum GitHub pushen
        push_to_github()
        
        print("🎉 Git-Repository erfolgreich eingerichtet und gepusht!")
        return True
        
    except GitOperationError as e:
        print(f"❌ Git-Operation fehlgeschlagen: {e}")
        return False
    except Exception as e:
        print(f"❌ Unerwarteter Fehler: {e}")
        return False

def initialisiere_git_und_push(projekt, nutzer, privat, basis_pfad):
    """
    Legacy-Funktion für Kompatibilität (optional)
    """
    projekt_pfad = os.path.join(basis_pfad, projekt)
    # Wechsle ins Projektverzeichnis
    original_dir = os.getcwd()
    try:
        os.chdir(projekt_pfad)
        return setup_git_repository()
    finally:
        os.chdir(original_dir)

if __name__ == "__main__":
    # Hauptausführung wenn Script direkt aufgerufen wird
    success = setup_git_repository()
    sys.exit(0 if success else 1)