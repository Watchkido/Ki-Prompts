# 💻 Tricks und Kniffe für besseres Programmieren mit VS Code

Eine umfassende Sammlung von Tipps, Shortcuts und bewährten Praktiken für effizienteres Programmieren in Python und C++ mit Visual Studio Code.

## 🚀 Allgemeine Productivity-Tricks

| Shortcut | Beschreibung |
|----------|--------------|
| `Ctrl+P` | Schnell öffnen: Dateinamen tippen oder `@` für Funktionen/Klassen |
| `Ctrl+Shift+O` | Springe direkt zu Methoden/Symbolen in der aktuellen Datei |
| `Ctrl+Shift+L` | Alle gleichen Wörter im Dokument markieren (Multicursor) |
| `Alt+Shift+↓/↑` | Zeile duplizieren |
| `Ctrl+/` | Kommentar toggeln (auch für Blockauswahl) |
| `F2` | Refactoring: Variablen/Funktionsnamen umbenennen |
| `Ctrl+Shift+M` | Alle Probleme (Fehler/Warnungen) anzeigen |
| `Ctrl+Shift+E` | Fokus auf Explorer |
| `Ctrl+Shift+D` | Fokus auf Debugger |

## 🤖 GitHub Copilot effizient nutzen

| Trick | Beschreibung |
|-------|--------------|
| **Ghost-Text bewusst steuern** | Schreibe präzise Funktionsnamen oder Docstrings für gezielte Vorschläge |
| **Kommentar prompting** | `# Berechne die Fibonacci-Zahlen rekursiv` → führt zu zielgerichtetem Code |
| **Tab & Alt+[/]** | Vorschlag akzeptieren / andere Vorschläge durchgehen |
| **Klare Absicht zeigen** | `# Erzeuge Zufallszahlen mit Normalverteilung` führt zu besserem Output |

## 📦 Empfohlene Extensions

### 🐍 Für Python
- **Python (Microsoft)**: Linting, Debugging, IntelliSense
- **Pylance**: High-Performance Language Server
- **Jupyter**: Interaktive Notebooks in VS Code
- **Black Formatter**: Automatische Formatierung
- **Flake8**: Für Linting & PEP8-Einhaltung
- **Python Docstring Generator**: Docstrings automatisch generieren

### ⚡ Für C++
- **C/C++ (Microsoft)**: IntelliSense, Debugging, Linting
- **CMake Tools**: Für Build-Management & Projekte
- **Better C++ Syntax**: Verbesserte Syntax-Hervorhebung
- **Include Autocomplete**: Vervollständigt #include automatisch
- **clangd**: High-Performance Code-Intelligence

### 🛠 Sonstige nützliche Erweiterungen
- **vscode-icons**: Schöne Dateityp-Icons
- **Todo Tree**: Visualisiere `# TODO:` in Sidebar
- **REST Client**: Teste APIs direkt in VS Code
- **Bookmarks**: Setze Sprungmarken im Code
- **Path Intellisense**: Auto-Vervollständigung für Dateipfade
- **GitLens**: Superpower für Git - Blame, Verlauf, Branch-Analyse

## 🐛 Code-Analyse & Debugging

| Tool | Zweck |
|------|-------|
| **Breakpoint + F5** | Starte Debugging mit variabler Beobachtung |
| **"Watch" Panel** | Beobachte Variablen beim Debuggen |
| **Inline-Werte anzeigen** | Einstellungen: `"debug.inlineValues": true` |
| **Python Interactive** | `Shift+Enter` - teste Codezeilen interaktiv |
| **Task Runner** | tasks.json - automatisiere Kompilierungen oder Tests |

## 🔧 Git & GitHub Integration

| Trick | Beschreibung |
|-------|--------------|
| `Ctrl+Shift+G` | Git-Ansicht für Commits, Änderungen, Branches |
| `@username, #issue` | Verlinkung zu GitHub-Profilen & Issues in Commits |
| **Merge Conflicts** | Super UI für Merge-Konflikte in VS Code |
| **Terminal + Git Shortcuts** | Nutze Aliase wie `git st`, `git co`, `git br`, `git lg` |

## ⚙️ Empfohlene Einstellungen

Beispiel für `settings.json`:

```json
{
  "editor.formatOnSave": true,
  "editor.tabSize": 4,
  "files.autoSave": "afterDelay",
  "python.formatting.provider": "black",
  "editor.codeActionsOnSave": {
    "source.organizeImports": true
  },
  "git.enableSmartCommit": true,
  "github.copilot.enable": {
    "*": true,
    "plaintext": false,
    "markdown": true,
    "python": true
  },
  "workbench.iconTheme": "vscode-icons"
}
```

## 📝 Eigene Code-Snippets

Erstelle eigene Snippets über: `Strg+Shift+P` → "Preferences: Configure User Snippets"

Beispiel für Python:
```json
"Print Debug": {
  "prefix": "pdbg",
  "body": ["print(f'🔍 ${1:var} = {${1:var}}')"],
  "description": "Print Debug Variable"
}
```

## 📁 Workspace-Organisation

### Was ist ein Workspace?
Ein Workspace ist wie ein Schreibtisch, auf dem du mehrere Ordner gleichzeitig geöffnet hast. Statt jeden Ordner einzeln zu öffnen, kannst du mehrere Projekte, Unterordner und Dateien gemeinsam verwalten.

### Workspace erstellen:
1. Öffne deine gewünschten Ordner in VS Code
2. `Datei` → `Arbeitsbereich speichern unter...`
3. Speichere als `.code-workspace` Datei

### Beispiel-Struktur:
```
E:/dev/
├── Projekte_Python_venv/     # Python-Projekte mit venv
├── Projekte_C/               # C/C++ Projekte
├── Prompts/                  # Ideen, Notizen
├── Scripte/                  # Einzelne Skripte
└── dev.code-workspace        # Workspace-Datei
```

### Workspace-Datei Beispiel:
```json
{
  "folders": [
    { "path": "Projekte_Python_venv" },
    { "path": "Projekte_C" },
    { "path": "Prompts" },
    { "path": "Scripte" }
  ],
  "settings": {
    "python.pythonPath": "Projekte_Python_venv/venv/Scripts/python.exe"
  }
}
```

## 🔄 .vscode Ordner verstehen

Der `.vscode` Ordner enthält projektspezifische Einstellungen:

| Datei | Zweck |
|-------|-------|
| `settings.json` | Projekteigene Editor-Einstellungen |
| `launch.json` | Debugging-Konfigurationen |
| `tasks.json` | Automatisierbare Aufgaben (Build, Test, Linting) |
| `extensions.json` | Empfehlungen für Extensions |
| `c_cpp_properties.json` | (C++) Compilerpfade, IntelliSense-Einstellungen |

## 🐍 Python Virtual Environments

### Wichtige Regeln:
- **Niemals venv kopieren!** Erstelle immer neue Umgebungen
- Nutze `.venv` (mit Punkt) für bessere Git-Kompatibilität
- Pro Projekt ein eigenes venv

### Neues venv erstellen:
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

### Packages übertragen:
```bash
# Im alten Projekt
pip freeze > requirements.txt

# Im neuen Projekt
pip install -r requirements.txt
```

## 🗂 Git Best Practices

### .gitignore Regeln:
Jedes Git-Projekt sollte eine eigene `.gitignore` haben:

**Für Python:**
```
.venv/
venv/
__pycache__/
*.py[cod]
.ipynb_checkpoints/
.vscode/
```

**Für C++:**
```
*.o
*.out
*.exe
/build/
/dist/
.vscode/
```

### Git-Repository pro Projekt:
```bash
cd mein_projekt/
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/username/projekt.git
git push -u origin main
```

## 🎯 Tägliche Workflows

| Aktion | Shortcut/Befehl |
|--------|-----------------|
| **Build starten** | `Ctrl+Shift+B` |
| **Python-Interpreter wählen** | `Ctrl+Shift+P` → "Python: Select Interpreter" |
| **Debugging starten** | `F5` |
| **Terminal öffnen** | `Ctrl+Shift+`` (Backtick) |
| **Problem-Panel** | `Ctrl+Shift+M` |

## 📊 Datenanalyse & Visualisierung

### Interaktive Diagramme mit Python:
```python
import pandas as pd
import plotly.express as px
import streamlit as st

# Daten laden und filtern
df = pd.read_csv("daten.csv")

# Interaktive Filter
ort = st.selectbox("Ort", df['Ort'].unique())
stunde = st.slider("Stunde", 0, 23)

gefiltert = df[(df['Ort'] == ort) & (df['Stunde'] == stunde)]

# Diagramm erstellen
fig = px.line(gefiltert, x='Zeit', y='Temperatur')
st.plotly_chart(fig)
```

### Dashboard mit Streamlit starten:
```bash
pip install streamlit
streamlit run dashboard.py
```

## 📚 Automatische Dokumentation

### Für Python (Sphinx):
```bash
pip install sphinx sphinx_rtd_theme
sphinx-quickstart docs
# Konfiguration in docs/source/conf.py
make html
```

### Für C++ (Doxygen):
```bash
doxygen -g Doxyfile
# Konfiguration in Doxyfile anpassen
doxygen Doxyfile
```

## 🎵 Audio-Optimierung mit Equalizer APO

### Installation:
1. Equalizer APO von SourceForge laden
2. Peace GUI als Oberfläche installieren
3. Geräte auswählen und Windows neustarten

### Anti-Blech Mikrofon-Preset:
```
# GraphicEQ: 25 -10; 40 -8; 63 -5; 100 -2.5; 160 0; 250 1.5; 400 2; 630 2.5; 1000 2.5; 1600 1.5; 2500 0; 4000 -2; 6300 -4; 10000 -5; 16000 -6
```

### Datenschutz-Einstellungen für Mikrofon:
1. `Einstellungen` → `Datenschutz & Sicherheit` → `Mikrofon`
2. "Zugriff auf das Mikrofon" aktivieren
3. "Desktop-Apps den Zugriff erlauben" aktivieren

## 💡 Pro-Tipps

1. **Nutze mehrere Workspaces** für verschiedene Themenbereiche
2. **Erstelle Templates** für häufige Projektstrukturen
3. **Verwende aussagekräftige Commit-Nachrichten**
4. **Dokumentiere deine Shortcuts** in einer persönlichen Cheatsheet
5. **Teste regelmäßig** deine Backup- und Restore-Prozesse
6. **Nutze Code-Reviews** auch bei Einzelprojekten zur Selbstreflexion

---

*Erstellt für effizienteres Programmieren mit VS Code, Python und C++*