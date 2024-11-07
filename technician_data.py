class Technician:
    def __init__(self, nom, specialite, niveau, salaire, facteur_reparation, image_path):
        self.nom = nom
        self.specialite = specialite
        self.niveau = niveau
        self.salaire = salaire
        self.facteur_reparation = facteur_reparation
        self.image_path = image_path

technicians = [
    Technician("Rémy Tourneur", "Mécanique", "Débutant", 100, 0.75,'images/Tech7.png'),
    Technician("Jack Soudey", "Mécanique", "Moyen", 200, 1,'images/Tech7.png'),
    Technician("Claude Piston", "Mécanique", "Expert", 300, 1.5,'images/Tech7.png'),
    Technician("Hubert Volt", "Électrique", "Débutant", 150, 0.75,'images/Tech7.png'),
    Technician("Fred Fraiseuse", "Électrique", "Moyen", 250, 1,'images/Tech7.png'),
    Technician("Léon Laser", "Électrique", "Expert", 350, 1.5,'images/Tech7.png'),
    Technician("Alex Byte", "Informatique", "Débutant", 120, 0.75,'images/Tech7.png'),
    Technician("Lucas Pixel", "Informatique", "Moyen", 220, 1,'images/Tech7.png'),
    Technician("Dave Data", "Informatique", "Expert", 320, 1.5,'images/Tech7.png')
]
