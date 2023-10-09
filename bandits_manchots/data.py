import matplotlib.pyplot as plt
import numpy as np
from settings import *
from algo import *

def experience(rend, strategie):

    gain_joueur, recomp_estimees, count, count_victory, regret_tab = simulate(rend, strategie)
    
    #Tracage des graphes de comparaison rendements vs recompenses estimees
    x = np.arange(N)
    plt.bar(x + 0.2, recomp_estimees, width=0.4, label='Récompenses Estimées', color='g')
    plt.bar(x - 0.2, rend, width=0.4, label='Récompenses Réelles', color='r')
    plt.xlabel('Levier')
    plt.ylabel('Récompenses')
    plt.title('Récompenses estimées vs récompenses réelles')
    plt.legend()
    plt.show()

    #Tracage des graphes de comparaison du nombre de coups contre le nombre de victoires
    y = np.arange(N) #Tableau utilisé pour le graphe avec N entiers
    plt.bar(y - 0.2, count, width=0.4, label="Nombre d'essais", color='b')
    plt.bar(y + 0.2, count_victory, width=0.4, label='Nombre de victoires', color='g')
    plt.xlabel('Levier')
    plt.ylabel('Tirage')
    plt.title("Nombre d'essais vs Nombre de victoires")
    plt.legend()
    plt.show()

    #Tracage des regrets
    plt.plot(range(1, T + 1), regret_tab, marker='o')
    plt.xlabel('Temps (t)')
    plt.ylabel('Regret')
    plt.title('Évolution du regret en fonction du temps')
    plt.show()


