class Spaceship:
    
    def __init__(self, color, nb_passengers, nb_seats, name):
        self.__color = color
        self.nb_passengers = nb_passengers
        self.nb_seats = nb_seats
        self.name = name

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        if value == 'red' or value == 'blue':
            self.__color = value
        else:
            print('unable to set yellow color')

# créer la classe Hangar

vaisseau1 = Spaceship('red', 1, 1, 'v1')
print(vaisseau1.color)

vaisseau1.color = 'blue'
print(vaisseau1.color)
