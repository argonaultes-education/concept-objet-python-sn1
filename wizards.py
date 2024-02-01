class Moldu:
    
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

class Wizard(Moldu):

    def __init__(self, house, name):
        super(Wizard, self).__init__(name)
        self.__house = house

    def lancer_un_sort(self):
        print(f'Sort lance par {self.name}')

harry = Wizard('gryffondor', 'harry')
dursley = Moldu('dursley')

harry.lancer_un_sort()
dursley.lancer_un_sort()