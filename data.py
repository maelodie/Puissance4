import matplotlib.pyplot as plt
import numpy as np
from plateau import *
from player import * 

def analyse(joueur1, joueur2, nb_parties):
    """
    Cette fonction analyse le fonctionnement. Voici le concept:
    - On définit une variable aléatoire X qui représente le nombre de coups
    nécessaires avant qu'un joueur ne gagne la partie

    - On a 2 événements: A, le premier joueur gagne la partie et B, le second
    joueur gagne la partie

    - On calcule P(A) et P(B) les probabilités des événements A et B

    - On associe le nombre de coup à la probabilité qu'un joueur ne gagne la partie 
    au nombre de coups
    """
    victoire_J1 = 0 #nombre de victoires du joueur 1
    victoire_J2 = 0 #nombre de victoires du joueur 2
    
    P_A = 0 #probabilité de l'événement A
    P_B = 0 #probabilité de l'événement B

    tab_res = []

    for i in range(nb_parties):
        plateau = Plateau(NB_COLONNES, NB_LIGNES) 
        res = plateau.run(joueur1, joueur2)
        if res[0] == 1:
            victoire_J1 += 1
        else:
            victoire_J2 += 1
        tab_res.append(res)
        plateau.reset()
    
    #résultats
    P_A = victoire_J1 / nb_parties
    P_B = victoire_J2 / nb_parties
    #print(tab_res)
    #print("Nombre de victoires joueur 1: ", victoire_J1)
    #print("Nombre de victoires joueur 2: ", victoire_J2)
    print("Probabilité que le joueur 1 gagne: ", P_A)
    print("Probabilité que le joueur 2 gagne: ", P_B)

    #graphes
    graphe(tab_res)

def graphe(list):
    #listes de données
    nb_coups_j1 = [x[1] for x in list if x[0] == 1]
    nb_coups_j2 = [x[1] for x in list if x[0] == -1]

    #historigrammes
    plt.hist(nb_coups_j1, bins=10, alpha=0.5, label='Joueur 1', color='blue')
    plt.hist(nb_coups_j2, bins=10, alpha=0.5, label='Joueur 2', color='green')

    #graphique
    plt.xlabel('Nombre de coups')
    plt.ylabel('Fréquence')
    plt.title('Fréquence de victoire selon le nombre de coups')

    #Affichage
    plt.show()
        

