# VS Code Workspace Konfiguration

Diese Dokumentation erklärt alle JSON-Konfigurationsdateien im `.vscode` Ordner für optimale Entwicklungsumgebung in Visual Studio Code.

## 📁 Übersicht der Konfigurationsdateien

| Datei | Zweck | Schema-Typ |
|-------|-------|------------|
| `settings.json` | Workspace-spezifische Einstellungen | JSONC |
| `launch.json` | Debug-Konfigurationen | JSONC |
| `tasks.json` | Build- und Automatisierungs-Tasks | JSONC |
| `extensions.json` | Empfohlene Erweiterungen | JSONC |
| `c_cpp_properties.json` | C/C++ IntelliSense-Konfiguration | JSON |

> **Hinweis**: JSONC unterstützt Kommentare mit `//` und `/* */`, reines JSON nicht.

---

## ⚙️ settings.json

**Zweck**: Workspace-spezifische VS Code-Einstellungen, die nur für dieses Projekt gelten.

### Struktur
```json
{
    "python.defaultInterpreterPath": "./venv/Scripts/python.exe",
    "editor.tabSize": 4,
    "files.encoding": "utf8"
}
```

### Wichtige Einstellungskategorien

#### Python-Konfiguration
- `python.defaultInterpreterPath` - Standard Python-Interpreter
- `python.formatting.provider` - Code-Formatter (black, autopep8)
- `python.linting.enabled` - Linting aktivieren/deaktivieren
- `python.testing.pytestEnabled` - pytest Integration

#### Editor-Verhalten
- `editor.tabSize` - Tab-Größe (meist 2 oder 4)
- `editor.insertSpaces` - Leerzeichen statt Tabs
- `editor.formatOnSave` - Automatisches Formatieren beim Speichern
- `editor.rulers` - Vertikale Linien bei bestimmten Spalten

#### Dateien & Encoding
- `files.encoding` - Standard-Zeichenkodierung
- `files.eol` - Zeilenendeformat (\n, \r\n)
- `files.exclude` - Dateien aus Explorer ausblenden

#### GitHub Copilot
- `github.copilot.enable` - Copilot aktivieren
- `github.copilot.inlineSuggest.enable` - Inline-Vorschläge
- `github.copilot.chat.enabled` - Chat-Feature

---

## 🐛 launch.json

**Zweck**: Debug-Konfigurationen für verschiedene Programmtypen und Szenarien.

### Struktur
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "debugpy",
            "request": "launch",
            "program": "${file}"
        }
    ]
}
```

### Konfigurationstypen

#### Python-Debugging
- **Current File**: Aktuelle Python-Datei debuggen
- **Main Script**: Haupt-Skript des Projekts starten
- **Tests**: Unit Tests mit pytest ausführen
- **Django**: Django-Entwicklungsserver debuggen

#### Wichtige Parameter
- `type` - Debugger-Typ (`debugpy`, `node`, `chrome`)
- `request` - `launch` (starten) oder `attach` (anhängen)
- `program` - Zu debuggende Datei/Skript
- `args` - Kommandozeilen-Argumente
- `console` - Output-Ziel (`integratedTerminal`, `internalConsole`)
- `cwd` - Arbeitsverzeichnis
- `env` - Umgebungsvariablen

#### Variable Substitution
- `${workspaceFolder}` - Projekt-Stammverzeichnis
- `${file}` - Aktuell geöffnete Datei
- `${env:VARIABLE}` - Umgebungsvariable
- `${config:setting}` - VS Code-Einstellung

---

## 🔧 tasks.json

**Zweck**: Automatisierte Build-, Test- und Deployment-Tasks definieren.

### Struktur
```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Build Project",
            "type": "shell",
            "command": "python",
            "args": ["setup.py", "build"]
        }
    ]
}
```

### Task-Typen

#### Build-Tasks
- **Python Build**: `python setup.py build`
- **Pip Install**: `pip install -r requirements.txt`
- **Poetry Install**: `poetry install`

#### Test-Tasks
- **pytest**: Unit Tests ausführen
- **Coverage**: Code-Abdeckung messen
- **Linting**: Code-Qualität prüfen (pylint, flake8)

#### Wichtige Parameter
- `label` - Anzeigename des Tasks
- `type` - Task-Typ (`shell`, `process`)
- `command` - Auszuführender Befehl
- `args` - Befehlsargumente
- `group` - Gruppierung (`build`, `test`)
- `presentation` - Output-Darstellung
- `problemMatcher` - Fehler-Pattern für Problems-Panel

#### Task-Gruppen
- `build` - Standard-Build-Task (Strg+Shift+B)
- `test` - Standard-Test-Task
- `clean` - Aufräum-Tasks

---

## 🧩 extensions.json

**Zweck**: Empfohlene Erweiterungen für das Projekt definieren.

### Struktur
```json
{
    "recommendations": [
        "ms-python.python",
        "ms-python.flake8",
        "github.copilot"
    ],
    "unwantedRecommendations": [
        "ms-python.pylint"
    ]
}
```

### Kategorien

#### Python-Entwicklung
- `ms-python.python` - Python-Unterstützung
- `ms-python.pylint` - Pylint Integration
- `ms-python.flake8` - Flake8 Linter
- `ms-python.black-formatter` - Black Code-Formatter

#### C/C++ Entwicklung
- `ms-vscode.cpptools` - C/C++ IntelliSense
- `ms-vscode.cmake-tools` - CMake Support
- `twxs.cmake` - CMake Language Support

#### Arduino-Entwicklung
- `vsciot-vscode.vscode-arduino` - Arduino IDE Integration
- `platformio.platformio-ide` - PlatformIO Support

#### Allgemeine Tools
- `github.copilot` - AI-Programmierassistent
- `eamodio.gitlens` - Git-Integration erweitern
- `ms-vsliveshare.vsliveshare` - Live-Kollaboration

---

## 🎯 c_cpp_properties.json

**Zweck**: IntelliSense-Konfiguration für C/C++-Projekte und Arduino.

> **Detaillierte Dokumentation**: Siehe `c_cpp_properties.md`

### Konfigurationen
- **Win32**: Windows native C/C++ Entwicklung
- **Linux**: Linux native C/C++ Entwicklung  
- **Arduino Uno**: ATmega328P Mikrocontroller
- **Arduino Mega 2560**: ATmega2560 Mikrocontroller
- **Arduino ESP32**: ESP32 Development Board
- **Arduino ESP8266**: ESP8266 NodeMCU
- **PlatformIO**: Universal Embedded Platform

---

## 🚀 Best Practices

### 1. Versionskontrolle
```gitignore
# VS Code settings - nur workspace-spezifische Dateien committen
.vscode/settings.json
.vscode/tasks.json
.vscode/launch.json
.vscode/extensions.json

# Persönliche Einstellungen ignorieren
.vscode/sftp.json
```

### 2. Team-Entwicklung
- **Committen**: `extensions.json`, `tasks.json`, `launch.json` (Basis-Konfiguration)
- **Ignorieren**: Persönliche `settings.json` Anpassungen
- **Dokumentieren**: Alle projektspezifischen Konfigurationen

### 3. Multi-Language Projekte
```json
// settings.json für gemischte Projekte
{
    "[python]": {
        "editor.tabSize": 4
    },
    "[javascript]": {
        "editor.tabSize": 2
    },
    "[cpp]": {
        "editor.tabSize": 4,
        "editor.insertSpaces": true
    }
}
```

### 4. Umgebungsspezifische Konfiguration
```json
// launch.json mit Umgebungsvariablen
{
    "configurations": [
        {
            "name": "Debug Development",
            "env": {
                "DEBUG": "1",
                "DATABASE_URL": "sqlite:///dev.db"
            }
        }
    ]
}
```

---

## 🔍 Troubleshooting

### Häufige Probleme

#### IntelliSense funktioniert nicht
1. `c_cpp_properties.json` Pfade prüfen
2. Compiler-Path validieren
3. Include-Pfade aktualisieren

#### Tasks schlagen fehl
1. Shell-Path prüfen (`PowerShell` vs `cmd`)
2. Arbeitsverzeichnis (`cwd`) setzen
3. Umgebungsvariablen definieren

#### Python-Interpreter nicht gefunden
1. `python.defaultInterpreterPath` setzen
2. Virtual Environment aktivieren
3. Python-Extension neu laden

### Debugging-Tipps
- `Strg+Shift+P` > "Developer: Reload Window"
- Output-Panel für Fehlermeldungen prüfen
- VS Code-Logs in Entwicklertools ansehen

---

## 📚 Weiterführende Dokumentation

- [VS Code User and Workspace Settings](https://code.visualstudio.com/docs/getstarted/settings)
- [Debugging in VS Code](https://code.visualstudio.com/docs/editor/debugging)
- [Tasks in VS Code](https://code.visualstudio.com/docs/editor/tasks)
- [Managing Extensions](https://code.visualstudio.com/docs/editor/extension-marketplace)
- [C++ Configuration](https://code.visualstudio.com/docs/cpp/config-linux)