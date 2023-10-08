import matplotlib.pyplot as plt
import numpy as np
from settings import *
from algo import *

def comparaisons_rendements(rendements, recomp_estimees, count, count_victory, strategie, T):
    """
        Quantification de l'exploration
        Cette fonction analyse les résultats de chaque fonction 
    """

    #Tableaux à comparer
    TAB_A = [] #Tableau des récompenses estimées
    TAB_B = rendements #Tableau des rendements
    

    #Variables à comparer
    gain_joueur = 0
    gain_max_espéré = T
    
    #simulation
    gain_joueur, TAB_A, _ , _ = simulate(rendements, recomp_estimees, count, count_victory, strategie, T)
    print(gain_joueur)

    #affichages
    print(TAB_A)
    print(TAB_B)
    print(gain_max_espéré)
    print(gain_joueur)

    #dessin des bars de comparaison entre le rendement estimé et le rendement réel
    x = np.arange(N) #Tableau utilisé pour le graphe avec N entiers
    
    plt.bar(x - 0.2, TAB_B, width=0.4, label='Rendements Estimées', color='r')
    plt.bar(x + 0.2, TAB_A, width=0.4, label='Rendements Réelles', color='b')

    plt.xlabel('Levier')
    plt.ylabel('Récompenses')
    plt.title('Récompenses estimées vs récompenses réelles')
    plt.legend()
    #algo
    plt.show()

def comparaison_victoires(rendements, recomp_estimees, count, count_victory, strategie, T):
    """
    Quantification de l'exploitation
    Cette fonction compare le nombre de victoires vs le nombre d'essais pour chaque algorithme
    """ 
    _, _, count, count_victory = simulate(rendements, recomp_estimees, count, count_victory, strategie, T)
    x = np.arange(N) #Tableau utilisé pour le graphe avec N entiers

    plt.bar(x - 0.2, count, width=0.4, label="Nombre d'essais", color='b')
    plt.bar(x + 0.2, count_victory, width=0.4, label='Nombre de victoires', color='g')

    plt.xlabel('Levier')
    plt.ylabel('Tirage')
    plt.title("Nombre d'essais vs Nombre de victoires")
    plt.legend()

    #algo
    plt.show()

def comparaison_gains(rendements, recomp_estimees, count, count_victory, T):
    """
    Cette fonction compare les gains de chaque algorithme
    """
    gain_max = T
    gain_aleatoire, _, _, _ = simulate(rendements, recomp_estimees, count, count_victory, aleatoire, T)
    gain_greedy, _, _, _ = simulate(rendements, recomp_estimees, count, count_victory, greedy, T)
    gain_epsilon_greedy, _, _, _ = simulate(rendements, recomp_estimees, count, count_victory, epsilon_greedy, T)
    gain_UCB, _, _, _ = simulate(rendements, recomp_estimees, count, count_victory, UCB, T)

    data = [gain_max, gain_aleatoire, gain_greedy, gain_epsilon_greedy, gain_UCB]
    labels = ['Gain Maximal', 'Gain Aleatoire', 'Gain Greedy', 'Gain Epsilon Greedy', 'Gain UCB']
    x_values = range(len(data))

    plt.bar(x_values, data, color='blue')

    for i, (value, label) in enumerate(zip(data, labels)):
        plt.text(i, value + 0.5, f'{label}\n{value}', ha='center', va='bottom')

    plt.xlabel('Algorithmes')
    plt.ylabel('Gain')
    plt.title('Comparaison des gains par algorithme')

    plt.show()
    
def experience(rend, T_value, T_greedy_value, epsilon_value, T_ucb_value):
    #Variable resets
    global T
    T = T_value
    global T_greedy
    T_greedy = T_greedy_value
    global epsilon
    epsilon = epsilon_value
    global T_ucb
    T_ucb = T_ucb_value

    #Comparaison des rendements
    comparaisons_rendements(rend, [0] * N, [0] * N, [0] * N, aleatoire, T)
    comparaisons_rendements(rend, [0] * N, [0] * N, [0] * N, greedy, T)
    comparaisons_rendements(rend, [0] * N, [0] * N, [0] * N, epsilon_greedy, T)
    comparaisons_rendements(rend, [0] * N, [0] * N, [0] * N, UCB, T)

    #Comparaison du nombre de victoires
    comparaison_victoires(rend, [0] * N, [0] * N, [0] * N, aleatoire, T)
    comparaison_victoires(rend, [0] * N, [0] * N, [0] * N, greedy, T)
    comparaison_victoires(rend, [0] * N, [0] * N, [0] * N, epsilon_greedy, T)
    comparaison_victoires(rend, [0] * N, [0] * N, [0] * N, UCB, T)

    #Comparaison des gains
    comparaison_gains(rend, [0] * N, [0] * N, [0] * N, T)




