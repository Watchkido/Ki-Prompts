import os
import subprocess
from config import CONFIG
def initialisiere_git_und_push(projekt, nutzer, privat, basis_pfad):
    projekt_pfad = os.path.join(basis_pfad, projekt)
    # Wechsle ins Projektverzeichnis
    os.chdir(projekt_pfad)
    subprocess.run(["git", "init"])
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Initial commit"])
    # Optional: GitHub Push, falls gh CLI installiert ist
    # repo_visibility = "--private" if privat else "--public"
    # subprocess.run(["gh", "repo", "create", f"watchkido/019_KI_Prompts", repo_visibility, "--source=.", "--push"])
    print(f"🚀 Repo lokal initialisiert (GitHub Push optional).")

        
if __name__ == "__main__":
    # Code hier drunter wird nur ausgeführt wenn das Skript direkt aufgerufen wird
    pass