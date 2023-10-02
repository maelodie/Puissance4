import random 
import numpy as np

# Variables globales
N = 10
T = 1000
T_greedy = 400
greedy_call_count = 0
greedy_max_ind = 0


# Liste des rendements 
rendements = [random.uniform(0, 1) for i in range(N)]

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


def simulate(recomp_estimees, count, count_victory, strategie, T):
   
    for i in range(T):
        a = strategie(recomp_estimees, count, count_victory)
        count[a] += 1
        if tirage_bernouilli(rendements, a):
            count_victory[a] += 1

        if i == T_greedy :
            print("count_victory with  i = T_greedy : ")
            print(count_victory)

            print("count i = T_greedy : ")
            print(count) 
        
    if strategie == greedy :
        global greedy_call_count
        global greedy_max_ind
        greedy_call_count = 0 
        greedy_max_ind = 0

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
