from groupe import Groupe
from classe import Classe

class Ecole:
    
    def __init__(self, groupe, nom):
        self.__groupe = groupe
        self.__groupe.ajout_ecole(self)
        self.__nom = nom
        self.__classes = set()

    def ajout_classe(self, classe):
        self.__classes.add(classe)

    @property
    def nom(self):
        return self.__nom
    
    def afficher_classes(self):
        for classe in self.__classes:
            print(classe)

    def display(self):
        print(f'Nom: {self.__nom}')

    def __str__(self):
        return f'Nom: {self.__nom}'

cetd = Groupe('cetd')
epsi = Ecole(cetd, 'epsi')
epsi.ajout_classe(Classe(epsi, 'sn1-gr1'))
epsi.ajout_classe(Classe(epsi, 'sn1-gr1'))
epsi.afficher_classes()