class Ecole:
    
    def __init__(self, groupe, nom):
        self.__groupe = groupe
        self.__groupe.ajout_ecole(self)
        self.__nom = nom

    @property
    def nom(self):
        return self.__nom
    
    def display(self):
        print(f'Nom: {self.__nom}')

    def __str__(self):
        return f'Nom: {self.__nom}'