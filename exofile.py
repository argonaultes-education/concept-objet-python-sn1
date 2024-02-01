# ouvrir le fichier en lecture
with open('ages.txt', 'r') as ages:
# lire le fichier ligne à ligne
    lines = ages.readlines()
    print(lines[1])