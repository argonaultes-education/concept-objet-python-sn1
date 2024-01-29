spaceships = []

spaceshipWithMaxRatio = spaceships[0]

for idx in range(3):
    spaceship = {} # déclaration du dictionnaire vaisseau

    spaceship['color'] = input('color: ')
    spaceship['nb_passengers'] = int(input('passengers: '))
    spaceship['nb_seats'] = int(input('seats: '))
    spaceship['name'] = input('name')
    spaceship['ratio_passenger_seat'] = spaceship['nb_passengers'] / spaceship['nb_seats']

    # est-ce que le nouveau vaisseau est plus rempli que les autres déjà créés
    if spaceshipWithMaxRatio['ratio_passenger_seat'] < spaceship['ratio_passenger_seat']:
        spaceshipWithMaxRatio = spaceship

    # ajout en fin de liste
    spaceships.append(spaceship)
    

print(f'max ratio: {spaceshipWithMaxRatio["name"]}')