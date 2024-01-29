spaceshipWithMaxRatio = spaceships[0]

spaceships = [{
        'color': input('color: '),
        'nb_passengers': int(input('passengers: ')),
        'nb_seats':  int(input('seats: ')),
        'name': input('name'),
    } for _ in range(3)]

for idx in range(3):
    spaceship['ratio_passenger_seat'] = spaceship['nb_passengers'] / spaceship['nb_seats']

    # est-ce que le nouveau vaisseau est plus rempli que les autres déjà créés
    if spaceshipWithMaxRatio['ratio_passenger_seat'] < spaceship['ratio_passenger_seat']:
        spaceshipWithMaxRatio = spaceship

    # ajout en fin de liste
    spaceships.append(spaceship)
    

print(f'max ratio: {spaceshipWithMaxRatio["name"]}')