import random 
import math
import numpy as np

#variables globales
N = 10

#liste des rendements 
rendements = [random.uniform(0, 1) for i in range(N)]
formatted_rendements = ["{:.2f}".format(random.uniform(0, 1)) for i in range(N)]

def tirage_bernouilli(rendements, choix):
    res = np.random.binomial(1, rendements[choix], 1)
    return res[0]

def aleatoire(recomp_estimees, count):
    a = random.randint(0,9)
    return a

def greedy(recomp_estimees, count):

def simulate(strategie, T):
    count_victory = []
    recomp_estimees = []
    count = []

    for i in range(T):
        a = strategie(recomp_estimees, count)
        
        
#AFFICHAGES 
#print(tirage_bernouilli(rendements, 5))
aleatoire([],[])