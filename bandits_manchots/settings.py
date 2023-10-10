"""Ce fichier comporte l'ensemble des paramètres de l'expérience menée 
au cours du jeu du bandits-manchots"""

import random 
# Variables globales
N = 10 #Nombre de leviers
T = 3000 #Nombre d'essais
T_greedy = 1000 #Nombre de tours pendant lesquels on explore
greedy_call_count = 0 #Nombre d'appels à greedy
greedy_max_ind = 0 #index maximal de greedy
ucb_call_count = 0 #nombre d'appels à ucb
T_ucb = 1500 #nombre de coups joués en aléatoire pendant ucb
epsilon = 0.5

#Listes de rendements sur lesquels on va mener l'expérience
rendements = [(random.uniform(0, 1)) for i in range(N)]
rend_3ele = [0.50, 0.02, 0.86]
rendements_1 = [0.22, 0.51, 0.16, 0.75, 0.69, 0.97, 0.01, 0.8, 0.28, 0.46]
rendements_2 = [0.86, 0.13, 0.65, 0.73, 0.57, 0.39, 0.08, 0.52, 0.34, 0.91]
rendements_3 = [0.63, 0.82, 0.94, 0.19, 0.33, 0.27, 0.73, 0.76, 0.62, 0.45]
rendements_4 = [0.61, 0.29, 0.09, 0.77, 0.45, 0.88, 0.74, 0.53, 0.13, 0.95]
rendements_5 = [0.67, 0.25, 0.14, 0.32, 0.67, 0.45, 0.89, 0.16, 0.37, 0.06]
rendements_6 = [0.26, 0.37, 0.99, 0.72, 0.18, 0.75, 0.65, 0.22, 0.08, 0.11]
rendements_7 = [0.68, 0.72, 0.58, 0.52, 0.17, 0.72, 0.56, 0.04, 0.26, 0.69]
rendements_8 = [0.59, 0.46, 0.35, 0.21, 0.95, 0.34, 0.72, 0.12, 0.72, 0.25]
rendements_9 = [0.98, 0.41, 0.92, 0.74, 0.31, 0.43, 0.65, 0.79, 0.65, 0.79]
rendements_10 = [0.11, 0.68, 0.77, 0.19, 0.16, 0.94, 0.89, 0.77, 0.25, 0.33]

list_rend = [rendements, rendements_1, rendements_2, rendements_3, rendements_4, 
             rendements_5, rendements_6, rendements_7, rendements_8, rendements_7, 
             rendements_10]