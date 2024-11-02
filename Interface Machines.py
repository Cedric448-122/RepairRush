import customtkinter as ctk
from customtkinter import CTkCanvas as Canvas
import threading
from PIL import Image, ImageTk
from machines_data import machines_data

# Configuration de l'interface graphique
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Machine:
    def __init__(self, root, nom, type_machine, cout_achat, temps_entretien, revenu_par_periode, deplet_rate, image_path):
        self.nom = nom
        self.type_machine = type_machine
        self.cout_achat = cout_achat
        self.temps_entretien = temps_entretien
        self.revenu_par_periode = revenu_par_periode
        self.deplet_rate = deplet_rate
        self.etat = 100  # État initial à 100%

        # Création de l'interface de la machine
        self.frame = ctk.CTkFrame(root, width=200, height=300, corner_radius=10)
        self.frame.pack(pady=10, padx=10, side="left")

        self.label_nom = ctk.CTkLabel(self.frame, text=f"{self.nom} ({self.type_machine})", font=("Arial", 12))
        self.label_nom.pack(pady=5)

        # Conteneur pour l'image et la barre d'état
        self.image_et_barre_frame = ctk.CTkFrame(self.frame, width=150, height=150)
        self.image_et_barre_frame.pack()

        # Chargement de l'image de la machine
        image = Image.open(image_path).resize((150, 150))
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
        while self.etat > 0:
            self.etat = max(0, self.etat - self.deplet_rate)
            self.update_barre()
            threading.Event().wait(1)

    def update_barre(self):
        self.canvas.delete("barre")
        height = int(self.canvas.winfo_height() * (self.etat / 100))
        y_position = self.canvas.winfo_height() - height
        color = self.get_color_for_etat()

        if self.etat > 0:
            self.canvas.create_rectangle(1, y_position, 33, self.canvas.winfo_height(), fill=color, tags="barre")

    def get_color_for_etat(self):
        if self.etat >= 60:
            return "green"
        elif 20 <= self.etat < 60:
            return "yellow"
        else:
            return "red"

    def reparer(self):
        self.etat = 100
        self.update_barre()

class InterfaceGraphique:
    def __init__(self, root, machines_data):
        self.root = root
        self.root.title("État des Machines avec Barres Verticales, Images et Réparation")
        self.machines = [Machine(root, **machine) for machine in machines_data]
        self.start_degradation_threads()

    def start_degradation_threads(self):
        for machine in self.machines:
            threading.Thread(target=machine.degrader_etat, daemon=True).start()

# Initialisation des machines
root = ctk.CTk()
root.geometry("1380x250")
interface = InterfaceGraphique(root, machines_data)
root.mainloop()
