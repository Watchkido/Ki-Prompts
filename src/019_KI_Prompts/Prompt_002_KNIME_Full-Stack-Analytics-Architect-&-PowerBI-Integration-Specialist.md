--------------------------------------------------EINFACH------------------------------------------------------


Du bist ein KNIME Full-Stack Analytics Architect & PowerBI Integration Specialist. Ich beginne ein neues Datenanalyse-Projekt in KNIME. Mein Ziel ist [DEIN ZIEL]. 
Die Daten die ich habe sind [KURZE DATENBESCHREIBUNG]. 
Kannst du mir einen step-by-step Plan für den kompletten KNIME Workflow geben, 
beginnend mit dem Datenimport bis zur finalen Visualisierung?

------------------------------------------------AUSFÜHRLICH----------------------------------------------------------

# ROLLE
Du bist ein "KNIME Enterprise Analytics Architect & PowerBI Integration Specialist" mit umfassender Expertise in allen KNIME-Erweiterungen und Enterprise-Data-Pipelines.

# AUFGABE
Erstelle einen vollständigen, importierbaren KNIME Workflow für den kompletten Datenanalyse-Prozess bis zur PowerBI-Präsentation mit vollständiger tabellarischer Dokumentation aller Node-Einstellungen.

# PROZESSABLAUF
## 1. UMFASSENDE DATEN-ERFASSUNG
**Systematische Abfrage aller benötigten Informationen:**

**A. DATENQUELLE & STRUKTUR**
- Primäre Datenquelle (Datenbank, CSV, Excel, API, Web, etc.)
- Datenformat, Schema und Beispieldaten
- Datenvolumen und Update-Frequenz
- Datenqualitäts-Status (fehlende Werte, Duplikate, Inkonsistenzen)

**B. ANALYSE-ZIELE**
- Konkrete Business-Fragen die beantwortet werden sollen
- Gewünschte Kennzahlen und Metriken
- Zielgruppe der Analyse-Ergebnisse
- Entscheidungen die auf Basis der Analyse getroffen werden

**C. KNIME ERWEITERUNGEN**
Basierend auf den Anforderungen schlage ich spezifische Erweiterungen vor:
- **KNIME Open Source**: DL4J, H2O, Spark, Python/R Integration
- **KNIME Labs**: Aktuelle experimentelle Features
- **Trusted Community**: Chemoinformatik, Bildverarbeitung, etc.
- **Partner Extensions**: Kommerzielle Lösungen wenn benötigt

**D. POWERBI-SPEZIFIKATIONEN**
- Berichtstyp und Visualisierungen
- Dataset-Typ (Push-Datasets für KNIME Integration)
- Workspace-Konfiguration und Authentifizierung
- Multi-Tabelle Relationships

## 2. WORKFLOW-ARCHITEKTUR
[Project Name] - [Business Purpose]
│
├── 1. DATA EXTRACTION LAYER
│ ├── Source Connectivity Nodes
│ ├── Initial Metadata Capture
│ └── Data Quality Assessment
│
├── 2. DATA PROCESSING LAYER
│ ├── Data Cleaning & Validation
│ ├── Transformation & Enrichment
│ └── Data Quality Metrics Calculation
│
├── 3. ANALYSIS & MODELING LAYER
│ ├── Statistical Analysis
│ ├── Machine Learning Models
│ └── Business Metrics Calculation
│
├── 4. POWERBI EXPORT LAYER
│ ├── Data Model Optimization
│ ├── Push Dataset Configuration
│ └── Authentication Setup
│
├── 5. MONITORING & LOGGING
│ ├── Error Handling Workflow
│ ├── Performance Metrics
│ └── Data Lineage Documentation
│
└── METADATA & DOCUMENTATION
├── Workflow Annotation
├── Node Configuration Docs
└── Deployment Instructions


## 3. DETAILIERTE DOKUMENTATION

**FÜR JEDE NODE:**
[Node Name] - [Node Type]
EINSTELLUNGEN:
• Konkrete Parameter: [Wert]
• Konfiguration: [Schritt-für-Schritt]
• Alternativen: [Ähnliche Nodes]

FUNKTION:
• [Spezifische Aufgabe]
• [Input/Output Beschreibung]

BEST PRACTICES:
• Performance Optimierungen
• Fehlerbehandlung
• Skalierungsempfehlungen

DATA LINEAGE:
• Datenherkunft
• Transformationseffekt
• Output-Metadaten


## 4. SPEZIFISCHE IMPLEMENTIERUNGEN

**DATA QUALITY METRICS:**
- Automatische Validierungsregeln
- Data Quality Scoring
- Exception Reporting

**ERROR HANDLING:**
- Try-Catch Error Handling
- Comprehensive Logging
- Alert Mechanisms

**PERFORMANCE OPTIMIZATION:**
- Chunk Processing für große Datenmengen
- Memory Management
- Parallel Processing wo möglich

**POWERBI INTEGRATION:**
- Push Dataset Configuration
- Multi-Table Relationship Setup
- Secure Authentication Pattern
- Dataset Update Strategy

## 5. AUSGABE-FORMAT

**WORKFLOW EXPORT:**
- Vollständiger KNIME Workflow
- Metadaten und Annotations
- Konfigurierte Node-Einstellungen

**BEGLEITDOKUMENTATION:**
- Installationsanleitung für Erweiterungen
- Deployment Guide
- Troubleshooting Handbook
- Performance Monitoring Guide

# STARTFRAGE
**Bitte beschreiben Sie Ihr konkretes Datenanalyse-Vorhaben mit:**
1. Datenquelle und ersten Beispielen
2. Hauptziel der Analyse
3. Gewünschten Visualisierungen in PowerBI
4. Besonderen Anforderungen an Datenqualität

Ich erstelle darauf basierend einen komplett dokumentierten, produktionsreifen KNIME Workflow.


---------------------------------------------WORKFLOWESTELLUNG---------------------------------------------------------------------


Ich möchte einen kompletten Data Science Workflow in KNIME erstellen für: [GESAMTPROJEKT BESCHREIBUNG].

Von der Datenbeschaffung bis zur Visualisierung sollen alle Schritte abgedeckt werden:

Bitte designe einen modularen KNIME Workflow mit:
1. Klarer Projektstruktur
2. Wiederverwendbaren Komponenten
3. Fehlerbehandlung und Logging
4. Performance-Optimierung
5. Dokumentation des gesamten Prozesses

------------------------------------------DATENBESCHASFFUNG---------------------------------------------------------------

Ich möchte Daten in KNIME importieren. Mein Use Case ist: [DEIN USE CASE, z.B. "Kundenanalyse für E-Commerce"]. 

Die Datenquellen die ich verwenden möchte sind:
- [z.B. CSV/Excel-Dateien, SQL-Datenbank, Web-API, etc.]
- Besondere Herausforderungen: [z.B. große Datenmengen, unstrukturierte Daten, API-Limits]

Bitte erstelle mir einen Schritt-für-Schritt-Plan für:
1. Optimalen Datenimport in KNIME
2. Konfiguration der Reader-Nodes
3. Erste Datenexploration zur Qualitätskontrolle
4. Handling von speziellen Datenformaten



------------------------------------------DATENBEREINIGUNG---------------------------------------------------------------
Ich habe meine Daten in KNIME importiert. Jetzt benötige ich einen umfassenden Datenbereinigungs-Workflow.

Meine Daten haben folgende Qualitätsprobleme:
- Fehlende Werte in Spalten: [Spaltennamen nennen]
- Inkonsistente Formate: [z.B. Datumsformate, Währungen]
- Duplikate und Ausreißer
- Nicht-normalisierte Kategorien

Bitte designe mir einen KNIME-Workflow mit:
1. Metadaten-Exploration zu Beginn
2. Spezifischen Nodes für jede Bereinigungsaufgabe
3. Daten-Profiling nach jedem Schritt
4. Dokumentation der Veränderungen
------------------------------------------FEATUREENGENEERING---------------------------------------------------------------
Ich benötige Hilfe bei Feature Engineering in KNIME für mein Projekt: [PROJEKTBESCHREIBUNG].

Aktuelle Datenstruktur:
- Numerische Spalten: [auflisten]
- Kategorische Spalten: [auflisten]
- Zeitreihen-Daten: [falls vorhanden]

Ziele für Feature Engineering:
- Erstellung neuer aussagekräftiger Features
- Behandlung kategorischer Variablen (One-Hot Encoding, Label Encoding)
- Skalierung und Normalisierung
- Zeitbasierte Feature-Extraktion

Bitte zeige mir den optimalen KNIME-Workflow mit:
1. Automatischer Feature-Erkennung
2. Bewährten Transformationstechniken
3. Feature-Selektion zur Vermeidung von Overfitting


-------------------------------------------MASCHINELEARNING---------------------------------------------------------------
Ich möchte Machine Learning Modelle in KNIME für [KLASSIFIKATION/REGRESSION/CLUSTERING] aufbauen.

Datenkontext: [Beschreibe deine Zielvariable und Features]

Anforderungen:
- Vergleich mehrerer Algorithmen
- Hyperparameter-Tuning
- Kreuzvalidierung
- Modellinterpretation

Bitte erstelle einen ML-Workflow in KNIME mit:
1. Datenaufteilung (Train/Test/Validation)
2. Mehrere Modell-Typen im Vergleich
3. Automatisches Hyperparameter-Tuning
4. Modell-Evaluation Metriken
5. Feature Importance Analyse

-------------------------------------------MODELL-DEPLOYMENT---------------------------------------------------------------
Ich habe ein trainiertes Modell in KNIME und möchte es produktiv setzen.

Anwendungsfall: [z.B. Batch-Prognose, Echtzeit-Vorhersage]

Bitte zeige mir den KNIME-Workflow für:
1. Modell-Serialisierung und Speicherung
2. Erstellung eines Prognose-Workflows
3. Integration in bestehende Prozesse
4. Monitoring der Modellperformance over time
5. Retraining-Strategie
-------------------------------------------POWERBI-INTEGRATION---------------------------------------------------------------
Ich möchte meine KNIME Analyseergebnisse in PowerBI visualisieren.

Daten: [Beschreibe die zu exportierenden Daten]
Visualisierungsziele: [z.B. Dashboard, interaktive Reports]

Bitte designe einen KNIME zu PowerBI Workflow mit:
1. Optimalem Datenexport-Format für PowerBI
2. Datenstruktur-Optimierung für PowerBI
3. Automatisierter Refresh-Mechanismus
4. Best Practices für die Übergabe

-------------------------------------------Excel-Integration---------------------------------------------------------------
Ich benötige einen KNIME Workflow zur Automatisierung von Excel-Reports.

Aktuelle Excel-Struktur: [beschreiben]
Gewünschte Outputs: [z.B. pivotierte Tabellen, formatierte Reports]

Bitte zeige mir:
1. KNIME Nodes für Excel-Export
2. Automatisierte Formatierung
3. Handling großer Datensätze
4. Update-Strategien für bestehende Excel-Dateien

--
-------------------------------------------PYTHON-INTEGRATION---------------------------------------------------------------
Ich möchte Python-Code in meinen KNIME Workflow integrieren.

Use Case: [Spezifische Python-Funktionalität die benötigt wird]
Bestehender Python-Code: [falls vorhanden]

Bitte erkläre mir:
1. Python Node Konfiguration in KNIME
2. Datenübergabe zwischen KNIME und Python
3. Handling von Python-Umgebungen
4. Best Practices für die Integration
-------------------------------------------REPORTING-&-DASHBOARDS-------------------------------------------------------------
Ich möchte ein umfassendes Reporting- und Dashboard-System in KNIME erstellen.

Anwendungsfall: [Beschreibe den spezifischen Reporting- oder Dashboard-Bedarf, z. B. "Monatliche Verkaufsberichte für das Management"]

Daten: [Beschreibe die Daten, die für das Reporting verwendet werden sollen, z. B. "Aggregierte Verkaufsdaten aus verschiedenen Regionen"]

Ziele:
- Erstellung interaktiver Dashboards
- Automatisierte Berichterstellung
- Integration von Echtzeit-Daten (falls erforderlich)
- Anpassung der Berichte an verschiedene Zielgruppen

Bitte designe einen KNIME-Workflow für Reporting und Dashboards mit:
1. Datenaggregation und -bereinigung für Berichte
2. Erstellung von Visualisierungen (z. B. Diagramme, Tabellen)
3. Automatisierte Generierung von Berichten (z. B. PDF, Excel)
4. Integration von Dashboards in bestehende Systeme
5. Best Practices für die Gestaltung und Performance-Optimierung

-------------------------------------------PRÄSENTATION-DER-ERGEBNISSE-------------------------------------------------
Ich möchte die Ergebnisse meiner Datenanalyse in einer klaren und überzeugenden Weise präsentieren.

Anwendungsfall: [Beschreibe den spezifischen Präsentationsbedarf, z. B. "Präsentation der Verkaufsanalyse für das Management"]

Ziele:
- Erstellung einer klaren und strukturierten Präsentation
- Hervorhebung der wichtigsten Erkenntnisse
- Verwendung von Visualisierungen zur Unterstützung der Ergebnisse
- Anpassung der Präsentation an die Zielgruppe

Bitte designe einen KNIME-Workflow für die Präsentation der Ergebnisse mit:
1. Auswahl und Aufbereitung der wichtigsten Analyseergebnisse
2. Erstellung von Visualisierungen (z. B. Diagramme, Heatmaps, Tabellen)
3. Export der Ergebnisse in Präsentationsformate (z. B. PowerPoint, PDF)
4. Integration von interaktiven Dashboards (falls erforderlich)
5. Best Practices für die Gestaltung und Strukturierung der Präsentation

---------------------------------------------WORKFLOWESTELLUNG---------------------------------------------------------------------

Ich möchte einen kompletten Data Science Workflow in KNIME erstellen für: [GESAMTPROJEKT BESCHREIBUNG].

Von der Datenbeschaffung bis zur Visualisierung sollen alle Schritte abgedeckt werden:

Bitte designe einen modularen KNIME Workflow mit:

Klarer Projektstruktur
Wiederverwendbaren Komponenten
Fehlerbehandlung und Logging
Performance-Optimierung
Dokumentation des gesamten Prozesses

------------------------------------------DATENBESCHASFFUNG---------------------------------------------------------------

Ich möchte Daten in KNIME importieren. Mein Use Case ist: [DEIN USE CASE, z.B. "Kundenanalyse für E-Commerce"].

Die Datenquellen die ich verwenden möchte sind:

[z.B. CSV/Excel-Dateien, SQL-Datenbank, Web-API, etc.]

Besondere Herausforderungen: [z.B. große Datenmengen, unstrukturierte Daten, API-Limits]

Bitte erstelle mir einen Schritt-für-Schritt-Plan für:

Optimalen Datenimport in KNIME
Konfiguration der Reader-Nodes
Erste Datenexploration zur Qualitätskontrolle
Handling von speziellen Datenformaten

------------------------------------------DATENINTEGRATION---------------------------------------------------------------

Ich möchte Daten aus mehreren Quellen in KNIME integrieren.

Meine Datenquellen sind:

[Liste der verschiedenen Datenquellen: z.B. SQL-Datenbank, CSV-Dateien, REST-API, Excel]

Besondere Anforderungen: [z.B. unterschiedliche Update-Zyklen, verschiedene Datenformate]

Bitte erstelle mir einen KNIME-Workflow für:

Verbindung zu verschiedenen Datenquellen
Daten-Merging und Joins
API-Integration und Handling von API-Limits
Konsistente Datenstruktur über alle Quellen hinweg
Dokumentation der Datenherkunft und Transformationen

------------------------------------------DATENVALIDIERUNG---------------------------------------------------------------

Ich benötige einen umfassenden Datenvalidierungs-Workflow in KNIME.

Meine Daten haben folgende Validierungsanforderungen:

[Spezifische Geschäftsregeln: z.B. "Alter muss zwischen 18 und 100 liegen"]

[Datenintegritätsregeln: z.B. "Kunden-ID muss eindeutig sein"]

[Formatvalidierung: z.B. "E-Mail muss gültiges Format haben"]

Bitte designe einen KNIME-Workflow mit:

Definition von Validierungsregeln
Automatische Prüfung auf Regelverletzungen
Reporting von Validierungsfehlern
Fehlerbehandlungsstrategien
Data Quality Score Berechnung

------------------------------------------EXPLORATIVE DATENANALYSE (EDA)---------------------------------------------------------------

Ich möchte eine umfassende explorative Datenanalyse in KNIME durchführen.

Analyseziele:

[Spezifische Fragen: z.B. "Verteilung der Altersgruppen erkennen", "Zusammenhang zwischen Umsatz und Region finden"]

Besondere Schwerpunkte: [z.B. Ausreißererkennung, Korrelationsanalyse]

Bitte erstelle einen KNIME-EDA-Workflow mit:

Deskriptive Statistiken für alle Variablen
Visualisierungen (Histogramme, Boxplots, Scatterplots)
Korrelationsanalyse und Heatmaps
Ausreißererkennung und -dokumentation
Automatischer EDA-Report Generierung

------------------------------------------FEATURESELECTION---------------------------------------------------------------

Ich benötige Hilfe bei der Feature Selection in KNIME für mein Projekt: [PROJEKTBESCHREIBUNG].

Aktuelle Datenstruktur:

Anzahl der Features: [Anzahl]

Feature-Typen: [numerisch/kategorisch/zeitbasiert]

Ziele der Feature Selection:

[Spezifische Ziele: z.B. "Reduzierung auf 10 wichtigste Features", "Eliminierung hochkorrelierter Variablen"]

Bitte zeige mir den optimalen KNIME-Workflow für:

Korrelationsanalyse zwischen Features
PCA zur Dimensionsreduktion
Automatisierte Feature-Auswahl-Algorithmen
Feature Importance Bewertung
Visualisierung der Feature-Relevanz

------------------------------------------MODELLINTERPRETATION---------------------------------------------------------------

Ich möchte meine Machine Learning Modelle in KNIME interpretieren und erklären.

Modelltyp: [z.B. Random Forest, Neuronales Netzwerk, lineare Regression]
Interpretationsbedarf:

[Spezifische Anforderungen: z.B. "Erklärung einzelner Vorhersagen", "globale Modellinterpretation"]

Bitte erstelle einen KNIME-Workflow für:

Feature Importance Analyse
SHAP-Werte Berechnung
Partial Dependence Plots
Modell-Erklärungen für Business-Stakeholder
Visualisierung der Modellentscheidungen

------------------------------------------DATENEXPORT UND -BEREITSTELLUNG---------------------------------------------------------------

Ich möchte meine Analyseergebnisse aus KNIME exportieren und bereitstellen.

Zielsysteme: [z.B. PowerBI, Datenbank, CSV für Excel, Web-Dashboard]
Anforderungen:

[Spezifische Formate: z.B. "täglicher Export als CSV", "Echtzeit-Update der Datenbank"]

Bitte designe einen KNIME-Export-Workflow mit:

Datenexport in verschiedene Formate (CSV, Excel, Datenbank)
Optimierung der Datenstruktur für Zielsysteme

3 Automatisierte Export-Prozesse
Qualitätssicherung der exportierten Daten
Dokumentation der Export-Prozesse

------------------------------------------AUTOMATISIERUNG UND DEPLOYMENT---------------------------------------------------------------

Ich möchte meinen KNIME-Workflow automatisieren und in einer Produktivumgebung deployen.

Umgebungsanforderungen:

[Spezifische Umgebung: z.B. "KNIME Server", "Cloud-Umgebung"]

Scheduling-Anforderungen: [z.B. "täglich um 6:00 Uhr", "bei Datenupdate"]

Bitte erstelle einen Deployment-Workflow mit:

KNIME Server Integration
Workflow-Scheduling und -Monitoring
Error Handling und Benachrichtigungen
Performance-Optimierung für Produktivbetrieb
Deployment-Dokumentation und Rollback-Strategien

------------------------------------------FEEDBACK-LOOP UND ITERATION---------------------------------------------------------------

Ich benötige einen systematischen Feedback-Loop für meinen KNIME-Analyse-Workflow.

Iterationsanforderungen:

[Spezifische Feedback-Quellen: z.B. "neue Daten monatlich", "User-Feedback aus PowerBI"]

Änderungsmanagement: [z.B. "Versionierung der Workflows", "Dokumentation von Anpassungen"]

Bitte designe einen KNIME-Workflow mit:

Mechanismen für kontinuierliche Verbesserung
Versionierung von Workflows und Modellen
Dokumentation von Änderungen und Anpassungen
Monitoring der Modellperformance over time
Automatisches Retraining bei Performance-Degradation

------------------------------------------DATENBEREINIGUNG---------------------------------------------------------------
Ich habe meine Daten in KNIME importiert. Jetzt benötige ich einen umfassenden Datenbereinigungs-Workflow.

Meine Daten haben folgende Qualitätsprobleme:

Fehlende Werte in Spalten: [Spaltennamen nennen]

Inkonsistente Formate: [z.B. Datumsformate, Währungen]

Duplikate und Ausreißer
Nicht-normalisierte Kategorien

Bitte designe mir einen KNIME-Workflow mit:

Metadaten-Exploration zu Beginn
Spezifischen Nodes für jede Bereinigungsaufgabe
Daten-Profiling nach jedem Schritt
Dokumentation der Veränderungen

------------------------------------------FEATUREENGINEERING---------------------------------------------------------------
Ich benötige Hilfe bei Feature Engineering in KNIME für mein Projekt: [PROJEKTBESCHREIBUNG].

Aktuelle Datenstruktur:
Numerische Spalten: [auflisten]
Kategorische Spalten: [auflisten]
Zeitreihen-Daten: [falls vorhanden]
Ziele für Feature Engineering:

Erstellung neuer aussagekräftiger Features
Behandlung kategorischer Variablen (One-Hot Encoding, Label Encoding)
Skalierung und Normalisierung
Zeitbasierte Feature-Extraktion

Bitte zeige mir den optimalen KNIME-Workflow mit:

Automatischer Feature-Erkennung
Bewährten Transformationstechniken
Feature-Selektion zur Vermeidung von Overfitting

-------------------------------------------MASCHINELLEARNING---------------------------------------------------------------
Ich möchte Machine Learning Modelle in KNIME für [KLASSIFIKATION/REGRESSION/CLUSTERING] aufbauen.

Datenkontext: [Beschreibe deine Zielvariable und Features]

Anforderungen:

Vergleich mehrerer Algorithmen
Hyperparameter-Tuning
Kreuzvalidierung
Modellinterpretation

Bitte erstelle einen ML-Workflow in KNIME mit:

Datenaufteilung (Train/Test/Validation)
Mehrere Modell-Typen im Vergleich
Automatisches Hyperparameter-Tuning
Modell-Evaluation Metriken
Feature Importance Analyse

-------------------------------------------MODELL-DEPLOYMENT---------------------------------------------------------------
Ich habe ein trainiertes Modell in KNIME und möchte es produktiv setzen.

Anwendungsfall: [z.B. Batch-Prognose, Echtzeit-Vorhersage]

Bitte zeige mir den KNIME-Workflow für:

Modell-Serialisierung und Speicherung
Erstellung eines Prognose-Workflows
Integration in bestehende Prozesse
Monitoring der Modellperformance over time
Retraining-Strategie

-------------------------------------------POWERBI-INTEGRATION---------------------------------------------------------------
Ich möchte meine KNIME Analyseergebnisse in PowerBI visualisieren.

Daten: [Beschreibe die zu exportierenden Daten]
Visualisierungsziele: [z.B. Dashboard, interaktive Reports]

Bitte designe einen KNIME zu PowerBI Workflow mit:

Optimalem Datenexport-Format für PowerBI
Datenstruktur-Optimierung für PowerBI
Automatisierter Refresh-Mechanismus
Best Practices für die Übergabe

-------------------------------------------EXCEL-INTEGRATION---------------------------------------------------------------
Ich benötige einen KNIME Workflow zur Automatisierung von Excel-Reports.

Aktuelle Excel-Struktur: [beschreiben]
Gewünschte Outputs: [z.B. pivotierte Tabellen, formatierte Reports]

Bitte zeige mir:

KNIME Nodes für Excel-Export
Automatisierte Formatierung
Handling großer Datensätze
Update-Strategien für bestehende Excel-Dateien

-------------------------------------------PYTHON-INTEGRATION---------------------------------------------------------------
Ich möchte Python-Code in meinen KNIME Workflow integrieren.

Use Case: [Spezifische Python-Funktionalität die benötigt wird]
Bestehender Python-Code: [falls vorhanden]

Bitte erkläre mir:

Python Node Konfiguration in KNIME
Datenübergabe zwischen KNIME und Python
Handling von Python-Umgebungen
Best Practices für die Integration

-------------------------------------------REPORTING-&-DASHBOARDS-------------------------------------------------------------
Ich möchte ein umfassendes Reporting- und Dashboard-System in KNIME erstellen.

Anwendungsfall: [Beschreibe den spezifischen Reporting- oder Dashboard-Bedarf, z. B. "Monatliche Verkaufsberichte für das Management"]

Daten: [Beschreibe die Daten, die für das Reporting verwendet werden sollen, z. B. "Aggregierte Verkaufsdaten aus verschiedenen Regionen"]

Ziele:

Erstellung interaktiver Dashboards
Automatisierte Berichterstellung
Integration von Echtzeit-Daten (falls erforderlich)
Anpassung der Berichte an verschiedene Zielgruppen

Bitte designe einen KNIME-Workflow für Reporting und Dashboards mit:

Datenaggregation und -bereinigung für Berichte
Erstellung von Visualisierungen (z. B. Diagramme, Tabellen)
Automatisierte Generierung von Berichten (z. B. PDF, Excel)
Integration von Dashboards in bestehende Systeme
Best Practices für die Gestaltung und Performance-Optimierung

-------------------------------------------PRÄSENTATION-DER-ERGEBNISSE-------------------------------------------------
Ich möchte die Ergebnisse meiner Datenanalyse in einer klaren und überzeugenden Weise präsentieren.

Anwendungsfall: [Beschreibe den spezifischen Präsentationsbedarf, z. B. "Präsentation der Verkaufsanalyse für das Management"]

Ziele:

Erstellung einer klaren und strukturierten Präsentation
Hervorhebung der wichtigsten Erkenntnisse
Verwendung von Visualisierungen zur Unterstützung der Ergebnisse
Anpassung der Präsentation an die Zielgruppe

Bitte designe einen KNIME-Workflow für die Präsentation der Ergebnisse mit:

Auswahl und Aufbereitung der wichtigsten Analyseergebnisse
Erstellung von Visualisierungen (z. B. Diagramme, Heatmaps, Tabellen)
Export der Ergebnisse in Präsentationsformate (z. B. PowerPoint, PDF)
Integration von interaktiven Dashboards (falls erforderlich)
Best Practices für die Gestaltung und Strukturierung der Präsentation
