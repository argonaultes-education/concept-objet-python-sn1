# créer la classe Spaceship

class Spaceship:
    
    def __init__(self, color, nb_passengers, nb_seats, name):
        self.__color = color
        self.nb_passengers = nb_passengers
        self.nb_seats = nb_seats
        self.name = name

    @property
    def color(self):
        return self.__color

    # ajouter une propriété ratio
    @property
    def ratio(self):
        return self.nb_passengers / self.nb_seats

# créer la classe Hangar

class Hangar:

    def __init__(self):
        self.spaceships = [] #TODO v2: remplacer l'initialisation à liste vide par directement l'initialisation complète de la liste
    
    # TODO v1 créer une nouvelle méthode d'instance pour ajouter tous les vaisseaux
    def ajouter_tous_les_vaisseaux(self):
        for _ in range(3): # TODO: taille constante de 3, comment la rendre personnalisable au moment de la création du hangar
            self.spaceships.append(
                Spaceship(
                    input('color: '),
                    int(input('passengers: ')),
                    int(input('seats: ')),
                    input('name: '),
                ) 
            )
    
    def ajouter_depuis_fichier(self):
        pass
        # identifier le fichier à lire
        # ouvrir le fichier en lecture
        # lire ligne à ligne
        # chaque ligne contient des caractéristiques d'un unique vaisseau séparées par des virgules
        # créer le vaisseau correspondant à la ligne
        # l'ajouter à la liste

# utiliser la classe à la place du dictionnaire pour chaque élément de la liste

spaceships = [ Spaceship(
                    input('color: '),
                    int(input('passengers: ')),
                    int(input('seats: ')),
                    input('name: '),
            ) for _ in range(3) ]


spaceshipWithMaxRatio = max(spaceships, key=lambda spaceship: spaceship.ratio)


print(f'max ratio: {spaceshipWithMaxRatio.name}')

# == Résultat attendu ==
# Instanciation de la classe Hangar
# TODO: comment créer ce Hangar
# Ajout des vaisseaux dans le hangar
# Affichage du vaisseau ayant le plus