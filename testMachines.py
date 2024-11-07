import customtkinter as ctk
from customtkinter import CTkCanvas as Canvas
import threading
from PIL import Image, ImageTk
from machines_data import machines

# J'ai oublié de commit lol 
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Machine:
    def __init__(self, root, machine_data):
        self.nom = machine_data.nom
        self.type_machine = machine_data.type_machine
        self.cout_achat = machine_data.cout_achat
        self.temps_entretien = machine_data.temps_entretien
        self.revenu_par_periode = machine_data.revenu_par_periode
        self.deplet_rate = machine_data.deplet_rate
        self.etat = 100  # État initial à 100%

        # Création de l'interface de la machine
        self.frame = ctk.CTkFrame(root, width=200, height=300, corner_radius=10)
        self.frame.pack(pady=10, padx=10, side="left")

        self.label_nom = ctk.CTkLabel(self.frame, text=f"{self.nom} ({machine_data.niveau_machine})", font=("Arial", 12))
        self.label_nom.pack(pady=5)

        # Conteneur pour l'image et la barre d'état
        self.image_et_barre_frame = ctk.CTkFrame(self.frame, width=150, height=150)
        self.image_et_barre_frame.pack()

        # Chargement de l'image de la machine
        image = Image.open(machine_data.image_path).resize((150, 150))
        self.image = ImageTk.PhotoImage(image)
        self.label_image = ctk.CTkLabel(self.image_et_barre_frame, image=self.image, text="")
        self.label_image.grid(row=0, column=0, padx=5)

        # Canvas pour la barre d'état verticale
        self.canvas = Canvas(self.image_et_barre_frame, width=31, height=150, bg="black")
        self.canvas.grid(row=0, column=1, padx=5)

        # Bouton de réparation
        self.bouton_reparer = ctk.CTkButton(self.frame, text="Réparer", command=self.reparer)
        self.bouton_reparer.pack(pady=10)

        # Initialisation de la barre d'état
        self.update_barre()

    def degrader_etat(self):
        # Dégrade l'état de la machine d'un montant fixe toutes les secondes
        while self.etat > 0:
            self.etat = max(0, self.etat - self.deplet_rate)  # Dégradation par seconde
            self.update_barre()
            threading.Event().wait(1)  # Attendre 1 seconde avant la prochaine dégradation

    def update_barre(self):
        # Effacer la barre précédente pour un rafraîchissement propre
        self.canvas.delete("barre")

        # Déterminer la hauteur de la barre en fonction de l'état de la machine
        height = int(self.canvas.winfo_height() * (self.etat / 100))
        y_position = self.canvas.winfo_height() - height

        # Déterminer la couleur de la barre
        color = self.get_color_for_etat()

        # Dessiner la barre d'état verticale
        if self.etat > 0:
            self.canvas.create_rectangle(1, y_position, 33, self.canvas.winfo_height(), fill=color, tags="barre")

    def get_color_for_etat(self):
        # Choisir la couleur en fonction de l'état
        if self.etat >= 60:
            return "green"
        elif 20 <= self.etat < 60:
            return "yellow"
        else:
            return "red"

    def reparer(self):
        # Remet l'état de la machine à 100% et met à jour la barre
        self.etat = 100
        self.update_barre()

class InterfaceGraphique:
    def __init__(self, frame, machines):
        self.frame = frame
        self.frame.configure(corner_radius=0)
        self.machines = [Machine(self.frame, machine) for machine in machines]
        self.start_degradation_threads()

    def start_degradation_threads(self):
        for machine in self.machines:
            threading.Thread(target=machine.degrader_etat, daemon=True).start()

# Exemple d'utilisation dans un autre fichier
if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("1380x800")

    # Création d'un cadre pour les machines dans l'interface principale
    machines_frame = ctk.CTkFrame(root, width=1380, height=300)
    machines_frame.place(x=0, y=250)

    # Initialiser l'interface des machines dans le cadre
    interface = InterfaceGraphique(machines_frame, machines)

    root.mainloop()
