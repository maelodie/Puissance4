import numpy as np
import pandas as pd
import random
from matplotlib import pyplot
from parametres import *

class Plateau: 
    """
    Classe qui représente le plateau du jeu Puissance 4
    """

    #Attributs statiques
    w_combos = quad_list(NB_LIGNES, NB_COLONNES, PUISSANCE)

    def __init__(self, nb_colonnes, nb_lignes):
        #Attributs de classe
        self.plateau = np.zeros((nb_lignes, nb_colonnes), dtype=int)
        self.filled_cases = np.zeros(NB_COLONNES, dtype=int)
        self.nb_colonnes = nb_colonnes
        self.nb_lignes = nb_lignes
        self.possible_actions = [0,1,2,3,4,5,6]
    
    def reset(self):
        self.plateau = np.zeros(NB_LIGNES, NB_COLONNES)
    
    def show(self):
        """ Affiche le tableau de dimensions nb_lignes  x nb_colonnes"""
        data = self.plateau
        df = pd.DataFrame(data)
        print("Voici un visuel du plateau")
        print(df)

    def is_full(self) :
        """"Renvoie True si le plateau est complet, False sinon"""
        return np.all(self.plateau != 0)
    
    def play(self, x, joueur):
        y = (NB_LIGNES - 1) - self.filled_cases[x]
        self.filled_cases[x] += 1
        self.plateau[y,x] = joueur.id

        if self.filled_cases[x]>=self.nb_lignes :
            self.possible_actions.remove(x)
        

    def has_won(self):
        combo = []
        for quad in self.w_combos:
            combo = [self.plateau[x][y] for x,y in quad]
            if all(item == ID_JOUEUR1 for item in combo) :
                print("Le Joueur 1 a gagné")
                return (True, 1)
            if all(item == ID_JOUEUR2 for item in combo):
                print("Le Joueur 2 a gagné")
                return (True, -1)
        return (False, 0)

class Player:

    def __init__(self, id):
        self.id = id
    
    def play(self, plateau : Plateau, mode):
        """
        Renvoie le coup à jouer pour le joueur
        Si mode vaut 0, l'utilisateur saisie le colonne souhaitée via la ligne de commande
        Si mode vaut 1, on génere une colonne aléatoire
        """
        if self.id == ID_JOUEUR1:
            print("C'est le tour du Joueur 1")
        elif self.id == ID_JOUEUR2:
            print("C'est le tour du Joueur 2")

        if mode == 0 :
            player_input = input("Choisir un entier pour la colonne choisie: ")
            print("Le coup à jouer est la colonne ", int(player_input))
            plateau.play(int(player_input),self)
        if mode==1 :
            player_input = random.choice(plateau.possible_actions)
            print("Le coup à jouer est la colonne ", player_input)
            plateau.play(player_input,self)
