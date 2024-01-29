spaceships = [{}, {}, {}]


for spaceship in spaceships:
    spaceship['color'] = input('color: ')
    spaceship['nb_passengers'] = int(input('passengers: '))
    spaceship['nb_seats'] = int(input('seats: '))
    spaceship['name'] = input('name')
    spaceship['ratio_passenger_seat'] = spaceship['nb_passengers'] / spaceship['nb_seats']

spaceshipWithMaxRatio = spaceships[0]

for spaceship in spaceships[1:]:
    if spaceshipWithMaxRatio['ratio_passenger_seat'] < spaceship['ratio_passenger_seat']:
        spaceshipWithMaxRatio = spaceship

print(f'max ratio: {spaceshipWithMaxRatio["name"]}')