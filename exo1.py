print('Bienvenue ici')

lifePoints = input('Nb de points de vie: ')

hits = input('Nb dégâts: ')

remainingLife = int(lifePoints) - int(hits)

print('Nb de points de vie :', remainingLife)

print('Nb de points de vie :' + str(remainingLife))

print(f'Nb de points de vie : {remainingLife}')