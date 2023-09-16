import numpy as np
from matplotlib import pyplot
from parametres import NB_COLONNES, NB_LIGNES

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
            quadruple = set()
            for i in range(j, j + puissance):
                quadruple.add((k, i))
            my_list.append(quadruple)

def quadruplets_colonnes(x, y, puissance, my_list):
    for j in range(y) :
        for k in range(x - puissance + 1):  
            quadruple = set()
            for i in range(k, k + puissance):
                quadruple.add((i, j))
            my_list.append(quadruple)
        
def quadruplets_diagonales_droit(x, y, puissance, my_list) :
    for i in range(x) :
        for j in range(y):
            quadruple= set()
            if j+puissance <= y  and i+puissance<= x :
                for l in range(4) :
                    quadruple.add((i+l ,j + l))
                my_list.append(quadruple)

def quadruplets_diagonales_gauche(x, y, puissance, my_list):
    for i in range(x):
        for j in range(y):
            quadruple = set()
            if j - puissance >= -1 and i + puissance <= x:
                for l in range(4):
                    quadruple.add((i + l, j - l))
                my_list.append(quadruple)
                print(quadruple)
    
my_list=[]
quadruplets_diagonales_gauche(NB_LIGNES,NB_COLONNES,4,my_list)