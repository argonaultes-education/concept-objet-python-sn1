class Classe:
    
    def __init__(self, ecole, nom):
        self.__ecole = ecole
        self.__nom = nom

    def __eq__(self, other):
        return self.__nom == other.__nom

    def __hash__(self):
        return hash(self.__nom)

    def __str__(self):
        return f'Classe: {self.__nom}'