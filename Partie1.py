import numpy as np
from matplotlib import pyplot
from Parametres import NB_COLONNES, NB_LIGNES, PUISSANCE

class Plateau : 
    """
    Classe qui représente le plateau du jeu Puissance 4
    """

    def __init__(self, nb_colonnes, nb_lignes):
        self.nb_colonnes = NB_COLONNES
        self.nb_lignes = NB_LIGNES

           
def quadruplets_lignes(x, y, puissance, my_list):
    for k in range(x) :
        for j in range(y - puissance + 1):  
            quadruple = []
            for i in range(j, j + puissance):
                quadruple.append((k, i))
            my_list.append(quadruple)

def quadruplets_colonnes(x, y, puissance, my_list):
    for j in range(y) :
        for k in range(x - puissance + 1):  
            quadruple = []
            for i in range(k, k + puissance):
                quadruple.append((i, j))
            my_list.append(quadruple)
        
def quadruplets_diagonales_droit(x, y, puissance, my_list) :
    for i in range(x) :
        for j in range(y):
            quadruple=[]
            if j+puissance <= y  and i+puissance<= x :
                for l in range(4) :
                    quadruple.append((i+l ,j + l))
                my_list.append(quadruple)

def quadruplets_diagonales_gauche(x, y, puissance, my_list):
    for i in range(x):
        for j in range(y):
            quadruple = []
            if j - puissance >= -1 and i + puissance <= x:
                for l in range(4):
                    quadruple.append((i + l, j - l))
                my_list.append(quadruple)

def quadruplets_possibles(x, y, puissance) :
    my_list=[]
    quadruplets_lignes(x,y,puissance,my_list)
    quadruplets_colonnes(x,y,puissance,my_list)
    quadruplets_diagonales_droit(x,y,puissance,my_list)
    quadruplets_diagonales_gauche(x,y,puissance,my_list)
    print(my_list)

