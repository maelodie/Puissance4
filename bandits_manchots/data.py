import matplotlib.pyplot as plt
import numpy as np
from settings import *
from algo import *

def analysis(rendements, recomp_estimees, count, count_victory, strategie, T):
    """
        Cette fonction analyse les résultats de chaque fonction 
    """

    #Tableaux à comparer
    TAB_A = [] #Tableau des récompenses estimées
    TAB_B = rendements #Tableau des rendements
    tirages = [] #tableau du nombre de tirages par leviers
    victoires_levier = [] #nombre de victoires par levier
    

    #Variables à comparer
    gain_joueur = 0
    gain_max_espéré = gain_maximal(rendements)
    
    #simulation
    TAB_A, tirage, victoires_levier = simulate(rendements, recomp_estimees, count, count_victory, strategie, T)
    gain_joueur = nb_victoires(victoires_levier)

    #affichages
    print(TAB_A)
    print(TAB_B)
    print(tirage)
    print(gain_max_espéré)
    print(gain_joueur)
    #dessin des bars de comparaison entre le rendement estimé et le rendement réel
    bar_rendements(TAB_A, TAB_B)


def bar_rendements(TAB_A, TAB_B):
    x = np.arange(N) #Tableau utilisé pour le graphe avec N entiers
    
    plt.bar(x - 0.2, TAB_A, width=0.4, label='Rendements Estimées', color='b')
    plt.bar(x + 0.2, TAB_B, width=0.4, label='Rendements Réelles', color='g')

    plt.xlabel('Levier')
    plt.ylabel('Récompenses')
    plt.title('Récompenses estimées vs récompenses réelles')
    plt.legend()
    plt.show()



    
