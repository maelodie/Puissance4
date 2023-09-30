import matplotlib.pyplot as plt
import numpy as np
from plateau import *
from player import * 

def analyse(joueur1, joueur2, nb_parties):
    """
    Cette fonction analyse le fonctionnement. Voici le concept:
    - On définit une variable aléatoire X qui représente le nombre de coups
    nécessaires avant qu'un joueur ne gagne la partie

    - On a 3 événements: A, le premier joueur gagne la partie et B, le second
    joueur gagne la partie et C, la partie est nulle

    - On calcule P(A) et P(B) les probabilités des événements A et B ainsi que P(C)

    - On associe le nombre de coup à la probabilité qu'un joueur ne gagne la partie 
    au nombre de coups
    """
    victoire_J1 = 0 #nombre de victoires du joueur 1
    victoire_J2 = 0 #nombre de victoires du joueur 2
    parties_nulles = 0 #nombre de parties nulles

    P_A = 0 #probabilité de l'événement A
    P_B = 0 #probabilité de l'événement B
    P_0 = 0 #probabilité de l'événement C
    tab_res = []

    for i in range(nb_parties):
        plateau = Plateau(NB_COLONNES, NB_LIGNES) 
        res = plateau.run(joueur1, joueur2)
        if res[0] == 1:
            victoire_J1 += 1
        elif res[0] == -1:
            victoire_J2 += 1
        else:
            parties_nulles +=1
        tab_res.append(res)
        plateau.reset()
    
    #résultats
    P_A = victoire_J1 / nb_parties
    P_B = victoire_J2 / nb_parties
    P_0 = parties_nulles / nb_parties

    #affichages 
    for i in tab_res:
        print(i)
    #print("Nombre de victoires joueur 1: ", victoire_J1)
    #print("Nombre de victoires joueur 2: ", victoire_J2)
    print("Probabilité que le joueur 1 gagne: ", P_A)
    print("Probabilité que le joueur 2 gagne: ", P_B)
    print("Probabilité que la partie soit null: ", P_0)

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
        

