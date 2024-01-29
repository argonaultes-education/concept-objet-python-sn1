# ouvrir le fichier en lecture
with open('ages.txt', 'r') as ages:
# lire le fichier ligne à ligne
    for line in ages.readlines():
# comparer le nombre lu avec 18, plus grand ?
        if int(line) >= 18:
            print(f'Student[{int(line)}] is an adult')
        else:
            print(f'Student[{int(line)}] is too young')
