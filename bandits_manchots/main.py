from data import *
from settings import * 
from algo import *

# VALEURS INITIALES 
from data import *
#format rendements, T, T_greedy, epsilon, T_ucb, fonction

def exp(rend):
    experience(rend, 100, 50, 1, 0, epsilon_greedy)
    experience(rend, 1000, 500, 0.2, 0, epsilon_greedy)
    experience(rend, 10000, 5000, 0.2, 0.2, epsilon_greedy)
    experience(rend, 100, 50, 0.5, 0, epsilon_greedy)
    experience(rend, 1000, 500, 0.5, 0, epsilon_greedy)
    experience(rend, 10000, 5000, 0.5, 0, epsilon_greedy)
    experience(rend, 100, 50, 0.8, 0, epsilon_greedy)
    experience(rend, 1000, 500, 0.8, 0, epsilon_greedy)
    experience(rend, 10000, 5000, 0.8, 0.2, epsilon_greedy)



exp(rendements_1)