import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from countOperation import nbOperation  # Importer la fonction de comptage des opérations
def parcourir_fichier():
    chemin_fichier = filedialog.askopenfilename(filetypes=[("Tous les fichiers texte", "*.txt")])
    if chemin_fichier:
        entree_chemin_fichier.delete(0, tk.END)
        entree_chemin_fichier.insert(0, chemin_fichier)

def lire_fichier_entree(chemin_fichier):
    try:
        with open(chemin_fichier, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        messagebox.showerror("Erreur", "Fichier non trouvé.")
        return None

# Fonction pour analyser le code à partir d'un fichier
def analyser_code_fichier():
    chemin_fichier = entree_chemin_fichier.get()
    if not chemin_fichier:
        messagebox.showwarning("Attention", "Veuillez sélectionner un fichier.")
        return

    try:
        nombre_operations = nbOperation(chemin_fichier)
        messagebox.showinfo("Résultat", f"Le nombre d'opérations dans le pseudo-code est : {nombre_operations}")
    except ValueError as e:
        messagebox.showerror("Erreur", str(e))

# Fonction pour analyser le code saisi manuellement
def analyser_code_texte():
    texte_code = texte_algorithme.get("1.0", tk.END).strip()
    if not texte_code:
        messagebox.showwarning("Attention", "Veuillez saisir du code.")
        return

    with open("temp_code.txt", 'w') as temp_file:
        temp_file.write(texte_code)

    try:
        nombre_operations = nbOperation("temp_code.txt")
        messagebox.showinfo("Résultat", f"Le nombre d'opérations dans le pseudo-code est : {nombre_operations}")
    except ValueError as e:
        messagebox.showerror("Erreur", str(e))

# Fonction pour réinitialiser les champs de texte
def reinitialiser_champs():
    entree_chemin_fichier.delete(0, tk.END)
    texte_algorithme.delete("1.0", tk.END)

# Fonction pour quitter l'application avec confirmation
def quitter_application():
    reponse = messagebox.askyesno("Quitter", "Voulez-vous vraiment quitter?")
    if reponse:
        root.quit()

# Configuration de l'interface utilisateur
root = tk.Tk()
root.title("Compteur d'Opérations de Pseudo-Code")
root.geometry("900x600")

# Charger l'image d'arrière-plan
image_path = r"D:\Serge\Express ING2\ING2-2023-2024\COMPLEXITE\TP-complexite\images\tm-astro-bg.jpg"
bg_image = Image.open(image_path)
bg_image = bg_image.resize((800, 500), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Créer un canvas pour afficher l'image d'arrière-plan
canvas = tk.Canvas(root, width=800, height=500)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Créer un frame pour les widgets
frame = ttk.Frame(canvas, padding="10")
frame.place(relwidth=1, relheight=1)

# Définir une taille de police commune pour les boutons
button_font = ("Helvetica", 12)

# Section pour l'analyse de fichier
label_chemin_fichier = ttk.Label(frame, text="Sélectionner le fichier de pseudo-code :", font=("Helvetica", 14), foreground="blue")
label_chemin_fichier.grid(row=0, column=0, padx=10, pady=10)

entree_chemin_fichier = ttk.Entry(frame, width=50)
entree_chemin_fichier.grid(row=0, column=1, padx=10, pady=10)

btn_parcourir = tk.Button(frame, text="Parcourir", command=parcourir_fichier, bg="lightgray", font=button_font)
btn_parcourir.grid(row=0, column=2, padx=10, pady=10)

btn_analyser_fichier = tk.Button(frame, text="ANALYSER LE FICHIER", command=analyser_code_fichier, bg="lightgreen", font=button_font)
btn_analyser_fichier.grid(row=1, column=0, columnspan=3, pady=10)

# Section pour l'analyse de texte saisi manuellement
label_texte_algorithme = ttk.Label(frame, text="Ou SAISIR VOTRE ALGORITHME ICI :", font=("Helvetica", 14))
label_texte_algorithme.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

texte_algorithme = tk.Text(frame, width=80, height=20)
texte_algorithme.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

btn_analyser_texte = tk.Button(frame, text="ANALYSER L'ALGO", command=analyser_code_texte, bg="lightgreen", font=button_font)
btn_analyser_texte.grid(row=4, column=0, columnspan=1, pady=10)

# Boutons Réinitialiser et Quitter
btn_reinitialiser = tk.Button(frame, text="Réinitialiser", command=reinitialiser_champs, bg="lightblue", font=button_font)
btn_reinitialiser.grid(row=4, column=1, padx=10, pady=10)

btn_quitter = tk.Button(frame, text="Quitter", command=quitter_application, bg="red", font=button_font)
btn_quitter.grid(row=4, column=2, padx=10, pady=10)

root.mainloop()
