import customtkinter as ctk
from tkinter import Canvas

class InterfaceGraphique:
    def __init__(self, root, machines):
        self.root = root
        self.root.title("État des Machines")
        self.machines = machines
        self.create_interface()

    def create_interface(self):
        # Canvas plus grand pour dessiner les machines et les barres d'état
        self.canvas = Canvas(self.root, width=1500, height=800, bg='lightgreen')
        self.canvas.pack()
        self.dessiner_machines()

    def dessiner_machines(self):
        self.canvas.delete("all")  # Effacer les anciens dessins
        x_position = 100  # Position de départ pour la première machine
        machine_width = 100  # Largeur de la machine
        machine_height = 100  # Hauteur de la machine
        barre_width = 20  # Largeur de la barre d'état

        for machine in self.machines:
            # Dessiner une "machine" agrandie (remplace avec une image si nécessaire)
            self.canvas.create_rectangle(x_position, 300, x_position + machine_width, 300 + machine_height, fill="black")
            
            # Créer une barre d'état basée sur l'état de la machine (de bas en haut)
            etat_color = self.get_color_for_etat(machine.etat)
            height = machine.etat  # La hauteur de la barre dépend de l'état (en pourcentage)
            
            # Ajuster la barre d'état pour qu'elle commence à la même hauteur que la machine
            self.canvas.create_rectangle(
                x_position + machine_width + 20, 
                300 + machine_height - height,  # Départ de la barre en bas de la machine
                x_position + machine_width + 20 + barre_width, 
                300 + machine_height,  # La barre remonte vers le haut
                fill=etat_color
            )

            # Mettre à jour la position x pour la prochaine machine avec plus d'espace
            x_position += 200

    def get_color_for_etat(self, etat):
        # Retourne une couleur en fonction de l'état de la machine
        if etat >= 70:
            return "green"
        elif 30 <= etat < 70:
            return "yellow"
        else:
            return "red"

    def mise_a_jour_etats(self):
        # Faire dégrader les machines
        for machine in self.machines:
            machine.degrader_etat()
        self.dessiner_machines()
        self.root.after(750, self.mise_a_jour_etats)  # Mise à jour automatique toutes les 2 secondes


class Machine:
    def __init__(self, nom, etat, pourcentage_degradation):
        self.nom = nom
        self.etat = 100
        self.pourcentage_degradation = pourcentage_degradation

    def degrader_etat(self):
        # Dégradation en fonction du pourcentage défini
        self.etat -= self.etat * (self.pourcentage_degradation / 100)
        if self.etat < 0:
            self.etat = 0  # L'état minimum est 0%


# Création de quelques machines avec différents pourcentages de dégradation
machines = [
    Machine("Tour", 90, 5),           # Dégradation de 5% par période
    Machine("Tour Avancé", 80, 3),    # Machine avancée, dégradation plus lente
    Machine("Fraiseuse", 60, 7),      # Dégradation rapide
    Machine("Fraiseuse Avancée", 40, 4), # Dégradation modérée
    Machine("Perceuse", 20, 6),       # Dégradation rapide
    Machine("Perceuse Avancée", 75, 2),  # Machine avancée, très petite dégradation
]

# Créer l'interface Tkinter
root = ctk.CTk()
interface = InterfaceGraphique(root, machines)

# Dégrader l'état des machines automatiquement toutes les 2 secondes
interface.mise_a_jour_etats()

# Lancer l'interface
root.mainloop()
