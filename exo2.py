# créer la classe Spaceship

class Spaceship:
    
    def __init__(self, color, nb_passengers, nb_seats, name):
        self.color = color
        self.nb_passengers = nb_passengers
        self.nb_seats = nb_seats
        self.name = name
    
# utiliser la classe à la place du dictionnaire pour chaque élément de la liste

spaceships = [ Spaceship(
                    input('color: '),
                    int(input('passengers: ')),
                    int(input('seats: ')),
                    input('name: '),
            ) for _ in range(3) ]


# spaceships = []
# for _ in range(3):
#     spaceship = Spaceship(
#                     input('color: '),
#                     int(input('passengers: ')),
#                     int(input('seats: ')),
#                     input('name: '),
#             )
#     spaceships.append(spaceship)


# modifier le code pour interroger les attributs correspondants

# spaceshipWithMaxRatio = max(spaceships, key=lambda spaceship: spaceship.nb_passengers / spaceship.nb_seats)

def getRatio(spaceship):
    return spaceship.nb_passengers / spaceship.nb_seats

spaceshipWithMaxRatio = max(spaceships, key=getRatio)


print(f'max ratio: {spaceshipWithMaxRatio.name}')

# == Résultat attendu ==
# Instanciation de la classe Hangar
# Ajout des vaisseaux dans le hangar
# Affichage du vaisseau ayant le plus