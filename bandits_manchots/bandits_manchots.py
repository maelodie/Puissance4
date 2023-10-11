import random 
import numpy as np
from math import sqrt, log

# Variables globales
N = 10
T = 3000
T_greedy = 100
greedy_call_count = 0
greedy_max_ind = 0
ucb_call_count = 0
T_ucb = 1000


# Liste des rendements 
# rendements = [random.uniform(0, 1) for i in range(N)]
rendements = [0.22, 0.51, 0.16, 0.75, 0.69, 0.97, 0.01, 0.98, 0.28, 0.46]

def tirage_bernouilli(rendements, choix):
    """
    Effectue un tirage de Bernouilli
    """
    res = np.random.binomial(1, rendements[choix], 1)
    return res[0]

def aleatoire(recomp_estimees, count, count_victory):
    """
    Tire aléatoirement et uniformément un numéro de levier
    """
    a = random.randint(0, 9)
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
    epsilon = random.uniform(0,1) #probabilité de choisir greedy
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

def simulate(recomp_estimees, count, count_victory, strategie, T):
   
    for i in range(T):
        a = strategie(recomp_estimees, count, count_victory)
        count[a] += 1
        if tirage_bernouilli(rendements, a):
            count_victory[a] += 1

        if i == T_greedy :  #to delete once algo is clear 
            print("count_victory with  i = T_greedy : ")
            print(count_victory)

            print("count i = T_greedy : ")
            print(count) 
        
   #reset all global variables
    global greedy_call_count
    global greedy_max_ind
    global ucb_call_count
    greedy_call_count = 0 
    greedy_max_ind = 0
    ucb_call_count = 0

    recomp_estimees = [a / b if b != 0 else 0 for a, b in zip(count_victory, count)]
    return recomp_estimees, count, count_victory

# AFFICHAGES 
count_victory = [0] * N
recomp_estimees = [0] * N
count = [0] * N
recomp_estimees, count, count_victory = simulate(recomp_estimees, count, count_victory, greedy, T)

print("count_victory result : ")
print(count_victory)

print("count result : ")
print(count)

print("recompenses estimées : ")
print(recomp_estimees)
