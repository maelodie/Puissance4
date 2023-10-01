import random 
import math
from settings import *

def tirage(rendements, choix):
    p = random.uniform(0,1) #probabilité aléatoire générée, si elle est >= a, on gagne, sinon on perd
    if p < rendements[choix]:
        return 1
    else:
        return 0

def aleatoire(rendements, count_levier):
    a = random.randint(0,9)
    return a

def greedy(rendements, count_levier):

    ui = [0] * N #liste qui va stocker le nombre de victoires 
    
    #boucle qui fait une simulation X fois pour calculer les rendements de chaque levier
    for i in range(nb_exp):
        a = aleatoire(rendements, count_levier)
        if tirage(rendements, a) == 1:
            ui[a] += 1
    
    #on retourne la probabilité la + élevée sachant que la probabilité = nb_victoires / X
    victoire = [ i/nb_exp for i in ui]
    argmax = max(victoire)
    return victoire.index(argmax)

def epsilon_greedy(rendements, count_levier):
    #note: un epsilon élevé encourage à plus d'exploration, un epsilon faible encourage à plus d'exploitation

    epsilon = random.uniform(0,1) #probabilité de choisir greedy
    a = 0 #resutlat

    for i in range(nb_exp):
        #si un nombre aléatoire < epsilon on applique aleatoire, sinon on applique greedy
        if random.uniform(0,1) < epsilon:
            a = aleatoire(rendements, count_levier)
        else:
            a = greedy(rendements, count_levier)

    return a

def UCB(rendements, count_levier):
    #count_levier = Nt(a) où t est l'itération

    a = 0 #résultat
    a_test = 0 #resultat loirs de l'appel à aléatoire
    ui = [0] * N #tableau utilisé pour les probas estimées de chaque levier
    victoire = [0] * N #tab utilisé pour le nombre de victoire par levier

    for t in range(nb_exp+1):
        a_test = aleatoire(rendements, count_levier)
        count_levier[a_test] += 1

        if tirage(rendements, a_test) == 1:
            ui[a_test] += 1

        victoire = [ i/(t+1) for i in ui ]
        argmax_ui = max(victoire)
        a = int(victoire.index(argmax_ui) + math.sqrt((2 * math.log(t+1) / count_levier[a_test])))
    return a