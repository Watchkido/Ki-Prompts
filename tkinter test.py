import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime

def copy_and_modify_templates():
    # Quellordner (muss im selben Verzeichnis wie das Skript liegen)
    source_folder = os.path.join(os.path.dirname(__file__), "templates")
    
    # Zielordner auswählen
    dest_folder = filedialog.askdirectory(title="Zielordner auswählen")
    if not dest_folder:
        return
    
    # Projektname eingeben
    project_name = entry.get().strip()
    if not project_name:
        messagebox.showerror("Fehler", "Bitte Projektnamen eingeben!")
        return
    
    # Zielpfad erstellen
    target_path = os.path.join(dest_folder, project_name)
    
    try:
        # Ordner kopieren (inkl. Unterordner)
        shutil.copytree(source_folder, target_path)
        
        # Durch alle Dateien im kopierten Ordner iterieren
        for root, dirs, files in os.walk(target_path):
            for file in files:
                file_path = os.path.join(root, file)
                
                # Nur Textdateien verarbeiten
                if file.endswith(('.txt', '.html', '.css', '.js', '.py')):
                    with open(file_path, 'r+', encoding='utf-8') as f:
                        content = f.read()
                        
                        # Ersetzung nur durchführen, wenn Platzhalter existiert
                        if "{TEXTE}" in content:
                            # Platzhalter ersetzen
                            new_content = content.replace(
                                "{TEXTE}", 
                                f"Dateiname: {file}\nVermerk: Bearbeitet am {datetime.now().strftime('%Y-%m-%d %H:%M')}"
                            )
                            
                            # Zurückschreiben
                            f.seek(0)
                            f.write(new_content)
                            f.truncate()
        
        messagebox.showinfo("Erfolg", f"Projekt '{project_name}' wurde erfolgreich erstellt!\nSpeicherort: {target_path}")
    
    except Exception as e:
        messagebox.showerror("Fehler", f"Ein Fehler ist aufgetreten:\n{str(e)}")

# GUI erstellen
root = tk.Tk()
root.title("Projektgenerator")
root.geometry("400x200")

# Projektname Eingabe
tk.Label(root, text="Projektname:").pack(pady=10)
entry = tk.Entry(root, width=30)
entry.pack()
entry.insert(0, "tag-09")

# Auswahlbutton
tk.Button(
    root, 
    text="Zielordner auswählen und erstellen",
    command=copy_and_modify_templates,
    bg="#4CAF50",
    fg="white"
).pack(pady=20)

root.mainloop()