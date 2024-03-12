import tkinter as tk
from tkinter import messagebox
import subprocess

def commit():
    commit_message = commit_entry.get()
    if commit_message.strip() == "":
        messagebox.showerror("Errore", "Inserisci un messaggio di commit valido.")
    else:
        try:
            subprocess.run(['git', 'add', '.'])
            subprocess.run(['git', 'commit', '-m', commit_message])
            subprocess.run(['git', 'push', 'origin', 'main'])
            messagebox.showinfo("Successo", "Commit eseguito con successo.")
            root.destroy()
        except Exception as e:
            messagebox.showerror("Errore", f"Si è verificato un errore: {str(e)}")

root = tk.Tk()
root.title("Commit GUI")

commit_label = tk.Label(root, text="Inserisci il messaggio di commit:")
commit_label.pack(pady=5)

commit_entry = tk.Entry(root, width=50)
commit_entry.pack(pady=5)

commit_button = tk.Button(root, text="OK", command=commit)
commit_button.pack(pady=5)

root.mainloop()
