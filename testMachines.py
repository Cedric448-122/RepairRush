import customtkinter as ctk
from customtkinter import CTkCanvas as Canvas
import threading
from PIL import Image, ImageTk

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
    def __init__(self, root, machines):
        self.root = root
        self.root.title("État des Machines avec Barres Verticales, Images et Réparation")
        self.machines = machines
        self.start_degradation_threads()

    def start_degradation_threads(self):
        for machine in self.machines:
            threading.Thread(target=machine.degrader_etat, daemon=True).start()

# Initialisation des machines
root = ctk.CTk()
root.geometry("1380x250")
machines = [
    Machine(root, "Tour", "Tour", 20000, 5, 3000, 0.21, "images/TourNiveau1.png"),
    Machine(root, "Tour Avancé", "Tour", 25000, 6, 3500, 0.165, "images/TourNiveau2.png"),
    Machine(root, "CNC", "CNC", 30000, 7, 4000, 0.135, "images/CNCNiveau1.png"),
    Machine(root, "CNC Avancée", "CNC", 35000, 9, 4500, 0.12, "images/CNCNiveau2.png"),
    Machine(root, "Bras Robot", "Bras Robot", 15000, 4, 2000, 0.1, "images/RobotNiveau1.png"),
    Machine(root, "Bras Robot Avancé", "Bras Robot", 23000, 5, 2500, 0.084, "images/RobotNiv2.png")
]


# Lancer l'interface
interface = InterfaceGraphique(root, machines)
root.mainloop()