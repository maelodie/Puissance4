import random 
import math
from settings import *
from algo import tirage, aleatoire, greedy, epsilon_greedy, UCB

#Expérience de jeu
"""
#affichage terminal
x = int(input("Choisir:\n1 pour l'algorithme aléatoire\n2 pour l'algorithme greedy\n3 pour l'algorithme E-greedy\n4 pour l'algorithme UCB\n"))

if x == 1:
    print(tirage(rendements, aleatoire(rendements, [])))
elif x == 2 :
    print(tirage(rendements, greedy(rendements, [])))
elif x == 3:
    print(tirage(rendements, epsilon_greedy(rendements, [])))
else:
    print(tirage(rendements, UCB(rendements, ucb_list)))

"""

#tests si c'est le bon indice
print("aléatoire: ", aleatoire(rendements, []))
print("greedy: ", greedy(rendements, []))
print("espilon greedy: ", epsilon_greedy(rendements, []))
print("UCB: " ,UCB(rendements, ucb_list))
