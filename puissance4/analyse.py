import matplotlib.pyplot as plt
from plateau import *
import numpy as np 
from player import * 

def analyse(joueur1, joueur2, nb_parties, esp):
    """
    Cette fonction analyse les victoires et le nombre de coups joués. Voici le concept:
    - On définit une variable aléatoire X qui représente le nombre de coups
    nécessaires avant qu'un joueur ne gagne la partie
    - On a 3 événements: A, le premier joueur gagne la partie et B, le second
    joueur gagne la partie et C, la partie est nulle
    - On calcule P(A) et P(B) les probabilités des événements A et B ainsi que P(C)
    - On associe le nombre de coup à la probabilité qu'un joueur ne gagne la partie 
    au nombre de coups
    Si esp vaut 1, nous calculons l'espérance de X
    """
    victoire_J1 = 0 #nombre de victoires du joueur 1
    victoire_J2 = 0 #nombre de victoires du joueur 2
    parties_nulles = 0 #nombre de parties nulles

    tab_1= [0] * 43 #nombre de partie avec tab[i] coups avant la victoire du joueur 1
    tab_2= [0] * 43 #nombre de partie avec tab[i] coups avant la victoire du joueur 2

    P_A = 0 #probabilité de l'événement A
    P_B = 0 #probabilité de l'événement B
    P_0 = 0 #probabilité de l'événement C
    tab_res = []

    nb_coups_j1 = 0      #somme des nb de coups des parties dans lesquelles joueur 1 gagne
    nb_coups_j2 = 0      #somme des nb de coups des parties dans lesquelles joueur 2 gagne
    nb_coups_nulles = 0  #somme des nb de coups des partie nulles

    for i in range(nb_parties):
        plateau = Plateau(NB_COLONNES, NB_LIGNES) 
        res = plateau.run(joueur1, joueur2)

        if res[0] == 1:
            victoire_J1 += 1
            nb_coups_j1 += res[1]
            tab_1[res[1]] += 1

        elif res[0] == -1:
            victoire_J2 += 1 
            nb_coups_j2 += res[1]
            tab_2[res[1]] += 1

        else:
            parties_nulles +=1
            nb_coups_nulles += res[1]
        tab_res.append(res)
        plateau.reset()

    #résultats

    P_A = victoire_J1 / nb_parties
    P_B = victoire_J2 / nb_parties
    P_0 = parties_nulles / nb_parties
    C_A = nb_coups_j1 / victoire_J1
    C_B = nb_coups_j2 / victoire_J2
  
    if parties_nulles == 0:
        C_0 = 0  # éviter les division par 0 
    else:
        C_0 = nb_coups_nulles / parties_nulles

    print("Nombre de victoires joueur 1: ", victoire_J1)
    print("Nombre de victoires joueur 2: ", victoire_J2)
    print("Nombre de parties nulles: ", parties_nulles)
    print("Probabilité que le joueur 1 gagne: ", P_A)
    print("Probabilité que le joueur 2 gagne: ", P_B)
    print("Probabilité que la partie soit null: ", P_0)

    print("Nombre de coups moyens avant la victoire du Jouer 1 : ", C_A)
    print("Nombre de coups moyens avant la victoire du Jouer 2 : ", C_B)
    print("Nombre de coups moyens avant une partie nulle : ", C_0)

    if esp == 1 :
        P_1 = np.where(tab_1 == 0, 0.0, np.divide(tab_1, nb_parties)) #les prob de gains avec i coups pour joueur 1
        P_2 = np.where(tab_2 == 0, 0.0, np.divide(tab_2, nb_parties)) #les prob de gains avec i coups pour joueur 2

        E_1 = esperance(len(tab_1), P_1)
        E_2 = esperance(len(tab_2), P_2)

        print("Espérance du nombre de coups avant la victoire du joueur 1 : ", E_1)
        print("Espérance du nombre de coups avant la victoire du joueur 2 : ", E_2)

    #graphes
    graphe(tab_res)

def esperance(n, p) :
    """"
    Calcule l'espérance d'une variable aléatoir
    param n: nombre de valeurs pour X
    param p: tableau des p(Xi)
    """
    esp = 0
    for i in range(n) : 
        esp += i*p[i]
    return esp

def graphe(list):
    #listes de données
    data_j1 = [x[1] for x in list if x[0] == 1]
    data_j2 = [x[1] for x in list if x[0] == -1]


    # Créer les histogrammes
    hist_j1, bins_j1 = np.histogram(data_j1, bins=10)
    hist_j2, bins_j2 = np.histogram(data_j2, bins=10)

    # Définir les centres des bacs pour le plotting
    bin_centers_j1 = 0.5 * (bins_j1[:-1] + bins_j1[1:])
    bin_centers_j2 = 0.5 * (bins_j2[:-1] + bins_j2[1:])

    # Créer le graphique
    plt.figure(figsize=(8, 6))

    # Tracer  l'histogramme pour le Joueur 1
    plt.bar(bin_centers_j1, hist_j1, width=1, alpha=0.5, label='Joueur 1', color='blue')

    ## Tracer  l'histogramme pour le Joueur 1
    plt.bar(bin_centers_j2, hist_j2, width=1, alpha=0.5, label='Joueur 2', color='green')

    # Ajouter des étiquettes et un titre
    plt.xlabel('Nombre de coups avant la victoire')
    plt.ylabel('Fréquence')
    plt.title('Distribution du nombre de coups avant la victoire')

    # Ajouter une légende
    plt.legend()

    # Afficher le graphique
    plt.show()
