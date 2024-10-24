import random

class Machine:
    def __init__(self, nom, type_machine, cout_achat, temps_entretien, revenu_par_periode):
        self.nom = nom
        self.type_machine = type_machine
        self.cout_achat = cout_achat
        self.temps_entretien = temps_entretien
        self.revenu_par_periode = revenu_par_periode
        self.etat = 100  # L'état initial de la machine est à 100%
        
    def afficher_details(self):
        print(f"Nom: {self.nom}")
        print(f"Type: {self.type_machine}")
        print(f"Coût d'achat: {self.cout_achat}")
        print(f"Temps d'entretien: {self.temps_entretien}")
        print(f"Revenu par période: {self.revenu_par_periode}")
        print(f"État: {self.barre_etat()}")
    
    def barre_etat(self):
        if self.etat >= 70:
            return f"Vert ({self.etat}%)"
        elif 30 <= self.etat < 70:
            return f"Jaune ({self.etat}%)"
        else:
            return f"Rouge ({self.etat}%)"
    
    def degrader_etat(self):
        # Simule la dégradation de l'état de la machine avec le temps (perte de 10 à 30%)
        degradation = random.randint(10, 30)
        self.etat = max(0, self.etat - degradation)
    
    def entretenir(self):
        # Remet l'état de la machine à 100%
        print(f"Entretien de la machine {self.nom} en cours...")
        self.etat = 100
        print(f"Machine {self.nom} entretenue. État: {self.barre_etat()}")
        

class Tour(Machine):
    def __init__(self, nom):
        super().__init__(nom, "Tour", cout_achat=20000, temps_entretien=5, revenu_par_periode=3000)


class Fraiseuse(Machine):
    def __init__(self, nom):
        super().__init__(nom, "Fraiseuse", cout_achat=30000, temps_entretien=7, revenu_par_periode=4000)


class Perceuse(Machine):
    def __init__(self, nom):
        super().__init__(nom, "Perceuse", cout_achat=15000, temps_entretien=4, revenu_par_periode=2000)


def afficher_machines(liste_machines):
    print("Liste des machines disponibles :\n")
    for machine in liste_machines:
        machine.afficher_details()
        print("-" * 30)


def effectuer_entretien(liste_machines):
    for machine in liste_machines:
        if machine.etat < 50:  # Entretien uniquement si l'état est en jaune ou rouge
            machine.entretenir()

# Création des machines
machines = [
    Tour("Tour"),
    Tour("Tour Avancé"),
    Fraiseuse("Fraiseuse"),
    Fraiseuse("Fraiseuse Avancée"),
    Perceuse("Perceuse"),
    Perceuse("Perceuse Avancée")
]

# Améliorations spécifiques des machines
machines[1].cout_achat = 25000      # TourAvancé
machines[1].temps_entretien = 6
machines[1].revenu_par_periode = 3500

machines[3].cout_achat = 35000      # FraiseuseAvancée
machines[3].temps_entretien = 9
machines[3].revenu_par_periode = 4500

machines[5].cout_achat = 23000      # PerceuseAvancée
machines[5].temps_entretien = 5
machines[5].revenu_par_periode = 2500

# Simulation de l'utilisation des machines
afficher_machines(machines)

# Dégrader l'état des machines après plusieurs périodes
for _ in range(3):
    for machine in machines:
        machine.degrader_etat()

print("\n--- Après dégradation ---\n")
afficher_machines(machines)

# Effectuer l'entretien des machines dont l'état est bas
print("\n--- Entretien des machines ---\n")
effectuer_entretien(machines)

# Réaffichage des machines après entretien
print("\n--- Après entretien ---\n")
afficher_machines(machines)
