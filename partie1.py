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
        self.plateau = np.zeros((NB_LIGNES, NB_COLONNES))
        self.nb_colonnes = NB_COLONNES
        self.nb_lignes = NB_LIGNES
    
    def reset(self):
        self.plateau = np.zeros(NB_LIGNES, NB_COLONNES)
    
    def show(self):
        data = self.plateau
        df = pd.DataFrame(data)
        print(df)

    def play(self, x, joueur):
        if x > -1 and x < 7:
            print((self.plateau[x, :]==0).argmax())
            y = NB_LIGNES - 1 - (self.plateau[x, :]==0).argmax()
            if y < self.plateau.shape[0]: #s'il y'a une ligne disponible
                self.plateau[y][x] = joueur.id
        else:
            print("out of borders")

class Player:

    def __init__(self, id):
        self.id = id



           
def quadruplets_lignes(x, y, puissance, my_list):
    for k in range(x) :
        for j in range(y - puissance + 1):  
            quadruple = set()
            for i in range(j, j + puissance):
                quadruple.add((k, i))
            my_list.append(quadruple)
            print(quadruple)

def quadruplets_colonnes(x, y, puissance, my_list):
    for j in range(y) :
        for k in range(x - puissance + 1):  
            quadruple = set()
            for i in range(k, k + puissance):
                quadruple.add((i, j))
            my_list.append(quadruple)
            print(quadruple)
        
def quadruplets_diagonales_droit(x, y, puissance, my_list) :
    for i in range(x) :
        for j in range(y):
            quadruple= set()
            if j+puissance <= y  and i+puissance<= x :
                for l in range(4) :
                    quadruple.add((i+l ,j + l))
                my_list.append(quadruple)
                print(quadruple)

def quadruplets_diagonales_gauche(x, y, puissance, my_list):
    for i in range(x):
        for j in range(y):
            quadruple = set()
            if j - puissance >= -1 and i + puissance <= x:
                for l in range(4):
                    quadruple.add((i + l, j - l))
                my_list.append(quadruple)
                print(quadruple)
    
def quadruplets_possibles(x, y, puissance) :
    my_list=[]
    quadruplets_lignes(x,y,puissance,my_list)
    quadruplets_colonnes(x,y,puissance,my_list)
    quadruplets_diagonales_droit(x,y,puissance,my_list)
    quadruplets_diagonales_gauche(x,y,puissance,my_list)
    #print(my_list)