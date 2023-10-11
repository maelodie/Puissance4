from data import *
from config import * 
from algo import *

#NB : pour pouvoir utiliser des configurations différentes, remplacer les valeurs dans config
list = rendements_1

strategie = int(input("Sélectionner une numéro pour exécuter une analyse\n1 : Aléatoire\n2 : Greedy\n3 : Epsilon Greedy\n4 : UCB\n5 : Etude des regrets\n"))
if strategie == 1:
    experience(list, aleatoire)
elif strategie == 2:
    experience(list, greedy)
elif strategie == 3:
    experience(list, epsilon_greedy)
elif strategie == 4:
    experience(list, UCB)
else:
    regrets_gains(list)