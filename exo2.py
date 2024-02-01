# créer la classe Spaceship

# vaisseaux cargo/vaisseaux de marchandise : quantité de marchandise, nb de containers
# vaisseaux de course : puissance turbo

class Spaceship:
    
    def __init__(self, color, nb_passengers, nb_seats, name):
        self.__color = color
        self.__nb_passengers = nb_passengers
        self.__nb_seats = nb_seats
        self.__name = name

    @property
    def color(self):
        return self.__color

    @property
    def name(self):
        return self.__name

    # ajouter une propriété ratio
    @property
    def ratio(self):
        return self.__nb_passengers / self.__nb_seats

    def __repr__(self):
        return f'Vaisseau [{self.__name}] ({self.ratio})'

# Herite de Spaceshipe
class SpaceshipCargo(Spaceship):
    
    def __init__(self, color, nb_passengers, nb_seats, name, nb_containers, quantity_fret):
       super(SpaceshipCargo, self).__init__(color, nb_passengers, nb_seats, name)
       self.__nb_containers = nb_containers
       self.__quantity_fret = quantity_fret
    
    @property
    def average_quantity_container(self):
        return self.__quantity_fret / self.__nb_containers

    def __repr__(self):
        return f'Vaisseau [{self.name}] ({self.ratio}) ({self.average_quantity_container})'

# Herite de Spaceshipe
class SpaceshipRacer(Spaceship):

    def __init__(self, color, nb_passengers, nb_seats, name, turbo):
       super(SpaceshipRacer, self).__init__(color, nb_passengers, nb_seats, name)
       self.__turbo = turbo

class Hangar:

    def __init__(self, nb_spaceships):
        self.__spaceships = [] #TODO v2: remplacer 
        self.__nb_spaceships = nb_spaceships

    # TODO v1 créer une nouvelle méthode d'instance pour ajouter tous les vaisseaux
    def ajouter_tous_les_vaisseaux(self):
        for _ in range(self.__nb_spaceships):
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
                if row_number > 0 and row_number < self.__nb_spaceships + 1:
                    features = line.split(',') # un tableau de 4 éléments
                    self.__spaceships.append(
                        Spaceship(
                            features[0],
                            int(features[1]),
                            int(features[2]),
                            features[3].strip(),
                        ) 
                    )

    def get_spaceship_with_max_ratio(self):
        return max(self.__spaceships, key=lambda spaceship: spaceship.ratio)


hangar = Hangar(4)

hangar.ajouter_depuis_fichier()

spaceshipWithMaxRatio = hangar.get_spaceship_with_max_ratio()

print(f'max ratio: {spaceshipWithMaxRatio}')

cargo1 = SpaceshipCargo('purple',8,8,'v5', 10, 500)
print(cargo1)
print(cargo1.average_quantity_container)