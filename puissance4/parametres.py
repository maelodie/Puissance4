NB_COLONNES = 7
NB_LIGNES = 6
PUISSANCE = 4
ID_JOUEUR1 = 1
ID_JOUEUR2 = -1
N = 50      #nb parties aléatoires pour Monte-carlo

def quadruplets_colonnes(x, y, puissance, my_list):
    """"
    Calcule l'ensemble des quadruplets en colonnes gagnants de Puissance 4
    """
    for k in range(x) :
        for j in range(y - puissance + 1):  
            quadruple = set()
            for i in range(j, j + puissance):
                quadruple.add((k, i))
            my_list.append(quadruple)

def quadruplets_lignes(x, y, puissance, my_list):
    """"
    Calcule l'ensemble des quadruplets en lignes gagnants de Puissance 4
    """
    for j in range(y) :
        for k in range(x - puissance + 1):  
            quadruple = set()
            for i in range(k, k + puissance):
                quadruple.add((i, j))
            my_list.append(quadruple)
        
def quadruplets_diagonales_droit(x, y, puissance, my_list) :
    """"
    Calcule l'ensemble des quadruplets diagonales droites gagnants de Puissance 4
    """
    for i in range(x) :
        for j in range(y):
            quadruple= set()
            if j+puissance <= y  and i+puissance<= x :
                for l in range(4) :
                    quadruple.add((i+l ,j + l))
                my_list.append(quadruple)

def quadruplets_diagonales_gauche(x, y, puissance, my_list):
    """"
    Calcule l'ensemble des quadruplets diagonales gauchees gagnants de Puissance 4
    """
    for i in range(x):
        for j in range(y):
            quadruple = set()
            if j - puissance >= -1 and i + puissance <= x:
                for l in range(4):
                    quadruple.add((i + l, j - l))
                my_list.append(quadruple)
    
def quad_list(x, y, puissance) :
    """"
    Renvoie la liste de tous les quadruplets gagnants de Puissance 4 avec un plateau de taille X x Y
    """
    my_list=[]
    quadruplets_lignes(x,y,puissance,my_list)
    quadruplets_colonnes(x,y,puissance,my_list)
    quadruplets_diagonales_droit(x,y,puissance,my_list)
    quadruplets_diagonales_gauche(x,y,puissance,my_list)
    return my_list