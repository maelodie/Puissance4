import numpy as np
import pandas as pd
from matplotlib import pyplot
from parametres import *
"""
class Game : 
    def __init__(self, plateau):
        self.plateau = plateau
    
    def 
"""

class Plateau: 
    """
    Classe qui représente le plateau du jeu Puissance 4
    """
    def __init__(self, nb_colonnes, nb_lignes):
        self.plateau = np.zeros((NB_LIGNES, NB_COLONNES), dtype=int)
        self.filled_cases = np.zeros(NB_COLONNES, dtype=int)
        self.nb_colonnes = NB_COLONNES
        self.nb_lignes = NB_LIGNES
    
    def reset(self):
        self.plateau = np.zeros(NB_LIGNES, NB_COLONNES)
    
    def show(self):
        """ Affiche le tableau de dimensions nb_lignes  x nb_colonnes"""
        data = self.plateau
        df = pd.DataFrame(data)
        print(df)
    
    def is_full(self) :
        """"Renvoie True si le plateau est complet, false sinon"""
        return np.all(self.plateau != 0)

    def play(self, x, joueur):
        if self.filled_cases[x] < 6:
            if x > -1 and x < 7:
                y = (NB_LIGNES - 1) - self.filled_cases[x]
                self.filled_cases[x] += 1
                self.plateau[y,x] = joueur.id
            else:
                print("out of borders")
        else:
            print("filled row for row n°:", x)

class Player:
    def __init__(self, id):
        self.id = id

    def play(self, plateau):
        if self.id == ID_JOUEUR1:
            print("C'est le tour du joueur 1")
        elif self.id == ID_JOUEUR2:
            print("C'est le tour du joueur 2")

        player_input = input("Choisir un entier pour la colonne choisie: ")
        plateau.play(player_input,self)
          
