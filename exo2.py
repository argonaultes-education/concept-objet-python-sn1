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
        self.__spaceships = [] #TODO v2: remplacer l'initialisation à liste vide par directement l'initialisation complète de la liste
    
    # TODO v1 créer une nouvelle méthode d'instance pour ajouter tous les vaisseaux
    def ajouter_tous_les_vaisseaux(self):
        for _ in range(3): # TODO: taille constante de 3, comment la rendre personnalisable au moment de la création du hangar
            self.__spaceships.append(
                Spaceship(
                    input('color: '),
                    int(input('passengers: ')),
                    int(input('seats: ')),
                    input('name: '),
                ) 
            )
    
    def ajouter_depuis_fichier(self):
        spaceships = 'spaceships.csv'
        with open(spaceships, 'r') as spaceships_file:
            for row_number, line in enumerate(spaceships_file.readlines()):
                if row_number > 0 and row_number < 4:
                    features = line.split(',') # un tableau de 4 éléments
                    self.__spaceships.append(
                        Spaceship(
                            features[0],
                            int(features[1]),
                            int(features[2]),
                            features[3],
                        ) 
                    )

    def get_spaceship_with_max_ratio(self):
        return max(self.__spaceships, key=lambda spaceship: spaceship.ratio)


hangar = Hangar() #TODO: comment obtenir un hangar dont la taille est personnalisee a l'initialisation

hangar.ajouter_depuis_fichier()

spaceshipWithMaxRatio = hangar.get_spaceship_with_max_ratio()

print(f'max ratio: {spaceshipWithMaxRatio.name} with {spaceshipWithMaxRatio.ratio}')

