class Starship:

    def __init__(self, nomVaisseau):
        self.name = nomVaisseau
        self.listPassengers = []

    def display_name(self):
        print(self.name)

# Création/Instanciation du vaisseau 1
starship1 = Starship('x-wing')
starship1.listPassengers.append('john')
starship1.listPassengers.append('clark')

# Création du vaisseau 2
starship2 = Starship('t-fighter')
starship2.listPassengers.append('cindy')

# Affiche les passagers du vaisseau 1 et 2
print(starship1.listPassengers)
print(starship2.listPassengers)