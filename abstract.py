from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def go(self, destination):
        pass

class Car(Vehicle):

    def __init__(self, nb_wheels):
        self.__nb_wheels = nb_wheels

class RaceCar(Car):

    def __init__(self, nb_wheels):
        super(RaceCar, self).__init__(nb_wheels)

    def go(self, destination):
        print(f'race to {destination}')

class Boat(Vehicle):

    def go(self, destination):
        print(f'sail to {destination}')

car1 = RaceCar(4)
car1.go("vacances")

boat = Boat()
boat.go("bermudes")