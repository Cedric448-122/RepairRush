class Machine:
    def __init__(self, nom, niveau_machine, type_machine, cout_achat, temps_entretien, revenu_par_periode, deplet_rate, image_path):
        self.nom = nom
        self.niveau_machine = niveau_machine
        self.type_machine = type_machine
        self.cout_achat = cout_achat
        self.temps_entretien = temps_entretien
        self.revenu_par_periode = revenu_par_periode
        self.deplet_rate = deplet_rate
        self.image_path = image_path

machines = [
    Machine("Tour", "Apprentis", "Méchanique",  20000, 5, 3000, 0.21, "images/TourNiveau1.png"),
    Machine("Tour", "Maître", "Méchanique", 25000, 6, 3500, 0.165, "images/TourNiveau2.png"),
    Machine("CNC", "Artisan", "Electrique", 30000, 7, 4000, 0.135, "images/CNCNiveau1.png"),
    Machine("CNC", "Virtuose", "Electrique", 35000, 9, 4500, 0.12, "images/CNCNiveau2.png"),
    Machine("Bras Robot", "Rookie", "Informatique", 15000, 4, 2000, 0.1, "images/RobotNiveau1.png"),
    Machine("Bras Robot", " Légendaire", "Informatique", 23000, 5, 2500, 0.084, "images/RobotNiv2.png")
]
