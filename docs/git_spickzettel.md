# Git-Befehlsübersicht

| Kategorie                     | Befehl                                               | Beschreibung                                   |
| ----------------------------- | ---------------------------------------------------- | ---------------------------------------------- |
| **Installation**              | Windows                                              | windows.github.com                             |
|                               | macOS                                                | mac.github.com                                 |
|                               | Alle Plattformen                                     | git-scm.com                                    |
| **User konfigurieren**        | `git config --global user.name "[name]"`             | Benutzername für Commits setzen                |
|                               | `git config --global user.email "[email]"`           | E-Mail-Adresse für Commits setzen              |
| **Repository erstellen**      | `git init [projekt]`                                 | Erstellt lokales Repository                    |
|                               | `git clone [url]`                                    | Klont Repository inkl. Historie                |
| **Änderungen prüfen**         | `git status`                                         | Zeigt neue/geänderte Dateien                   |
|                               | `git diff`                                           | Zeigt unstaged Änderungen                      |
|                               | `git add [file]`                                     | Datei zum Staging hinzufügen                   |
|                               | `git diff --staged`                                  | Unterschiede: Index vs. Arbeitsverzeichnis     |
|                               | `git reset [file]`                                   | Datei aus Index entfernen (Änderung bleibt)    |
|                               | `git commit -m "[message]"`                          | Commit mit Nachricht                           |
| **Branches verwalten**        | `git branch`                                         | Lokale Branches anzeigen                       |
|                               | `git branch [name]`                                  | Neuen Branch erstellen                         |
|                               | `git switch -c [name]`                               | Erstellen und zu Branch wechseln               |
|                               | `git merge [name]`                                   | Branch in aktuellen mergen                     |
|                               | `git branch -d [name]`                               | Branch löschen                                 |
| **Dateien verwalten**         | `git rm [file]`                                      | Datei löschen und zum Entfernen stagen         |
|                               | `git rm --cached [file]`                             | Nur aus Git entfernen, lokal behalten          |
|                               | `git mv [alt] [neu]`                                 | Datei umbenennen und für Commit vorbereiten    |
| **Ignorieren von Dateien**    | `.gitignore`                                         | Enthält Muster wie `*.log`, `build/`, `temp-*` |
|                               | `git ls-files --others --ignored --exclude-standard` | Zeigt ignorierte Dateien an                    |
| **Stash (Zwischenspeichern)** | `git stash`                                          | Änderungen zwischenspeichern                   |
|                               | `git stash pop`                                      | Letzten Stash anwenden                         |
|                               | `git stash list`                                     | Alle Stashes anzeigen                          |
|                               | `git stash drop`                                     | Letzten Stash verwerfen                        |
| **Historie einsehen**         | `git log`                                            | Historie anzeigen                              |
|                               | `git log --follow [file]`                            | Historie einer Datei inkl. Umbenennung         |
|                               | `git show [commit]`                                  | Änderungen durch Commit anzeigen               |
|                               | `git diff [branch1]...[branch2]`                     | Unterschiede zwischen Branches                 |
| **Commits zurücksetzen**      | `git reset [commit]`                                 | Commits rückgängig machen, Änderungen bleiben  |
|                               | `git reset --hard [commit]`                          | Commits + Änderungen verwerfen                 |
| **Remote-Repos**              | `git fetch [remote]`                                 | Änderungen vom Remote holen                    |
|                               | `git merge [remote]/[branch]`                        | Remote-Branch in lokalen Branch mergen         |
|                               | `git push [remote] [branch]`                         | Lokalen Branch ins Remote pushen               |
|                               | `git pull`                                           | Fetch + Merge vom Remote                       |
|                               | `git add . , git commit -m "com" , git push          | allgemein:                                     |

…or create a new repository on the command line

echo "# 008_lottozahlen" >> README.md

git init

git add README.md

git commit -m "first commit"

git branch -M main

git remote add origin https://github.com/Watchkido/008_lottozahlen.git

git push -u origin main

…or push an existing repository from the command line

git remote add origin https://github.com/Watchkido/008_lottozahlen.git

git branch -M main

git push -u origin main

git push origin main --force-with-lease

git config --global http.postBuffer 524288000

git remote set-url origin git@github.com:Watchkido/008_lottozahlen.git

git push -u origin main

... oder

git lfs install
git lfs track "_.pkl" "_.csv" "\*.keras"
git add .gitattributes
git commit -m "Add Git LFS tracking"
git push -u origin main

branch push abbrechen: git reset --hard HEAD~1
