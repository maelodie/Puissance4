import random 
import numpy as np
from settings import *
from math import sqrt, log

def tirage_bernouilli(rendements, choix):
    """
    Effectue un tirage de Bernouilli
    premier argument = n
    deuxième argument = répartition des probabilité pour chaque choix (p)
    dernier argument = size de l'échantillon (ici 1 signifie que c'est un tableau unidimensionnel de taille 1)

    Valeur de retour = res[0] car la fonctin binomial retourne un tableau 
    """
    res = np.random.binomial(1, rendements[choix], 1)
    return res[0]

def aleatoire(recomp_estimees, count, count_victory):
    """
    Tire aléatoirement et uniformément un numéro de levier
    Baseline, algorithme que tous les autres doivent battre
    """
    a = random.randint(0, N-1)
    return a

def greedy(recomp_estimees, count, count_victory):
    global greedy_call_count
    global  greedy_max_ind
    
    # Check if the number of calls is less than T_greedy
    if greedy_call_count < T_greedy:
        
        if greedy_call_count ==  T_greedy - 1 :
            tmp =  [a / b if b != 0 else 0 for a, b in zip(count_victory, count)]
            greedy_max_ind = tmp.index(max(tmp))
            print("max_ind : ", greedy_max_ind)

        greedy_call_count += 1
        return aleatoire(recomp_estimees, count, count_victory)
    return greedy_max_ind

def epsilon_greedy(recomp_estimees, count, count_victory):
    #note: un epsilon élevé encourage à plus d'exploration, un epsilon faible encourage à plus d'exploitation
    
    a = 0 
    #si un nombre aléatoire < epsilon on applique aleatoire, sinon on applique greedy
    if random.uniform(0,1) < epsilon:
        a = aleatoire(recomp_estimees, count, count_victory)
    else:
         a = greedy(recomp_estimees, count, count_victory)

    return a

def UCB(recomp_estimees, count, count_victory):
    global ucb_call_count 

    if ucb_call_count < T_ucb :  #jouer qq coups pour ne pas avoir des valeurs nulles
        ucb_call_count += 1
        return aleatoire(recomp_estimees, count, count_victory)
    
    mû =  [a / b if b != 0 else 0 for a, b in zip(count_victory, count)] # les recompenses estimés
    t = sum(count) # l'instant t est le i-eme coup joué, donc la somme des coups  jusqu'a présentn == le nombre total d'itérations jusqu'à présent.

    ucb_val = [mû[i] + sqrt((2 * log(t + 1) / count[i])) for i in range(N)] # on comstruit la liste de la somme de la recompenses estimée (mû) et la racine carré du log...
    a = ucb_val.index(max(ucb_val)) #on renvoie le numéro du levier avec la valeur maximale

    return a

def simulate(rendements, recomp_estimees, count, count_victory, strategie, T):
    gain = 0
    regret = []
    cumul_regret = 0
    cumul_max = 0
    mu_max = rendements.index(max(rendements))
    for i in range(T):
        a = strategie(recomp_estimees, count, count_victory)
        count[a] += 1
        tirage = tirage_bernouilli(rendements, a)
        tirage_max = tirage_bernouilli(rendements, mu_max)

        #remplissage du tableau de regret
        cumul_regret += tirage
        cumul_max += tirage_max
        regret.append(cumul_max - cumul_regret)

        if tirage:
            count_victory[a] += 1
            gain += 1

   #reset all global variables
    global greedy_call_count
    global greedy_max_ind
    global ucb_call_count
    greedy_call_count = 0 
    greedy_max_ind = 0
    ucb_call_count = 0

    recomp_estimees = [a / b if b != 0 else 0 for a, b in zip(count_victory, count)]
    return gain, recomp_estimees, count, count_victory, regret

def calcul_gmax(rend, times):
    index_max = rend.index(max(rend))
    gain_max = 0
    for i in range(times):
        if tirage_bernouilli(rend, index_max):
            gain_max += 1
    return gain_max


def calcul_regret(rend, tirage):
    regret = []
    cumulation_regret = 0
    for i in range(T):
        regret.appe
    return regret

