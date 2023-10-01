import random 

N = 10 #nombre de leviers de la machine
ucb_list = [0] * N
#rendements = [(random.uniform(0, 1)) for i in range(N)] #chance de gagner selon un levier entre 0 et 1
rendements = [0.4, 0.5, 0.4, 0.1, 0.9, 0.2, 0.7, 0.6, 0.8, 0.3]
nb_exp = 1000