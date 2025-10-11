# C/C++ Properties Konfiguration

Diese Datei dokumentiert die verschiedenen Konfigurationen in `c_cpp_properties.json` für optimale IntelliSense-Unterstützung bei C/C++ und Arduino-Entwicklung.

## Konfigurationsübersicht

### Win32 Konfiguration
- **Zweck**: Native Windows C/C++ Entwicklung mit MSVC
- **Compiler**: Microsoft Visual Studio Community 2022
- **Standards**: C17 und C++17
- **Include-Pfade**: MSVC-Bibliotheken und Windows SDK

### Linux Konfiguration  
- **Zweck**: Native Linux C/C++ Entwicklung
- **Compiler**: GCC (/usr/bin/gcc)
- **Standards**: C17 und C++17
- **Include-Pfade**: Nur Workspace-Dateien

### Arduino Uno Konfiguration
- **Zweck**: Arduino Uno/Nano Entwicklung (ATmega328P)
- **Compiler**: AVR-GCC aus Arduino15 Package
- **Standards**: C11 und C++11 (Arduino-kompatibel)
- **CPU-Frequenz**: 16MHz
- **Defines**: 
  - `ARDUINO=10819` - Arduino IDE Version
  - `ARDUINO_AVR_UNO` - Board-spezifisch
  - `F_CPU=16000000L` - 16MHz Takt
  - `__AVR_ATmega328P__` - Mikrocontroller

### Arduino Mega 2560 Konfiguration
- **Zweck**: Arduino Mega 2560 Entwicklung (ATmega2560)
- **Compiler**: AVR-GCC aus Arduino15 Package
- **Standards**: C11 und C++11 (Arduino-kompatibel)
- **CPU-Frequenz**: 16MHz
- **Speicher**: 256KB Flash, 8KB SRAM, 4KB EEPROM
- **Defines**:
  - `ARDUINO_AVR_MEGA2560` - Board-spezifisch
  - `__AVR_ATmega2560__` - Mikrocontroller mit mehr Speicher
  - `F_CPU=16000000L` - 16MHz Takt
- **Besonderheiten**: Mehr I/O-Pins und Speicher als Uno

### Arduino ESP32 Konfiguration
- **Zweck**: ESP32 Development Board Entwicklung
- **Compiler**: Xtensa ESP32 ELF GCC
- **Standards**: C11 und C++11
- **CPU-Frequenz**: 240MHz
- **Defines**:
  - `ARDUINO_ESP32_DEV` - ESP32 Board
  - `F_CPU=240000000L` - 240MHz Takt
  - `ESP32` - Platform-spezifisch

### PlatformIO Konfiguration
- **Zweck**: Universal für verschiedene Mikrocontroller
- **Compiler**: Dynamisch je nach Board
- **Standards**: C11 und C++14
- **Features**: Automatische Library-Verwaltung

## Pfad-Variablen

- `${workspaceFolder}` - Aktuelles Projekt-Verzeichnis
- `${env:USERNAME}` - Windows-Benutzername
- `**` - Rekursive Ordner-Suche

## Arduino-spezifische Optimierungen

1. **Compiler-Args**: Optimierung für Embedded Systems
   - `-mmcu=atmega328p` (Uno) / `-mmcu=atmega2560` (Mega)
   - `-fno-exceptions` - Keine C++ Exceptions (spart Speicher)
   - `-fno-threadsafe-statics` - Keine Thread-sicheren Statics
2. **Include-Pfade**: Arduino Core, Libraries und Board-Varianten
   - `/cores/arduino` - Arduino Core-Funktionen
   - `/variants/standard` (Uno) / `/variants/mega` (Mega) - Pin-Definitionen
3. **Defines**: Hardware-spezifische Makros für korrekte IntelliSense
   - Board-spezifische Defines für Pin-Mapping
   - Mikrocontroller-spezifische Defines für Hardware-Features
4. **Standards**: Kompatible C/C++ Versionen für Arduino
   - C11 und C++11 für maximale Kompatibilität

## Verwendung

Wähle die passende Konfiguration über:
- `Ctrl+Shift+P` > "C/C++: Select a Configuration"
- Oder über die Status-Leiste unten rechts

## Anpassungen

Für andere Boards:
1. Kopiere eine ähnliche Konfiguration
2. Ändere die Pfade entsprechend
3. Aktualisiere die Defines für das Ziel-Board