class Groupe:
    
    def __init__(self, nom):
        self.__ecoles = []
        self.__nom = nom

    def ajout_ecole(self, ecole):
        self.__ecoles.append(ecole)

    def afficher_ecoles(self):
        for ecole in self.__ecoles:
            print(ecole)
            ecole.display() # Nom: nom_de_lecole