import matplotlib.pyplot as plt
import numpy as np
from config import *
from algo import *

def experience(rend, strategie):
    """
    Cette fonction permet d'afficher les historigrammes comparant les rendements réels et les rendements estimés par la stratégie
    en paramètre

    Puis la contion compare le nombre d'essais contre le nombre de victoire
    """
    _, recomp_estimees, count, count_victory, _ = simulate(rend, strategie)
    
    #Tracage des graphes de comparaison rendements vs recompenses estimees
    plt.subplot(1, 2, 1)
    x = np.arange(N)
    plt.bar(x + 0.2, recomp_estimees, width=0.4, label='Récompenses Estimées', color='g')
    plt.bar(x - 0.2, rend, width=0.4, label='Récompenses Réelles', color='r')
    plt.xlabel('Levier')
    plt.ylabel('Récompenses')
    plt.title('Récompenses estimées vs récompenses réelles')
    plt.legend()
    
    plt.subplot(1, 2, 2)
    #Tracage des graphes de comparaison du nombre de coups contre le nombre de victoires
    y = np.arange(N) #Tableau utilisé pour le graphe avec N entiers
    plt.bar(y - 0.2, count, width=0.4, label="Nombre d'essais", color='b')
    plt.bar(y + 0.2, count_victory, width=0.4, label='Nombre de victoires', color='g')
    plt.xlabel('Levier')
    plt.ylabel('Tirage')
    plt.title("Nombre d'essais vs Nombre de victoires")
    plt.legend()
    plt.show()

   
def regrets_gains(rend):
    """
    Cette fonction trace les courbes de regret de chaque fonction et les affiches sur un seul graphe
    """
    _, _, _, _, regret_tab_aleatoire = simulate(rend, aleatoire)
    _, _, _, _, regret_tab_greedy = simulate(rend, greedy)
    _, _, _, _, regret_tab_epsilon= simulate(rend, epsilon_greedy)
    _, _, _, _, regret_tab_UCB = simulate(rend, UCB)

    #Tracage des regrets
    plt.plot(range(1, T + 1), regret_tab_aleatoire, marker='o', color='blue', label='Aleatoire', linewidth=2, markersize=1)
    plt.plot(range(1, T + 1), regret_tab_greedy, marker='^', color='green', label='Greedy', linewidth=2, markersize=1)
    plt.plot(range(1, T + 1), regret_tab_epsilon, marker='s', color='red', label='Epsilon-Greedy', linewidth=2, markersize=1)
    plt.plot(range(1, T + 1), regret_tab_UCB, marker='d', color='purple', label='UCB', linewidth=2, markersize=1)
    exp_infos = "Nombre d'itérations: " + str(T) + " Nombre de leviers: " + str(N) + " T_greedy: " + str(T_greedy) + " Epsilon: " + str(epsilon) + " T_ucb" + str(T_ucb)
    
    plt.legend()
    plt.xlabel('Temps (t)')
    plt.ylabel('Regret')
    plt.title("Evolution du regret en fonction du temps\n" + exp_infos, fontsize=8)
    plt.show()
