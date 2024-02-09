class Classe:
    
    def __init__(self, ecole, nom):
        self.__ecole = ecole
        self.__nom = nom

    # def __eq__(self, other):
    #     pass

    def __str__(self):
        return f'Classe: {self.__nom}'